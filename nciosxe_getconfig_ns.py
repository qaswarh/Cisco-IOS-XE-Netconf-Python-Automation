from argparse import ArgumentParser
from ncclient import manager
import xml.dom.minidom

def netconf_config(ns):
    if ns == 'complete':
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running')))
        print(xmlDom.toprettyxml( indent = "  " ))
    elif ns == 'app-hosting':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns}-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-{ns}-cfg">' + \
                          f'</{ns}-cfg-data>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'native':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-{ns}">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'netconf-yang':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="http://cisco.com/yang/cisco-self-mgmt">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'licensing':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="http://cisco.com/ns/yang/cisco-smart-license">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))
        
    elif ns == 'interfaces':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="urn:ietf:params:xml:ns:yang:ietf-{ns}">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'nacm':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))        
    elif ns == 'routing':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="urn:ietf:params:xml:ns:yang:ietf-{ns}">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'acl':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="http://openconfig.net/yang/{ns}">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif ns == 'network-instances':
        ns_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{ns} xmlns="http://openconfig.net/yang/network-instance">' + \
                          f'</{ns}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',ns_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))
    else:
        print("Available ns choices are: app-hosting, native, netconf-yang, licensing, interfaces, nacm, routing, acl and network-instances. Type complete for entire configuration")


if __name__ == '__main__':
    parser = ArgumentParser(description='Credentials and XPath')
    parser.add_argument('--host', type=str, required=True, help="The device IP address or Domain Name")
    parser.add_argument('-ns', '--namespace', type=str, required=True, help="Filters configuration per namespace: app-hosting, native, netconf-yang, licensing, interfaces, nacm, routing, acl and network-instances")
    parser.add_argument('-u', '--username', type=str, default='cisco', help="check info at https://devnetsandbox.cisco.com/RM/Topology")
    parser.add_argument('-p', '--password', type=str, default='cisco', help="check info at https://devnetsandbox.cisco.com/RM/Topology")
    parser.add_argument('--port', type=int, default=830, help="Specify this if a non-default port to be used")
    args = parser.parse_args()

    m =  manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         device_params={'name':"csr"})

    netconf_config(args.namespace)



        
        
        
