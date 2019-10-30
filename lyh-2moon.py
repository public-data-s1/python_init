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
        url = "http://10.196.1.207/2moons/index.php?page=register"
        # url = "http://test.yuhang.cf/2moons/index.php?page=register"
        data = {"mode": "send",
                "externalAuth[account]": 0,
                "externalAuth[method]": "",
                "referralID": 0,
                "uni": 1,
                "username": username,
                "password": password,
                "passwordReplay": password,
                "email": email,
                "emailReplay": email,
                "lang": "cn",
                "rules": 1}
        result = requests.post(url=url, data=data)
        print(result.text)
