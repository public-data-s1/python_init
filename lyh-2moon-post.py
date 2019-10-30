import requests

if __name__ == "__main__":
    while (1):
        requests.post(
            url="http://10.196.1.207/2moons/index.php?page=login", data={"uni": "1",
                                                                         "username": "test",
                                                                         "password": "test"}, allow_redirects=False)
