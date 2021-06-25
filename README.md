# pulumi-aws-setup

## Run instruction in run.txt

## Sampple Outputs:

### Preview

```bash
$ pulumi preview
Please choose a stack, or create a new one: dev
Previewing update (dev):
     Type                              Name                               Plan
 +   pulumi:pulumi:Stack               pulumi-aws-setup-dev               create
 +   ├─ aws:ec2:Eip                    NatGatewayEIP                      create
 +   ├─ aws:ec2:Vpc                    YogeshSharmaPulumi                 create
 +   ├─ aws:ec2:InternetGateway        YogeshSharmaPulumi-ig              create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz1                   create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz2                   create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz3                   create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz1                    create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz2                    create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz3                    create
 +   ├─ aws:ec2:RouteTable             publicroutetable-vpc-route-table   create
 +   ├─ aws:ec2:NatGateway             NatGateway-YogeshSharmaPulumi      create
 +   ├─ aws:ec2:RouteTable             privateroutetable-vpc-route-table  create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-1     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-2     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-3     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-1    create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-2    create
 +   └─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-3    create

Resources:
    + 19 to create
```


### Up (Apply)

```bash
pulumi up
Please choose a stack, or create a new one: dev
Previewing update (dev):
     Type                              Name                               Plan
 +   pulumi:pulumi:Stack               pulumi-aws-setup-dev               create
 +   ├─ aws:ec2:Eip                    NatGatewayEIP                      create
 +   ├─ aws:ec2:Vpc                    YogeshSharmaPulumi                 create
 +   ├─ aws:ec2:InternetGateway        YogeshSharmaPulumi-ig              create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz1                   create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz3                   create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz1                    create
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz2                   create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz2                    create
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz3                    create
 +   ├─ aws:ec2:RouteTable             publicroutetable-vpc-route-table   create
 +   ├─ aws:ec2:NatGateway             NatGateway-YogeshSharmaPulumi      create
 +   ├─ aws:ec2:RouteTable             privateroutetable-vpc-route-table  create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-1     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-2     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-3     create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-1    create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-2    create
 +   └─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-3    create

Resources:
    + 19 to create

Do you want to perform this update? yes
Updating (dev):
     Type                              Name                               Status
 +   pulumi:pulumi:Stack               pulumi-aws-setup-dev               created
 +   ├─ aws:ec2:Eip                    NatGatewayEIP                      created
 +   ├─ aws:ec2:Vpc                    YogeshSharmaPulumi                 created
 +   ├─ aws:ec2:InternetGateway        YogeshSharmaPulumi-ig              created
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz1                   created
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz2                   created
 +   ├─ aws:ec2:Subnet                 PrivateSubnetAz3                   created
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz1                    created
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz2                    created
 +   ├─ aws:ec2:Subnet                 PublicSubnetAz3                    created
 +   ├─ aws:ec2:NatGateway             NatGateway-YogeshSharmaPulumi      created
 +   ├─ aws:ec2:RouteTable             publicroutetable-vpc-route-table   created
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-1     created
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-2     created
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-3     created
 +   ├─ aws:ec2:RouteTable             privateroutetable-vpc-route-table  created
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-1    created
 +   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-2    created
 +   └─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-3    created

Outputs:
    private_privatesubnetaz1                                                                                             : "subnet-0a31fc91511081080"
    private_privatesubnetaz2                                                                                             : "subnet-041caa1d01b462dde"
    private_privatesubnetaz3                                                                                             : "subnet-0cd4755cd37cfea33"
    public_publicsubnetaz1                                                                                               : "subnet-0f77c19eed7f628bb"
    public_publicsubnetaz2                                                                                               : "subnet-06f7c4b7ed94e4b55"
    public_publicsubnetaz3                                                                                               : "subnet-0c827a1b932798c55"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af44310>-<pulumi.output.Output object at 0x7fe19afb7190>: "rtbassoc-0b0cce330180ee037"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af4eb10>-<pulumi.output.Output object at 0x7fe19afb7190>: "rtbassoc-0ff113b0a6d8949a4"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af61350>-<pulumi.output.Output object at 0x7fe19afb7190>: "rtbassoc-06eb72758e50aaa84"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af6ab50>-<pulumi.output.Output object at 0x7fe19afb1150>: "rtbassoc-018cc50b0fea44feb"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af7a390>-<pulumi.output.Output object at 0x7fe19afb1150>: "rtbassoc-04fa3494847545621"
    vpc-route-table-assoc-<pulumi.output.Output object at 0x7fe19af83b90>-<pulumi.output.Output object at 0x7fe19afb1150>: "rtbassoc-004583c761621b740"

Resources:
    + 19 created

Duration: 1m33s
```

