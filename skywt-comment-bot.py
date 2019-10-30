import requests
import random
import string
import time
import urllib


def gen(length: int):
    return ''.join(random.sample(string.digits + string.ascii_lowercase, length))


def gen_commnet(length: int):
    ret = ""
    for _ in range(length):
        ret += chr(random.randint(0x4e00, 0x9fbf))
    return ret


if __name__ == "__main__":
    while (1):
        author = gen(8)
        mail = gen(8) + '@' + gen(8) + ".com"
        comment = gen_commnet(16)
        data = {"author": gen(8), "email": mail,
                "wp-comment-cookies-consent": "yes", "comment": comment, "comment_post_ID": 2440, "comment_parent": 0, "akismet_comment_nonce": "37790fda0e", "ak_js": time.time_ns(), "action": "comment-submission"}
        ret_content = requests.post(
            url="https://skywt.cn/wp-admin/admin-ajax.php", data=data)
        print(ret_content.text)
