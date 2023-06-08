# Cisco-IOS-XE-Netconf-Python-Automation
If you've intenet then explore [Cisco IOS XE CSR](https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology) Netconf config with Python<br>
All you need a Linux Box (ADM Server aka Jump Server) with Python installed<br>
Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to experience it from Windows machine<br>

**RPC Get**<br>
Use nciosxe_getconfig_ns.py as per help:<br>
![image](https://user-images.githubusercontent.com/47313728/235594887-c5b89c5e-361b-42fd-a6c9-7b2d8c5041bc.png)
nciosxe_getconfig_ns.py will yield same results as nciosxe_getconfig.yml in Ansible automation repo for nciosxe<br>
NAMESPACES in the help are for the user to input, scritp will translate to actual being used.<br>

You can do xmltodict in any namespace and get status/health  

        interface = xmlDom.toprettyxml( indent = "  " )
        netconf_data = xmltodict.parse(interface)["rpc-reply"]["data"]
        interfaces = netconf_data["interfaces"]["interface"]
        for interface in interfaces:
            if interface["enabled"] == 'true':
                print("Interface {} is Up".format(interface["name"]))
            else:
                print("Interface {} is Down".format(interface["name"]))


Adding above lines in the namespace 'interfaces' would yeild

![image](https://github.com/qaswarh/Cisco-IOS-XE-Netconf-Python-Automation/assets/47313728/fa49fc57-18ff-47a2-bdb0-6f664bcddc89)

