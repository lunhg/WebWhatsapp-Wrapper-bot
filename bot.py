
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
    # See for selenium first
    try:
      os.environ["SELENIUM"]
    except KeyError:
      print "Please set the environment variable SELENIUM to Selenium URL"
      sys.exit(1)

    self.attributes = []
    self.properties = {}
    b = kwargs.get('botname')
    c = kwargs.get('client')
    cwd = os.path.join(os.getcwd(), '_cache')
    p = os.path.abspath(cwd)
    h = kwargs.get('headless')
    self.driver = WhatsAPIDriver(client=c,
                                 username=b,
                                 profile=p,
                                 headless=h)

  def setup(self, **kwargs):
    for p in kwargs.get('config'):
      self.getattribute(p).setup(p)
      
  def run(self, **kwargs):
    while True:
      time.sleep(kwargs.get('frameTime'))
      for message_group in self.driver.get_unread():
        for message in message_group.messages:
          for fn in kwargs.get('callbacks'):
            fn(message_group.chat, message)

  def plugin(self, **kwargs):
    try:
      name = kwargs.name.split("/").join(".")
      name = name[len(name) - 1]
      sys.path.append(kwargs.path)
      module = __import__(name)
      __class__ = getattr(module, name.title())
      instance = __class__(driver=self.driver)
      self.attributes.push(name)
      self.setattr(name, instance)
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
