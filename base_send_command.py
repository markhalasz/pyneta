from netmiko import ConnectHandler
from getpass import getpass

device1 = {
	"host": "cisco4.lasthop.io", 
	"username": "pyclass", 
	"password": "88newclass", 
	"device_type": "cisco_ios", 
	} 

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

#output = net_connect.send_command("show ip arp", use_textfsm=True)
#print(output)
#net_connect.disconnect()
