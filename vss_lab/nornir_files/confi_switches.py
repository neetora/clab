from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Define your configuration commands
commands = [
    "switch virtual",
    "switch virtual mac-address 00:11:22:33:44:55",
    "interface Ethernet1/1",
    "switchport mode trunk",
    "switchport trunk allowed vlan all",
    "interface Ethernet1/2",
    "switchport mode access",
    "switchport access vlan 10",
]

# Apply configuration
result = nr.run(task=netmiko_send_config, config_commands=commands)

# Print results
for host in result:
    print(f"{host}: {result[host][0].result}")
