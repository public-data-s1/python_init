# -*- coding: utf-8 -*-
import hclib


def admin(method, username, channel="xjoi"):
    mod = hclib.HackChat(admin, "MinecraftFuns", channel,
                         "mcfuns,mcworld", "ws://127.0.0.1:6060/chat-ws", True)
    if method == "ban":
        mod.ban("username")


if __name__ == "__main__":
    while(1):
        method = str(input())
        username = input()
        admin(method, username)
