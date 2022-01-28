from getpass import getpass
import netmiko

IP       : str = ""
HOSTNAME : str = ""
DEVICE_TYPE : str = "cisco_nxos"

USERNAME : str = ""
PASSWORD : str = ""
PORT : str = ""

def main():
    sshTemplate = {
        'username' : USERNAME or input("Please Enter Username: "),
        'password' : PASSWORD or getpass("Please enter your password: "),
        'device_type' : DEVICE_TYPE or input("Please Enter Device Type: "),
        'ip' : IP or input("Please enter device IP: "),
    }

    conn = netmiko.Netmiko(**sshTemplate)
    res = conn.send_command('show cdp neighbors detail')

    print(res)



if __name__ == '__main__':
    main()