### Destroy

```bash
$ pulumi destroy
Please choose a stack: dev
Previewing destroy (dev):
     Type                              Name                               Plan
 -   pulumi:pulumi:Stack               pulumi-aws-setup-dev               delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-1    delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-3    delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-2    delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-2     delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-1     delete
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-3     delete
 -   ├─ aws:ec2:RouteTable             privateroutetable-vpc-route-table  delete
 -   ├─ aws:ec2:RouteTable             publicroutetable-vpc-route-table   delete
 -   ├─ aws:ec2:NatGateway             NatGateway-YogeshSharmaPulumi      delete
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz3                    delete
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz1                    delete
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz2                    delete
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz3                   delete
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz1                   delete
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz2                   delete
 -   ├─ aws:ec2:InternetGateway        YogeshSharmaPulumi-ig              delete
 -   ├─ aws:ec2:Eip                    NatGatewayEIP                      delete
 -   └─ aws:ec2:Vpc                    YogeshSharmaPulumi                 delete

Outputs:
  - private_privatesubnetaz1       : "subnet-0a31fc91511081080"
  - private_privatesubnetaz2       : "subnet-041caa1d01b462dde"
  - private_privatesubnetaz3       : "subnet-0cd4755cd37cfea33"
  - public_publicsubnetaz1         : "subnet-0f77c19eed7f628bb"
  - public_publicsubnetaz2         : "subnet-06f7c4b7ed94e4b55"
  - public_publicsubnetaz3         : "subnet-0c827a1b932798c55"
  - vpc-route-table-assoc-private-1: "rtbassoc-0b0cce330180ee037"
  - vpc-route-table-assoc-private-2: "rtbassoc-0ff113b0a6d8949a4"
  - vpc-route-table-assoc-private-3: "rtbassoc-06eb72758e50aaa84"
  - vpc-route-table-assoc-public-1 : "rtbassoc-018cc50b0fea44feb"
  - vpc-route-table-assoc-public-2 : "rtbassoc-04fa3494847545621"
  - vpc-route-table-assoc-public-3 : "rtbassoc-004583c761621b740"

Resources:
    - 19 to delete

Do you want to perform this destroy? yes
Destroying (dev):
     Type                              Name                               Status
 -   pulumi:pulumi:Stack               pulumi-aws-setup-dev               deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-3    deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-2    deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-private-1    deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-3     deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-1     deleted
 -   ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-public-2     deleted
 -   ├─ aws:ec2:RouteTable             privateroutetable-vpc-route-table  deleted
 -   ├─ aws:ec2:NatGateway             NatGateway-YogeshSharmaPulumi      deleted
 -   ├─ aws:ec2:RouteTable             publicroutetable-vpc-route-table   deleted
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz2                    deleted
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz3                   deleted
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz1                    deleted
 -   ├─ aws:ec2:InternetGateway        YogeshSharmaPulumi-ig              deleted
 -   ├─ aws:ec2:Subnet                 PublicSubnetAz3                    deleted
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz1                   deleted
 -   ├─ aws:ec2:Subnet                 PrivateSubnetAz2                   deleted
 -   ├─ aws:ec2:Eip                    NatGatewayEIP                      deleted
 -   └─ aws:ec2:Vpc                    YogeshSharmaPulumi                 deleted

Outputs:
  - private_privatesubnetaz1       : "subnet-0a31fc91511081080"
  - private_privatesubnetaz2       : "subnet-041caa1d01b462dde"
  - private_privatesubnetaz3       : "subnet-0cd4755cd37cfea33"
  - public_publicsubnetaz1         : "subnet-0f77c19eed7f628bb"
  - public_publicsubnetaz2         : "subnet-06f7c4b7ed94e4b55"
  - public_publicsubnetaz3         : "subnet-0c827a1b932798c55"
  - vpc-route-table-assoc-private-1: "rtbassoc-0b0cce330180ee037"
  - vpc-route-table-assoc-private-2: "rtbassoc-0ff113b0a6d8949a4"
  - vpc-route-table-assoc-private-3: "rtbassoc-06eb72758e50aaa84"
  - vpc-route-table-assoc-public-1 : "rtbassoc-018cc50b0fea44feb"
  - vpc-route-table-assoc-public-2 : "rtbassoc-04fa3494847545621"
  - vpc-route-table-assoc-public-3 : "rtbassoc-004583c761621b740"

Resources:
    - 19 deleted

Duration: 1m21s
```