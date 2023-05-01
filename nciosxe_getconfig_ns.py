from argparse import ArgumentParser
from ncclient import manager
import xml.dom.minidom

def netconf_config(sect):
    if sect == 'complete':
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running')))
        print(xmlDom.toprettyxml( indent = "  " ))
    elif sect == 'app-hosting':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect}-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-{sect}-cfg">' + \
                          f'</{sect}-cfg-data>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'native':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-{sect}">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'netconf-yang':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="http://cisco.com/yang/cisco-self-mgmt">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'licensing':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="http://cisco.com/ns/yang/cisco-smart-license">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'interfaces':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="urn:ietf:params:xml:ns:yang:ietf-{sect}">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'nacm':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'routing':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="urn:ietf:params:xml:ns:yang:ietf-{sect}">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'acl':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="http://openconfig.net/yang/{sect}">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))

    elif sect == 'network-instances':
        xpath_filter = '<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">' + \
                          f'<{sect} xmlns="http://openconfig.net/yang/network-instance">' + \
                          f'</{sect}>' + \
                      '</filter>'
        xmlDom = xml.dom.minidom.parseString( str( m.get_config('running',xpath_filter)))
        print(xmlDom.toprettyxml( indent = "  " ))
    else:
        print("Available xpath choices are: app-hosting, native, netconf-yang, licensing, interfaces, nacm, routing, acl and network-instances. Type complete for entire configuration")


if __name__ == '__main__':
    parser = ArgumentParser(description='Credentials and XPath')
    parser.add_argument('--host', type=str, required=True, help="The device IP address or Domain Name")
    parser.add_argument('--xpath', type=str, required=True, help="The Netconf Configuration section - XMLPath")
    parser.add_argument('-u', '--username', type=str, default='cisco', help="check info at https://devnetsandbox.cisco.com/RM/Topology")
    parser.add_argument('-p', '--password', type=str, default='cisco', help="check info at https://devnetsandbox.cisco.com/RM/Topology")
    parser.add_argument('--port', type=int, default=830, help="Specify this if a non-default port to be used")
    args = parser.parse_args()

    m =  manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         device_params={'name':"csr"})

    netconf_config(args.xpath)
        
