# -*- coding: utf-8 -*-
"""
Modified on Tue May 13 2021

https://blog.csdn.net/brucewong0516/article/details/84031715
"""

# encoding: UTF-8
from threading import *
# sys.path.append('D:\\works\\TestFile')
# print(sys.path)

# Event name:  New article
EVENT_ARTICLE = "Event_Article"


# Event Source: public account
class PublicAccounts:
    def __init__(self, eventManager):
        self.__eventManager = eventManager

    def WriteNewArticle(self):
        # event object, writing a new article
        event = Event(type_=EVENT_ARTICLE)
        event.dict["article"] = u'How to write clean code\n'

        # event of sending
        self.__eventManager.SendEvent(event)
        print(u'Publish Acct sent an new article\n')


# Listener: Subscriber
class Listener:
    def __init__(self, username):
        self.__username = username

    # Event handler of listener:  reading article
    def ReadArticle(self, event):
        print(u'%s Received' % self.__username)
        print(u'Reading new article：%s' % event.dict["article"])


"""test function"""


# --------------------------------------------------------------------
def test():
    # create listener instances
    listener1 = Listener("Peter")  # 订阅者1
    listener2 = Listener("Steve")  # 订阅者2

    # instantiate Event Manager
    eventManager = EventManager()

    # binding event and listener's handler function (reading article)
    eventManager.AddEventListener(EVENT_ARTICLE, listener1.ReadArticle)
    eventManager.AddEventListener(EVENT_ARTICLE, listener2.ReadArticle)
    # start an event manager thread
    eventManager.Start()

    publicAcc = PublicAccounts(eventManager)
    timer = Timer(2, publicAcc.WriteNewArticle)
    timer.start()


if __name__ == '__main__':
    test()
