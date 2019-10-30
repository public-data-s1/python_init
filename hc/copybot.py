import hackchat


def message_got(chat, message, sender):
    chat.send_message("{}".format(message))


roomid = input("room_id: ")
chat = hackchat.HackChat("CopyBot", roomid)
chat.on_message += [message_got]
chat.run()
