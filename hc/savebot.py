import hackchat

msg_list = []


def message_got(chat, message: str, sender: str):
    global msg_list
    if message != "show-msg":
        msg_element = "sender: " + sender + "\nmessage: \n" + message + "\n"
        msg_list += [msg_element]
    if "show-msg" in message.lower():
        for i in msg_list:
            chat.send_message(i)


roomid = input("room_id: ")
chat = hackchat.HackChat("SaveBot", roomid)
chat.on_message += [message_got]
chat.run()
