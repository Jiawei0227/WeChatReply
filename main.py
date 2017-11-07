# coding=utf8
import itchat
import sys
import requests
import json
import TuringAPIDataProcess

reload(sys)
sys.setdefaultencoding('utf-8')

turingApiUrl = 'http://www.tuling123.com/openapi/api'
itchat.wechatTable = {}
itchat.openTurning = u'芝麻开门'
itchat.closeTurning = u'芝麻关门'

def getMessageFromTuring(msg):
    inputData = {
        'key': '...', #Your own code
        'loc': '北京市中关村',
        'userid': '116985',
        'info': msg
    }
    rawData = json.dumps(inputData)
    r = requests.post(turingApiUrl,rawData)
    return r.json()

def processTuringJsonData(data):
    return TuringAPIDataProcess.codeMap[data['code']](data)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg['Text']
    FromUserName = msg['FromUserName']
    if itchat.wechatTable.has_key(FromUserName):
        if text == itchat.closeTurning:
            itchat.wechatTable[FromUserName]['isTurningOn'] = False
            return

        if text == itchat.openTurning:
            itchat.wechatTable[FromUserName]['isTurningOn'] = True
            return "欢迎光临~接下来的时间由我来回答你的问题哦~~~ 如果不想和我聊天就输入‘芝麻关门’~~~~我就会走哦~~"


        if itchat.wechatTable[FromUserName]['isTurningOn'] == True:
            resultJson = getMessageFromTuring(msg['Text'])
            text = processTuringJsonData(data=resultJson)
            return text

    else:
        itchat.wechatTable[FromUserName] = { 'isTurningOn': False }
        return text_reply(msg)





def main():
    itchat.auto_login()
    itchat.run()


if __name__ == '__main__':
    main()
