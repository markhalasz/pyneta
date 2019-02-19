from netmiko import ConnectHandler
from getpass import getpass

device1 = {
	"host": "cisco4.lasthop.io", 
	"username": "pyclass", 
	"password": "88newclass", 
	"device_type": "cisco_ios", 
	#"global_delay_factor":2,
	} 

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show lld neigh d", delay_factor=8, strip_prompt=False, strip_command=False)
#output = net_connect.send_command("show ip arp", use_textfsm=True)
print(output)
#net_connect.disconnect()
