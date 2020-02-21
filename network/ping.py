import subprocess
import multiprocessing.dummy


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

        :param liveoutput:
        :param network:
        :param start:
        :param end:
        """
        from itertools import product
        num_threads = 2 * multiprocessing.cpu_count()
        # p = multiprocessing.dummy.Pool(num_threads)
        # result = p.map(Pinger.ping, [network + str(x) for x in range(start, end)])

        with multiprocessing.Pool(processes=num_threads) as pool:
            results = pool.starmap(Pinger.ping, product([network + str(x) for x in range(start, end)]), liveoutput)
            # print(results)

        return results

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
    print(Pinger.ping_range(network="192.168.0.", start=1, end=81, liveoutput=True))
    # response = Pinger.ping("192.168.0.2")
    # if response:
    #     print(response)
