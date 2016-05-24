#! /usr/bin/env python
'''
@author: Roger Boldu
'''

import rospy
import actionlib
import sys
import select

from geometry_msgs.msg import Twist
from navigation.msg import sensor_raw_data

MAXMETERS=2 # this is the maximum numer of meters that can move the robot forward
MAXTIME=15 # numer maxim of time that the robot can be going forward
MINDIST=0.15
SPEED_X=0.1 # that is a forward speed
MAXIM_INIT=200 # it'a a initialitzation value, it have to be bigger than ultraSounds Range
NUM_MOSTRES=3

ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'

'''
@this is a navigation state
@The main Idea is to follow the the line that is on the floor
@/cmd_velux/input/navi
'''

class navigation_followLine():
    
    def __init__(self):
        rospy.loginfo("Initializing reverse")
        
        self.nav_pub= rospy.Publisher('/cmd_velux/input/navi', Twist)
	self.lineSensor_subs = rospy.Subscriber("navigation/sensor/line_possition", sensor_raw_data, self.print_line)
        self.average_possition=0

    def print_line(self,data):
        self.line_data=data
	if self.line_data.averagePosition >0 :
		self.pub_move()
	print self.line_data
        
            
    def pub_move(self):
        msg=Twist()
        msg.linear.x= 10
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=0
        self.nav_pub.publish(msg)
        
    def pub_stop(self):
        msg=Twist()
        msg.linear.x=0
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=0

        self.nav_pub.publish(msg)
       
    def run(self):
        while not rospy.is_shutdown():
            rospy.sleep(3)
        
if __name__ == '__main__':
    rospy.init_node('Following_Line_server')
    
    navigation = navigation_followLine()
    navigation.run()
    
    

  
