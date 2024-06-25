import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac_name", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help more info")
    elif not options.mac_name:
        parser.error("[-] Please specify an new mac, use --help more info")
    return options
def change_mac(interface, mac_name):
    print("[+] Changing mac address " + mac_name)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_name])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Culd not read MAC ADDRESS!")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.mac_name)
current_mac = get_current_mac(options.interface)

if current_mac == options.mac_name:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-} MAC address did not get changed.")




