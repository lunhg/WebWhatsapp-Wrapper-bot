# -*- coding: utf-8 -*-

from webwhatsapi import WhatsAPIDriver
import os
import string
import sys

# Abstract class to implement WebWhtasapp-Wrapper bots
# Author : Luis Fagundes
# Co-author: Guilherme Lunhani
class Bot(object):

  def __init__(self, **kwargs):
    self.attributes = []
    self.properties = {}
    self.botclass = kwargs.get('botclass')
    b = kwargs.get('botname')
    c = kwargs.get('client')
    cwd = os.path.join(os.getcwd(), '_cache')
    p = os.path.abspath(cwd)
    h = kwargs.get('headless')
    self.driver = WhatsAPIDriver(client=c,
                                 username=u,
                                 profile=p,
                                 headless=h)
    

  def setup(self, **kwargs):
    for p in self.attributes:
      self.getattribute(p).setup()

  def run(self, **kwargs):
    while True:
      time.sleep(kwargs.frameTime)
      for message_group in self.driver.get_unread():
        for message in message_group.messages:
          for fn in kwargs.get('callbacks'):
            fn(message_group.chat, message)

  def plugin(self, **kwargs):
    try:
      name = kwargs.name.split("/").join(".")
      print "===> plugin %s" % name 
      sys.path.append("%s" % kwargs.path)
      module = __import__("plugins.%s" % name)
      __className__  = name.split(".")
      __className__ = __className__[len(__className__)-1]
      __class__ = getattr(module, __className__)
      instance = __class__(driver=self.driver)
      self.attributes.push(name)
      self.setattr(name_, instance)
      print str(self.getattribute(name))
    except Exception, e:
      print e

  def getattribute(self, key):
    if key in self.attributes:
      return self.properties[key]
    else:
      raise Exception("no %s attribute found")

  def setattr(self, key, val):
    if key in self.attributes:
      self.properties[key] = val    
    else:
      raise Exception("no %s attribute defined")
