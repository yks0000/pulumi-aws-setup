"""An AWS Python Pulumi program"""

import pulumi
from vpc import VPC

config = pulumi.Config()
vpc_setup = config.get_object("vpc_setup")
subnet_list = config.get_object("subnet_list")
default_tags = config.get_object("tags")
input_list = {**vpc_setup, **subnet_list}
input_list = {**default_tags, **input_list}
VPC(**input_list).create()
