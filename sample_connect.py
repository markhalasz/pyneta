from netmiko import ConnectHandler
from getpass import getpass
net_connect = ConnectHandler(
	host="", 
	username="", 
	password=getpass(), 
	device_type="cisco_nxos", 
	session_log="my_session.txt",)

print(net_connect.find_prompt())
