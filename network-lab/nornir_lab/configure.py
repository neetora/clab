from nornir import InitNornir
from nornir_netmiko import netmiko_send_config

def configure_vlan(task):
    task.run(task=netmiko_send_config, config_commands=[
        "vlan 10",
        "name Sales",
        "vlan 20",
        "name Marketing",
        "vlan 30",
        "name Engineering",
        "vlan 40",
        "name HR",
        "vlan 50",
        "name IT",
        "vlan 60",
        "name Finance",
        "vlan 70",
        "name Guest",
        "vlan 80",
        "name R&D",
        "vlan 90",
        "name Management",
        "vlan 100",
        "name Voice",
    ])

def enable_dot1x(task):
    task.run(task=netmiko_send_config, config_commands=[
        "aaa new-model",
        "dot1x system-auth-control",
        "interface Ethernet1",
        "switchport mode access",
        "switchport access vlan 10",  # Example for VLAN 10
        "dot1x port-control auto",
        "exit",
        "interface Ethernet2",
        "switchport mode access",
        "switchport access vlan 20",  # Example for VLAN 20
        "dot1x port-control auto",
        "exit",
    ])

def enable_dhcp_snooping(task):
    task.run(task=netmiko_send_config, config_commands=[
        "ip dhcp snooping",
        "ip dhcp snooping vlan 10",
        "ip dhcp snooping vlan 20",
        "ip dhcp snooping vlan 30",
        "ip dhcp snooping vlan 40",
        "ip dhcp snooping vlan 50",
        "interface Ethernet1",
        "ip dhcp snooping trust",
        "exit",
        "interface Ethernet2",
        "ip dhcp snooping trust",
        "exit",
    ])

if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr.run(task=configure_vlan)
    nr.run(task=enable_dot1x)
    nr.run(task=enable_dhcp_snooping)
