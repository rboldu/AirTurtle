#!/bin/bash
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=10.21.115.154

rosnode kill /serial_navigation_sensor
rosnode kill /serial_node_camera
rosnode kill /cameracontrol
rosnode kill /navigationfollowline
killall -9 rosmaster
killall -9 roscore
exit

