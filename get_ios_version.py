from netmiko import ConnectHandler
from getpass import getpass

ios_devices = [
	{
	"host": "cisco3.lasthop.io", 
	"username": "pyclass", 
	"password": getpass(), 
	"device_type": "cisco_nxos", 
	#"session_log": "my_session.txt",
	}
	# ,
	#{
	#"host": "nxos2.lasthop.io",
        #"username": "pyclass",
        #"password": getpass(),
        #"device_type": "cisco_nxos",
	#}""
]

for device in ios_devices:
	net_connect = ConnectHandler(**device)
	print(net_connect.find_prompt())
	output = net_connect.send_command("show version")
	print(output)
