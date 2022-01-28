from getpass import getpass
import netmiko

IP       : str = "10.12.222.113"
HOSTNAME : str = "Test Devices"
DEVICE_TYPE : str = "cisco_nxos"

USERNAME : str = "admin"
PASSWORD : str = ""
PORT : str = ""

def main():

    # Create Initial Connection Template
    sshTemplate = {
        'username' : USERNAME or input("Please Enter Username: "),
        'password' : PASSWORD or getpass("Please enter your password: "),
        'device_type' : DEVICE_TYPE or input("Please Enter Device Type: "),
        'ip' : IP or input("Please enter device IP: "),
    }

    # Connect to Inital Device
    conn = netmiko.Netmiko(**sshTemplate)
    
    # Send Command to Initial Device
    res = conn.send_command('show cdp neighbors detail', use_textfsm=True)

    # Set Up Sets
    devicesConnectedTo = set([sshTemplate['ip']])
    devicesToConnectTo = set()

    # Populate original devices to connect to
    for device in res:
        ip = device['interface_ip']
        devicesToConnectTo.add(ip)

    # Connect to devices in set while we can
    while(devicesToConnectTo):

        # Note that we connected to new device
        devicesConnectedTo.add(ip)

        # Update SSH Template to connect to new device
        ip = devicesToConnectTo.pop()
        sshTemplate['ip'] = ip

        # Make sure we haven't connect already
        if ip not in devicesConnectedTo:
            try:
                # Connect to new device and get neighbors
                conn = netmiko.Netmiko(**sshTemplate)
                newRes = conn.send_command('show cdp neighbors detail', use_textfsm=True)

                # Add neighbors to devices to connect to
                for device in newRes:
                    ip = device['interface_ip']
                    devicesToConnectTo.add(ip)

            except Exception as e:
                print(f"Failed to connect to {ip}")


    print(devicesConnectedTo)



if __name__ == '__main__':
    main()

