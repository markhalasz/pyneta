from netmiko import ConnectHandler, file_transfer
from getpass import getpass

ios_devices = {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": "88newclass",
        "device_type": "cisco_ios",
}


source_file = "testTofu.txt"
dest_file = "testTofuBack.txt"
direction = "get"
file_system = "bootflash:"

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**ios_devices)
transfer_dict = file_transfer(
	ssh_conn,
	source_file=source_file,
	dest_file=dest_file,
	file_system=file_system,
	direction=direction,
	overwrite_file=True,
)

print(transfer_dict)
