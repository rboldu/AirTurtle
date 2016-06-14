import rospy
import actionlib
import sys
import select
import string
import json
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import PoseWithCovarianceStamped
from navigation.msg import navigationAutonomusEnable

from KHUBRobotClient import KHUBRobotClient

''' time in seconds, for each possition message'''
_FREQUENCY=1


class messageKyanite():
	def __init__(self,event="position",datax="-1",datay="-1",triggered_at="-1"):
		self.event=event
		self.datax=datax
		self.datay=datay
		self.triggered_at=triggered_at

	def getevent(self):
		return self.event

	def getdatax(self):
		return self.datax

	def getdatay(self):
		return self.datay

	def getTriggered_at(self):
		return self.triggered_at

class kyanite_ComServer():

	def __init__(self):
		rospy.loginfo("Initializing Kynate Client")
		self.roboClient = KHUBRobotClient('S1', '10.21.115.215', 9090)
		self.roboClient.onInfo(self.on_info_response)
		self.roboClient.onOps(self.on_ops_response)
		
		self.nav_enable_pub= rospy.Publisher('/navigation/enableAutonomus', navigationAutonomusEnable)
		self.poseSubs = rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, self.UpdatePosition)
		self.possitionMessage=messageKyanite()


	def on_info_response(self,*args):
		aux=args[0]
		print aux["event"]
		#print('on_info_response', args)


	def on_ops_response(self,*args):
		aux=args[0]
		if aux["event"]=="pause_operation":
			msg=navigationAutonomusEnable()
			msg.Enable=False
			self.nav_enable_pub.publish(msg)
			print "stoping"
		print aux["event"]
		#print('on_ops_response', args)
    

	def updateKyanite(self):
		self.roboClient.sendInfo({'event': self.possitionMessage.getevent(),'data': 
			{'x': self.possitionMessage.getdatax(),'y': self.possitionMessage.getdatay()},
			'triggered_at': self.possitionMessage.getTriggered_at()})


	def UpdatePosition(self,data):
		msg=messageKyanite(event="position",datax=str(data.pose.pose.position.x),datay=str(data.pose.pose.position.y),triggered_at=str(rospy.Time()))
		self.possitionMessage=msg

       
	def run(self):

		while not rospy.is_shutdown():
			self.updateKyanite()
			self.roboClient.wait(_FREQUENCY)
			#rospy.sleep(_FREQUENCY)
        
if __name__ == '__main__':
    rospy.init_node('Comunication_Kyanite')
    kyanite = kyanite_ComServer()
    kyanite.run()
    
    

  
