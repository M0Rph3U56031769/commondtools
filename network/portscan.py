"""
Simple port scan tool
"""

import sys
import socket


class PortScan:

    @staticmethod
    def portScan(host: str, port: int):
        ip = socket.gethostbyname(host)

        if port == "full":
            print("Executing full port scan. It can take 2-5 minutes...")
            try:
                # will scan ports between 1 to 65,535
                for port_number in range(1, 65535):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)

                    # returns an error indicator
                    scan_result = s.connect_ex((ip, port_number))
                    s.close()
                    if scan_result == 0:
                        print("Port {} is open".format(port_number))
                        return True
                    else:
                        print("Port {} is closed".format(port_number))
                        return False

            except KeyboardInterrupt:
                print("\n Exitting Program !!!!")
                sys.exit(1)
            except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit(1)
            except socket.error:
                print("\n Server not responding !!!!")
                sys.exit(1)
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # returns an error indicator
                scan_result = s.connect_ex((ip, port))
                s.close()
                if scan_result == 0:
                    print("Port {} is open".format(port))
                    return True
                else:
                    print("Port {} is closed".format(port))
                    return False
            except KeyboardInterrupt:
                print("\n Exitting Program !!!!")
                sys.exit(1)
            except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit(1)
            except socket.error:
                print("\n Server not responding !!!!")
                sys.exit(1)


if __name__ == '__main__':
    print(PortScan.portScan("epm.mphr11.morpho.com", 1433))
    # print("PORT SCANNER")
    #
    # # Defining a target
    # HOST: str = ""
    # PORT: int = -1
    #
    # if len(sys.argv) != 3:
    #     print("Invalid ammount of Argument")
    #     HOST = input("Give me the host name or IP: ")
    #     PORT = int(input("...and now the port(type 'full' if you want a full scan): "))
    # else:
    #     HOST = sys.argv[1]
    #     PORT = int(sys.argv[2])
    #
    # # translate hostname to IPv4
    # target = socket.gethostbyname(HOST)
    #
    # # Add Banner
    # print("-" * 50)
    # print("Scanning Target Host: " + HOST + " : " + target)
    # print("Scanning Target Port: " + str(PORT))
    # print("Scanning started at: " + str(datetime.now()))
    # print("-" * 50)
    #
    # if PORT == "full":
    #     print("Executing full port scan. It can take 2-5 minutes...")
    #     try:
    #         # will scan ports between 1 to 65,535
    #         for port in range(1, 65535):
    #             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #             socket.setdefaulttimeout(1)
    #
    #             # returns an error indicator
    #             result = s.connect_ex((target, port))
    #             if result == 0:
    #                 print("Port {} is open".format(port))
    #             s.close()
    #
    #     except KeyboardInterrupt:
    #         print("\n Exitting Program !!!!")
    #         sys.exit()
    #     except socket.gaierror:
    #         print("\n Hostname Could Not Be Resolved !!!!")
    #         sys.exit()
    #     except socket.error:
    #         print("\n Server not responding !!!!")
    #         sys.exit()
    # else:
    #     try:
    #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         socket.setdefaulttimeout(1)
    #
    #         # returns an error indicator
    #         result = s.connect_ex((target, PORT))
    #         if result == 0:
    #             print("Port {} is open".format(PORT))
    #         else:
    #             print("Port {} is closed".format(PORT))
    #         s.close()
    #     except KeyboardInterrupt:
    #         print("\n Exitting Program !!!!")
    #         sys.exit()
    #     except socket.gaierror:
    #         print("\n Hostname Could Not Be Resolved !!!!")
    #         sys.exit()
    #     except socket.error:
    #         print("\n Server not responding !!!!")
    #         sys.exit()
