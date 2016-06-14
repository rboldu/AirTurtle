#! /usr/bin/env python
'''
@author: Roger Boldu
'''

import rospy
import actionlib
import sys
import select

from geometry_msgs.msg import Twist
from navigation.msg import sensor_raw_data, navigationAutonomusEnable


MAXMETERS=2 # this is the maximum numer of meters that can move the robot forward
MAXTIME=15 # numer maxim of time that the robot can be going forward
MINDIST=0.15
SPEED_X=0.1 # that is a forward speed
MAXIM_INIT=200 # it'a a initialitzation value, it have to be bigger than ultraSounds Range
NUM_MOSTRES=3

ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'

MAX_SPEED=0.05
DESIRED_VALUE_SENSOR=0
SPEED_DEPENDENCE=0.3

'''
@this is a navigation state
@The main Idea is to follow the the line that is on the floor
@/cmd_velux/input/navi
'''
class pid():
    def __init__(self,Kp=1,Ki=2,Kd=3,iteration_time=0.5):
        self.error=0
        self.error_prior=0
        self.integral=0
        self.Kp=Kp
        self.Ki=Ki
        self.Kd=Kd
        self.iteration_time=iteration_time
        self.derivative=0

    def calculateOutput(self,linePosition):
     
        error=DESIRED_VALUE_SENSOR-linePosition
        self.intergal=self.integral+(error*self.iteration_time)
        self.derivative=(error - self.error_prior)/self.iteration_time
        output=self.Kp*error+self.Ki*self.integral+self.Kd*self.derivative
        self.error_prior=error

        msg=Twist()
        speed=MAX_SPEED-abs(output)*SPEED_DEPENDENCE
        if speed <0 :
            speed=0
        msg.linear.x= speed
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=output

        return msg
        



class lineSensorFollow():

    def __init__(self):
        self.average=0
        self.time=0
        self.lineSensor_subs = rospy.Subscriber("navigation/sensor/line_possition", sensor_raw_data, self.updateValue, queue_size=1)

    def print_line(self):
        print self.average

    def updateValue(self,data):
        self.average=data.averagePosition
        self.time=rospy.get_rostime()
        #self.print_line()

    def gedAverage(self):
        return self.Sensor.average


class navigation_followLine():
    
    def __init__(self):
        rospy.loginfo("Initializing line follower")
        self.nav_pub= rospy.Publisher('/cmd_vel_mux/input/navi', Twist)
        self.lineSensor_subs = rospy.Subscriber("navigation/enableAutonomus",navigationAutonomusEnable, self.enable)
        self.followingLineActive=False

    def enable(self,data):
        if data.Enable==False and self.followingLineActive == False:
            self.pub_stop()
        self.followingLineActive=data.Enable



    def pub_move(self):
        msg=Twist()
        msg.linear.x= 0.5
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
        msg.angular.z=0.0

        self.nav_pub.publish(msg)
       
    def run(self):
        line=lineSensorFollow()
        pidFollow=pid(Kp=0.0009,Ki=0.0005,Kd=0.0005,iteration_time=3)
        while not rospy.is_shutdown():
            if self.followingLineActive :
                msg=pidFollow.calculateOutput(line.average)
                self.nav_pub.publish(msg)
            else:
                #print "not runing"
                rospy.sleep(0.3)


            rospy.sleep(0.3)
        
if __name__ == '__main__':
    rospy.init_node('Following_Line_server')
    
    navigation = navigation_followLine()
    navigation.run()
    
    

  
