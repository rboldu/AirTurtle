#!/bin/bash
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=10.21.115.154

sleep 1
roscore &
sleep 2
roslaunch turtlebot_bringup minimal.launch &
sleep 4
roslaunch ~/AirTurtle/src/basic_functionalities/serial/launch/serial_peripherics.launch &
sleep 3
roslaunch ~/AirTurtle/src/basic_functionalities/camera_module/camera_module/launch/camera_module.launch &
sleep 1
roslaunch ~/AirTurtle/src/basic_functionalities/navigation/navigation/launch/navigation.launch &
sleep 1

