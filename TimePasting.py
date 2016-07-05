# -*- coding: utf-8 -*-

import sys
import os
import Foundation
import objc
import AppKit
from datetime import date, time, datetime, timedelta

reload(sys)
sys.setdefaultencoding('utf-8')

def notify(self, title, subtitle, text, url):
    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(str(title))
    notification.setSubtitle_(str(subtitle))
    notification.setInformativeText_(str(text))
    notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setHasActionButton_(True)
    notification.setOtherButtonTitle_("View")
    notification.setUserInfo_({"action":"open_url", "value":url})
    NSUserNotificationCenter.defaultUserNotificationCenter().setDelegate_(self)
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def runTask(func, day=0, hour=0, min=0, second=0):
  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print "now:",strnow
  # First next run time
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
  next_time = now + period
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  print "next run:",strnext_time
  while True:
      # Get system current time
      iter_now = datetime.now()
      iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
      if str(iter_now_time) == str(strnext_time):
          # Get every start work time
          print "start work: %s" % iter_now_time
          # Call task func
          func(iter_now_time)
          print "task done."
          # Get next iteration time
          iter_time = iter_now + period
          strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
          print "next_iter: %s" % strnext_time
          # Continue next iteration
          continue

def start(str):
	notify('self',title="时间流逝中",subtitle='',text=str,url='')

start('now start')
runTask(start, day=0, hour=0, min=0,second=1)

