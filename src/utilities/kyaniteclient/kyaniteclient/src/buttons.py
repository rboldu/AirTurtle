#! /usr/bin/env python
'''
@author: Roger Boldu
'''

# this software runs all the scripts of hardcode moving.
#it allows to move fordware and twist.


import rospy
import actionlib
import sys
import select
from kobuki_msgs.msg import ButtonEvent
from navigation.msg import navigationAutonomusEnable

ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'


'''
@this is a navigation state
@The main Idea is to follow the the line that is on the floor
@/cmd_velux/input/navi
'''
class buttonReceiver():
    def __init__(self):
        self.lineSensor_subs = rospy.Subscriber("/mobile_base/events/button", ButtonEvent,self.buttonThread, queue_size=1)
        self.navEnable = rospy.Publisher("navigation/enableAutonomus",navigationAutonomusEnable, queue_size=1)

    def buttonThread(self,data):
        self.buttonStatus=data
        if self.buttonStatus.state==1 and self.buttonStatus.button==1:
            print "button 1"
            msg=navigationAutonomusEnable()
            msg.Enable=False
            self.navEnable.publish(msg)
        if self.buttonStatus.state==1 and self.buttonStatus.button==2:
            print "button 2"
            msg=navigationAutonomusEnable()
            msg.Enable=True
            self.navEnable.publish(msg)


    def run(self):
        while not rospy.is_shutdown():
            rospy.sleep(1)
        
if __name__ == '__main__':
    rospy.init_node('button_controller')
    
    but = buttonReceiver()
    but.run()
    
    

  
