from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

device1 = {
	"host": "x", 
	"username": "x", 
	"password": "x",
	"device_type": "cisco_ios", 
	} 

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show run", use_textfsm=True)

#print(output)

cisco_obj = CiscoConfParse(output.splitlines())
intf = cisco_obj.find_objects(r"^interface")

#take interf with IP
interf_ip = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for x in interf_ip:
	print (x.text)
	print (x.children[0].text)
