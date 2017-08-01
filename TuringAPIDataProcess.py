# -*- coding: UTF-8 -*-


def getNormalText(data):
    return data['text']

def getListText(data):
    text = data['text'] + "\n"
    for article in data['list']:
        one = u'=> 标题：' + article["article"]+'\n' + u'来源：' + article["source"]+ '\n'+ u'详情：' + article["detailurl"]+ '\n'
        text = text + one.encode('utf-8')
    return text

def getUrlText(data):
    text = data['text'] +'\n' + data['url']
    return text

def getFoodRecipe(data):
    text = data['text'] + "\n"
    for article in data['list']:
        one = u'=> 图片：' + article["icon"]+'\n' + u'=> 名称：' + article["name"]+'\n' + u'信息：' + article["info"]+ '\n'+ u'详情：' + article["detailurl"]+ '\n'
        text = text + one.encode('utf-8')
    return text

codeMap = {
    100000 : getNormalText,
    200000 : getUrlText,
    302000 : getListText,
    308000 : getFoodRecipe
}
