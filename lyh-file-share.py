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


def rand(length: int):
    return ''.join(random.sample(string.digits + string.ascii_lowercase, length))


if __name__ == "__main__":
    random.seed(time.time_ns())
    file_data = gen(1048576)
    cnt = 0
    while (1):
        file_name = "o_" + rand(32) + ".png"
        data = {"name": file_name, "key": file_name,
                "token": "nothing"}
        files = {"img": (file_name, file_data, "image/png")}
        result = requests.post(
            url="http://10.196.1.14/sd/includes/fileReceive.php", data=data, files=files)
        print(result.status_code)
        cnt += 1
        print(cnt)
