import rospy
import actionlib
import sys
import select
import string
import json
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import PoseWithCovarianceStamped
from navigation.msg import navigationAutonomusEnable

from std_msgs.msg import UInt16

from KHUBRobotClient import KHUBRobotClient

''' time in seconds, for each possition message'''
_FREQUENCY=1


NAME_ROBOT='B'

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
		self.roboClient = KHUBRobotClient('S1', '10.21.115.114', 9099)
		self.roboClient.onInfo(self.on_info_response)
		self.roboClient.onOps(self.on_ops_response)
		
		self.nav_enable_pub= rospy.Publisher('/navigation/enableAutonomus', navigationAutonomusEnable,queue_size=1)
		self.cameraPosition_pub=rospy.Publisher('/kyanite/camera/desiredPosition',UInt16,queue_size=1)
		self.poseSubs = rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, self.UpdatePosition,queue_size=1)
		self.CamposeSubs = rospy.Subscriber("/CameraPosition", UInt16, self.UpdateCameraPosition,queue_size=1)

		self.possitionMessage=messageKyanite()
		self.camerapossitionMessage=messageKyanite()


	def on_info_response(self,*args):
		aux=args[0]
		print aux["event"]
		#print('on_info_response', args)


	def on_ops_response(self,*args):
		aux=args[0]
		#print aux["event"]
		if aux["event"]=="pause_operation":
			msg=navigationAutonomusEnable()
			msg.Enable=False
			self.nav_enable_pub.publish(msg)
			print "stoping"
		if aux["event"]=="resume_operation":
			msg=navigationAutonomusEnable()
			msg.Enable=True
			self.nav_enable_pub.publish(msg)
			print "starting"

		if aux["event"]=="camera_rotate":
			msg=UInt16()
			print(str(aux["data"]['x']))
			print str(aux)
			msg.data=int(aux["data"]['x'])
			#print "camera should go here "+str(msg.data)
			self.cameraPosition_pub.publish(msg)
			print "camera"
		#print('on_ops_response', args)
    

	def updateKyanite(self):
		self.roboClient.sendInfo({'event': self.possitionMessage.getevent(),'data': 
			{'x': self.possitionMessage.getdatax(),'y': self.possitionMessage.getdatay(),'name':NAME_ROBOT},
			'triggered_at': self.possitionMessage.getTriggered_at()})

		self.roboClient.sendInfo({'event': self.camerapossitionMessage.getevent(),'data': 
			{'x': self.camerapossitionMessage.getdatax(),'y': self.camerapossitionMessage.getdatay(),'name':NAME_ROBOT},
			'triggered_at': self.camerapossitionMessage.getTriggered_at()})


	def UpdatePosition(self,data):
		msg=messageKyanite(event="position",datax=str(data.pose.pose.position.x),datay=str(data.pose.pose.position.y),triggered_at=str(rospy.Time()))
		self.possitionMessage=msg
	def UpdateCameraPosition(self,data):
		msg=messageKyanite(event="camera_position",datax=str(data.data),datay=str(0),triggered_at=str(rospy.Time()))
		self.camerapossitionMessage=msg
       
	def run(self):

		while not rospy.is_shutdown():
			self.updateKyanite()
			self.roboClient.wait(_FREQUENCY)
			#rospy.sleep(_FREQUENCY)
        
if __name__ == '__main__':
    rospy.init_node('Comunication_Kyanite')
    kyanite = kyanite_ComServer()
    kyanite.run()
    
    

  
