import multiprocessing.dummy
import subprocess


class Pinger:

    @staticmethod
    def ping(ip, liveoutput: bool = False):
        """

        :param liveoutput:
        :param ip:
        :return:
        """
        # get response time in ms or None if host not reached in 1 sec
        success = Pinger.singleping(hostname=ip)  # Run the ping command here
        if liveoutput:
            print("Live output enabled:")
            if success:
                print("{} responded".format(ip))
            else:
                print("{} did not respond".format(ip))
        return {ip: success}
        # return success

    @staticmethod
    def ping_range(network: str = "192.168.0.", start: int = 1, end: int = 254, liveoutput: bool = False):
        """

        :param liveoutput: is console output live, or just get the result at the end
        :type liveoutput: bool
        :param network: subnet (currently only /24 is implemented)
        :type network: str
        :param start: first host number
        :type start: int
        :param end: last host number
        :type end: int
        """
        # TODO: https://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments
        from itertools import product
        num_threads = 2 * multiprocessing.cpu_count()

        with multiprocessing.Pool(processes=num_threads) as pool:
            results = pool.starmap(Pinger.ping, product([network + str(x) for x in range(start, end)]), liveoutput)

        return results

    @staticmethod
    def singleping(hostname: str):
        """
        Ping only 1 times

        :param hostname: hostname to ping
        :type hostname: str
        :return: result of ping: str
        """
        output = subprocess.getoutput("timeout 1 ping -c 1 " + hostname).split(" ")
        for i in output:
            if "time=" in i:
                response = i.split("=")
                return response[1]


if __name__ == "__main__":
    print(Pinger.ping_range(network="192.168.0.", start=1, end=81, liveoutput=True))
