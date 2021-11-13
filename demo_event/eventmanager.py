# -*- coding: utf-8 -*-
"""
Modified on Tue May 13 2021

https://blog.csdn.net/brucewong0516/article/details/84031715
"""
# sys modules
from queue import Queue, Empty
from threading import *


########################################################################
class EventManager:
    # ----------------------------------------------------------------------
    def __init__(self):
        """init event manager"""
        # event object queue
        self.__eventQueue = Queue()
        # switch of event manager
        self.__active = False
        # event handler thread
        self.__thread = Thread(target=self.__Run)
        self.count = 0
        # where this __handlers is a dict for saving event response functions for the corresponding event
        # each value of a key is a list, which stores event response functions for the event
        # one to many relationship
        self.__handlers = {}

    # ----------------------------------------------------------------------
    def __Run(self):
        """Run engine"""
        print('{}_run'.format(self.count))
        while self.__active == True:
            try:
                # set the timeout duration for event block
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__EventProcess(event)
            except Empty:
                pass
            self.count += 1

    # ----------------------------------------------------------------------
    def __EventProcess(self, event):
        """Processing event"""
        print('{}_EventProcess'.format(self.count))
        # to check if event response function does exit
        if event.type_ in self.__handlers:
            # if existing, then passing event object to each handler to execute
            for handler in self.__handlers[event.type_]:
                handler(event)
        self.count += 1

    # ----------------------------------------------------------------------
    def Start(self):
        """start"""
        print('{}_Start'.format(self.count))
        # set event manager to active state
        self.__active = True
        # start event handling thread
        self.__thread.start()
        self.count += 1

    # ----------------------------------------------------------------------
    def Stop(self):
        """stop"""
        print('{}_Stop'.format(self.count))
        # set event manager to inactive state
        self.__active = False
        # wait for event handler to exit
        self.__thread.join()
        self.count += 1

    # ----------------------------------------------------------------------
    def AddEventListener(self, type_, handler):
        """binding event object and listener's event handler"""
        print('{}_AddEventListener'.format(self.count))
        # try to acquire the function list of event handler,
        # create if there is not any list of event handler
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []
            self.__handlers[type_] = handlerList
        # if a handler does not stay at the event handler list
        # then register it
        if handler not in handlerList:
            handlerList.append(handler)
        print(self.__handlers)
        self.count += 1

    # ----------------------------------------------------------------------
    def RemoveEventListener(self, type_, handler):
        """remove listener's event handler"""
        print('{}_RemoveEventListener'.format(self.count))
        try:
            handlerList = self.handlers[type_]
            # if the handler function does exist in the list,
            # then remove it from the list
            if handler in handlerList:
                handlerList.remove(handler)
            # if the list gets empty,
            # then remove this event type from this engine
            if not handlerList:
                del self.handlers[type_]
        except KeyError:
            pass
        self.count += 1

    # ----------------------------------------------------------------------
    def SendEvent(self, event):
        """sending event，write event object to event queue"""
        print('{}_SendEvent'.format(self.count))
        self.__eventQueue.put(event)
        self.count += 1


########################################################################
"""event object"""


class Event:
    def __init__(self, type_=None):
        self.type_ = type_  # event type
        self.dict = {}  # dictionary is used for saving event data
