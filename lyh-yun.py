import requests
import random
import string
import time
import hashlib


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
        # url = "http://test.yuhang.cf/yun/includes/userAction.php"
        url = "http://10.196.1.14/sd/includes/userAction.php"
        data = {"action": "register",
                "username-reg": email,
                "password-reg": password,
                "password-check": password}
        result = requests.post(url=url, data=data)
        print(result.status_code)
