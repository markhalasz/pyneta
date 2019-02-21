from netmiko import ConnectHandler
from getpass import getpass
router = Cisco3 (
	host="", 
	username="", 
	password=getpass(), 
	device_type="cisco_nxos", 
	session_log="my_session.txt",)

net_connect = ConnectHandler(**router)
print(net_connect.find_prompt())
