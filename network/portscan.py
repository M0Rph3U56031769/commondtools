# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # import pyfiglet
    import sys
    import socket
    from datetime import datetime

    # ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    # print(ascii_banner)
    print("PORT SCANNER")
    # Defining a target
    HOST: str = ""
    PORT: int = -1

    if len(sys.argv) != 3:
        print("Invalid ammount of Argument")
        HOST = input("Give me the host name or IP: ")
        PORT = int(input("...and now the port(type 'full' if you want a full scan): "))
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        
    # translate hostname to IPv4
    target = socket.gethostbyname(HOST)

    # Add Banner
    print("-" * 50)
    print("Scanning Target Host: " + HOST + " : " + target)
    print("Scanning Target Port: " + str(PORT))
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)

    if PORT == "full":
        print("Executing full port scan. It can take 2-5 minutes...")
        try:
            # will scan ports between 1 to 65,535
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # returns an error indicator
                result = s.connect_ex((target, port))
                if result == 0:
                    print("Port {} is open".format(port))
                s.close()

        except KeyboardInterrupt:
            print("\n Exitting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\n Server not responding !!!!")
            sys.exit()
    else:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target, PORT))
            if result == 0:
                print("Port {} is open".format(PORT))
            else:
                print("Port {} is closed".format(PORT))
            s.close()
        except KeyboardInterrupt:
            print("\n Exitting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\n Server not responding !!!!")
            sys.exit()
