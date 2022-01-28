import netmiko
from getpass import getpass


IP = "10.10.221.176"
USERNAME = "dadmin"
PASSWORD = "dadmin01"
DEVICE_TYPE = "cisco_nxos"
CONN_TIMEOUT = 120


def main():
    
    sshTemplate = {
        'username' : USERNAME or input("Please enter your username: "),
        'password' : PASSWORD or getpass("Please enter your password: "),
        'ip' : IP or input("Please enter device IP: "),
        'device_type' : DEVICE_TYPE or input("Please Enter Device Type: "),
        'conn_timeout' : CONN_TIMEOUT or 15,
        "fast_cli": False,
    }

    connection = netmiko.Netmiko(**sshTemplate)

    commands = [
        'almsnmpconf',
        'almsnmpconf'
    ]

    results = []

    for command in commands:
        results.append(connection.send_command(command))

    with open('results.txt', 'w') as file:
        file.writelines(results)


if __name__ == '__main__':
    main()