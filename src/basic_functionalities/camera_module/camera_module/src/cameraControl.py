#! /usr/bin/env python
'''
@author: Roger Boldu
'''

import rospy
import actionlib
import sys
import select

from std_msgs.msg import UInt16

ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'

MAX_SPEED_TURN=0.5 #degrees per second
FREQ_MOVING=0.05
MAX_TURN=5 # every second
MAX_POSITION=175
MIN_POSITION=5
RESET_POSITION=90
'''
@this is a navigation state
@The main Idea is to follow the the line that is on the floor
@/cmd_velux/input/navi
'''

class moveCamera():
    def __init__(self):
       self.position=RESET_POSITION
       self.newPosition=RESET_POSITION
       self.camer_subs = rospy.Subscriber("/kyanite/camera/desiredPosition", UInt16, self.updateValue, queue_size=1)
       self.camera_pub= rospy.Publisher('/CameraPosition', UInt16,queue_size=0)


    def updateValue(self,data):
    	print "new value!!!!!!"
        self.newPosition=data.data
        if self.newPosition>MAX_POSITION :
        	self.newPosition=MAX_POSITION
        if self.newPosition<MIN_POSITION:
        	self.newPosition=MIN_POSITION
        #print "new possiiton is:  " + str(self.newPosition)
        msg=UInt16()
        while  (self.position!=self.newPosition):
        	if  (self.position<self.newPosition):
        		#it means we have to increase
        		if (self.newPosition>self.position+MAX_TURN):
        			msg.data=self.position+MAX_TURN
        			self.position=self.position+MAX_TURN
        		else:
        			msg.data=self.newPosition-self.position+self.position
        			self.position=self.newPosition
        	else:
        		#It means I need to decrease
        		if (self.newPosition<self.position-MAX_TURN):
        			msg.data=self.position-MAX_TURN
        			self.position=self.position-MAX_TURN
        		else:
        			msg.data=self.newPosition-self.position+self.position
        			self.position=self.newPosition
        	rospy.sleep(FREQ_MOVING)
        	#print "I am sending====== "+ str(msg.data)
        	self.camera_pub.publish(msg)
        print "done"


         
    def run(self):
        
        while not rospy.is_shutdown():
        	#if (self.position==self.newPosition):
        	#	print "loop"
                #msg=UInt16()
        		#msg.data=self.position
        		#self.camera_pub.publish(msg)

        	rospy.sleep(5)
        
if __name__ == '__main__':
    rospy.init_node('Following_Line_server')
    
    cameara_servo = moveCamera()
    cameara_servo.run()
    
    

  
