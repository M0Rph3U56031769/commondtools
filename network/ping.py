import subprocess
import multiprocessing.dummy


class Pinger:

    def ping(self, ip):
        """

        :param ip:
        :return:
        """
        success = self.singleping(hostname=ip)  # Run the ping command here
        if success:
            print("{} responded".format(ip))
        else:
            print("{} did not respond".format(ip))
        print(success)
        return success

    def ping_range(self, network: str = "192.168.2.", start: int = 1, end: int = 254):
        """

        :param network:
        :param start:
        :param end:
        """

        num_threads = 2 * multiprocessing.cpu_count()
        p = multiprocessing.dummy.Pool(num_threads)
        # for i in range(start,end)

        p.map(self.ping, [network + str(x) for x in range(start, end)])

    @staticmethod
    def singleping(hostname):
        """

                :param hostname:
                :return:
                """
        output = subprocess.getoutput("timeout 1 ping -c 1 " + hostname).split(" ")
        for i in output:
            if "time=" in i:
                response = i.split("=")
                return response[1]


if __name__ == "__main__":
    p = Pinger()
    p.ping_range()
