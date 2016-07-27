#!/bin/bash
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=127.0.0.1

sleep 1

roslaunch kyaniteclient kyaniteclient.launch

