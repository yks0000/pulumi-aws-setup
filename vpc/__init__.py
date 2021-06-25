import pulumi_aws as aws
import pulumi


class VPC:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.vpc_id = None
        self.internet_gateway_id = None
        self.nat_gateway_id = None
        self.public_subnets = []
        self.private_subnets = []

    @staticmethod
    def create_eip():
        return aws.ec2.Eip(resource_name="NatGatewayEIP").id

    def create_vpc(self):
        vpc = aws.ec2.Vpc(
            resource_name=self.kwargs['vpc_name'],
            cidr_block=self.kwargs['vpc_cidr_block'],
            tags={**self.kwargs['default_tags'], **{"Name": self.kwargs['vpc_name']}}
        )
        self.vpc_id = vpc.id

    def create_igw(self):
        igw = aws.ec2.InternetGateway(
            f'{self.kwargs["vpc_name"]}-ig',
            vpc_id=self.vpc_id,
            tags={**self.kwargs['default_tags'], **{"Name": f'{self.kwargs["vpc_name"]}-ig'}}
        )
        self.internet_gateway_id = igw.id

    def create_nat_gateway(self, subnet_id):
        nat_gw = aws.ec2.NatGateway(
            resource_name=f'NatGateway-{self.kwargs["vpc_name"]}',
            subnet_id=subnet_id,
            tags={**self.kwargs['default_tags'], **{"Name": f'{self.kwargs["vpc_name"]}-ig'}},
            allocation_id=self.create_eip()

        )
        self.nat_gateway_id = nat_gw.id

    def create_route_table(self, public=False, igw_id=None, nat_id=None):
        if not public:
            name = f"PrivateRouteTable"
            if not nat_id:
                raise ValueError("Internet Gateway can not be empty for Private Subnets")

            rt_args = aws.ec2.RouteTableRouteArgs(
                cidr_block='0.0.0.0/0',
                nat_gateway_id=nat_id,
            )

        else:
            name = f"PublicRouteTable"
            if not igw_id:
                raise ValueError("Internet Gateway can not be empty for Public Subnets")

            rt_args = aws.ec2.RouteTableRouteArgs(
                cidr_block='0.0.0.0/0',
                gateway_id=igw_id,
            )
        route_table = aws.ec2.RouteTable(
            f'{name.lower()}-vpc-route-table',
            vpc_id=self.vpc_id,
            routes=[rt_args],
            tags={
                'Name': name,
            },
        )
        return route_table.id

    @staticmethod
    def _create_subnet(subnet_name, availability_zone, cidr_block, vpc_id):
        subnet = aws.ec2.Subnet(
            resource_name=subnet_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc_id=vpc_id,
            tags={"Name": subnet_name}
        )
        return subnet.id

    def create_subnet(self):
        for subnet_name, subnet_config in self.kwargs['private_subnet_list'].items():
            subnet_id = self._create_subnet(subnet_name=subnet_name,
                                            availability_zone=subnet_config['availability_zone'],
                                            cidr_block=subnet_config['cidr_block'],
                                            vpc_id=self.vpc_id
                                            )
            pulumi.export(f'private_{str(subnet_name).lower()}', subnet_id)
            self.private_subnets.append(subnet_id)

        if 'public_subnet_list' in self.kwargs and self.kwargs['public_subnet_list']:
            for subnet_name, subnet_config in self.kwargs['public_subnet_list'].items():
                subnet_id = self._create_subnet(subnet_name=subnet_name,
                                                availability_zone=subnet_config['availability_zone'],
                                                cidr_block=subnet_config['cidr_block'],
                                                vpc_id=self.vpc_id
                                                )
                pulumi.export(f'public_{str(subnet_name).lower()}', subnet_id)
                self.public_subnets.append(subnet_id)

    def route_table_association(self, private_route_id, public_route_id=None):
        private_subnet_id = 1
        public_subnet_id = 1
        for subnet in self.private_subnets:
            rt_association = aws.ec2.RouteTableAssociation(
                resource_name=f'vpc-route-table-assoc-private-{private_subnet_id}',
                route_table_id=private_route_id,
                subnet_id=subnet,
            )
            pulumi.export(f'vpc-route-table-assoc-private-{private_subnet_id}', rt_association.id)
            private_subnet_id += 1

        for subnet in self.public_subnets:
            rt_association = aws.ec2.RouteTableAssociation(
                resource_name=f'vpc-route-table-assoc-public-{public_subnet_id}',
                route_table_id=public_route_id,
                subnet_id=subnet,
            )
            pulumi.export(f'vpc-route-table-assoc-public-{public_subnet_id}', rt_association.id)
            public_subnet_id += 1

    def create(self):
        self.create_vpc()
        self.create_igw()
        self.create_subnet()
        self.create_nat_gateway(subnet_id=self.public_subnets[0])
        public_route_id = self.create_route_table(public=True, igw_id=self.internet_gateway_id)
        private_route_id = self.create_route_table(public=False, nat_id=self.nat_gateway_id)
        self.route_table_association(private_route_id=private_route_id, public_route_id=public_route_id)

