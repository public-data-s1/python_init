import hackchat


def message_got(chat, message: str, sender):
    if "hello" in message.lower():
        chat.send_message("Hello, @{}! ".format(sender))
    elif "nihao" in message.lower():
        chat.send_message("The same to you, @{}! ".format(sender))


roomid = input("room_id: ")
chat = hackchat.HackChat("HelloBot", roomid)
chat.on_message += [message_got]
chat.run()
