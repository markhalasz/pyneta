from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")



vrf_list [
	{"vrf_name": "blue1", "ipv4_enabled": True, "ipv6_enabled": True,"red": "100:1"}
	{"vrf_name": "blue2, "ipv4_enabled": True, "ipv6_enabled": True,"red": "200:2"}
]

vrf_vars = {"vrf_list": vrf_list}

my_template = "bgp_template.j2"
j2_template = env.get_template(my_template)
output = j2_template.render(**vrf_vars)
print(output)



