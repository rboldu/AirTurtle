#!/bin/bash
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=10.21.115.154

sleep 1

roslaunch kyaniteclient kyaniteclient.launch

