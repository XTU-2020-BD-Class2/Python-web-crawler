import itchat


def send_image(image_path):
    itchat.send_image(image_path, toUserName="filehelper")

def vx(cmd, func):
    # 1. 登录微信
    itchat.auto_login()


    # 2. 监听微信收到消息（文本）
    @itchat.msg_register(itchat.content.TEXT)
    def itlike(msg):
        print(msg)
        if msg["ToUserName"] == "filehelper":
            if msg["Content"] == cmd:
                # print("收到了文件传输助手接收的消息itlike")
                #
                func()

    itchat.run()