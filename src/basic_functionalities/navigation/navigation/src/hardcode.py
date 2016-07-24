#! /usr/bin/env python
'''
@author: Roger Boldu
'''

import rospy
import actionlib
import sys
import select

from math_utils import *
from geometry_msgs.msg import Twist
from navigation.msg import sensor_raw_data, navigationAutonomusEnable
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler, euler_from_quaternion

ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'

SPEED_X=0.25
MARGE=0.01

'''
@this is a navigation state
@The main Idea is to follow the the line that is on the floor
@/cmd_velux/input/navi
'''
class navigationoperations():
    def __init__(self):
        self.lineSensor_subs = rospy.Subscriber("/odom", Odometry, self.checkOdometry, queue_size=1)
        self.nav_pub= rospy.Publisher('/cmd_vel_mux/input/navi', Twist,queue_size=1)
        self.lineSensor_subs = rospy.Subscriber("navigation/enableAutonomus",navigationAutonomusEnable, self.enable)


        self.navigationEnable=False
        self.nav_in_process=False
        self.meters=0
        self.straigh=True
        self.instructionCounter=0
        self.parameters=rospy.get_param('navigation_kobuki')
    def checkOdometry(self,data):
        self.Odometry_now=data

    def proces_odometry_straight(self):
        position_navigate=Pose()
        position_navigate.position.x=self.Odometry_now.pose.pose.position.x-self.Odometry_init.pose.pose.position.x
        position_navigate.position.y=self.Odometry_now.pose.pose.position.y-self.Odometry_init.pose.pose.position.y
        
        unit_vector = normalize_vector(position_navigate.position)
        #print "unit vector: " + str(unit_vector)
        position_distance = vector_magnitude(position_navigate.position)
        #print "position_distance: " + str(position_distance)
        
        if (position_distance<self.meters) :
            self.pub_move()            

        else :
            self.pub_stop()
            self.nav_in_process=False

    def proces_odometry_turn(self):
        
        position_navigate=Pose()
        position_navigate.orientation.x=self.Odometry_now.pose.pose.orientation.x
        position_navigate.orientation.y=self.Odometry_now.pose.pose.orientation.y
        position_navigate.orientation.z=self.Odometry_now.pose.pose.orientation.z
        position_navigate.orientation.w=self.Odometry_now.pose.pose.orientation.w
        
        
        
        roll, pitch, yaw = euler_from_quaternion([position_navigate.orientation.x,position_navigate.orientation.y,
                                position_navigate.orientation.z,
                                position_navigate.orientation.w])
    
        if (yaw<self.radians+MARGE and yaw>self.radians-MARGE) :
           self.nav_in_process=False
           self.pub_stop()
        else :
            
            self.pub_twist()

    def enable(self,data):
        self.navigationEnable=data.Enable
        if self.navigationEnable==False:
            self.pub_stop()

    
    def newOrder(self,distance_meters):
        self.straigh=True
        if self.nav_in_process==False:
            self.nav_in_process=True
            self.Odometry_init=self.Odometry_now
            self.time_init= rospy.get_rostime()
            self.meters=distance_meters
            return True
        else:
            print "still busyyy!!"
            return False


    def newOrderTurn(self,degrees):

        if self.nav_in_process==False:
            self.nav_in_process=True
            self.Odometry_init=self.Odometry_now
            self.time_init= rospy.get_rostime()



            self.straigh=False
            self.radians=math.radians(degrees)
            self.req_degree=degrees

            roll, pitch, yaw = euler_from_quaternion([self.Odometry_init.pose.pose.orientation.x,self.Odometry_init.pose.pose.orientation.y,
                    self.Odometry_init.pose.pose.orientation.z,
                    self.Odometry_init.pose.pose.orientation.w])
            if self.req_degree>0 :
                self.speed=+SPEED_X
                self.yaw_final=yaw-self.radians
            else :
                self.yaw_final=yaw-self.radians
                self.speed=-SPEED_X
            
            self.radians=self.yaw_final
            if self.radians>math.pi :
                self.radians=-(math.pi-self.radians+math.pi)
            if self.radians<-math.pi :
                self.radians= math.pi-(abs(self.radians)-math.pi)
                
            if self.radians>(-math.pi) and self.radians<(math.pi) :
                rospy.loginfo("eps new order")
                
            return True
        else:
            print "still busyyy!!"
            return False

        
    def pub_move(self):
        msg=Twist()
        msg.linear.x= SPEED_X
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
    
    def pub_twist(self):

        msg=Twist()
        msg.linear.x= 0
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=-self.speed
        self.nav_pub.publish(msg)
        

    def turn90degreesLeft(self):

        msg=Twist()
        msg.linear.x= 0
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=MAX_SPEED_TURN

        return msg

    def handleRequest(self,action_input,value_input):
        
        if action=="forward":
        #self.newOrderTurn(90)
            self.newOrder(value)
        if action=="twist":
            self.newOrderTurn(value)

        while self.nav_in_process==True :
            if self.navigationEnable :
                    if self.nav_in_process==True:
                        if self.straigh==True:
                            self.proces_odometry_straight()
                        else:
                            self.proces_odometry_turn()
            else:
                rospy.sleep(0.03)
        return True
    def run(self):
        while not rospy.is_shutdown():
            if self.navigationEnable :
                if self.nav_in_process==True:
                    if self.straigh==True:
                        self.proces_odometry_straight()
                    else:
                        self.proces_odometry_turn()
                else:
                    
                    self.instructionCounter=self.instructionCounter+1
                    if self.instructionCounter>self.parameters['number'][0]:
                        self.instructionCounter=1
                        print "one loop done"
                    print " sending parameter:=== "+ str(self.parameters[str(self.instructionCounter)])
                    action=self.parameters[str(self.instructionCounter)][0]
                    value=self.parameters[str(self.instructionCounter)][1]
                    if action=="forward":
                    #self.newOrderTurn(90)
                        self.newOrder(value)
                        
                    if action=="twist":
                        self.newOrderTurn(value)

                    rospy.sleep(0.03)
            else:
                #print "not runing"
                rospy.sleep(0.4)
        
if __name__ == '__main__':
    rospy.init_node('Following_Line_server')
    
    navigation = navigationoperations()
    navigation.run()
    
    

  
