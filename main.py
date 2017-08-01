# coding=utf8
import itchat
import sys
import requests
import json

reload(sys)
sys.setdefaultencoding('utf-8')

turingApiUrl = 'http://www.tuling123.com/openapi/api'
itchat.wechatTable = {}
itchat.openTurning = u'芝麻开门'
itchat.closeTurning = u'芝麻关门'

def getMessageFromTuring(msg):
    inputData = {
        'key': 'eae8cb9baae94693b49b6cad3ce88a1d',
        'loc': '北京市中关村',
        'userid': '116985',
        'info': msg
    }
    rawData = json.dumps(inputData)
    r = requests.post(turingApiUrl,rawData)
    return r.json()["text"]

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print msg
    text = msg['Text']
    FromUserName = msg['FromUserName']
    if itchat.wechatTable.has_key(FromUserName):
        if text == itchat.closeTurning:
            itchat.wechatTable[FromUserName]['isTurningOn'] = False
            return

        if (text == itchat.openTurning):
            itchat.wechatTable[FromUserName]['isTurningOn'] = True
            return "欢迎光临~接下来的时间由我来回答你的问题哦~~~ 如果不想和我聊天就输入‘芝麻关门’~~~~我就会走哦~~"


        if itchat.wechatTable[FromUserName]['isTurningOn'] == True:
            return getMessageFromTuring(msg['Text'])

    else:
        itchat.wechatTable[FromUserName] = { 'isTurningOn': False }
        text_reply(msg)
        return




def main():
    itchat.auto_login()
    itchat.run()
     #msg = raw_input()
     #getMessageFromTuring(msg)

if __name__ == '__main__':
    main()