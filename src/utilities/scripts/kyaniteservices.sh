#!/bin/bash
#source /opt/ros/indigo/setup.bash
#source /home/kyanite/AirTurtle/devel/setup.sh 
#export ROS_MASTER_URI=http://localhost:11311
#export ROS_IP=127.0.0.1
#sleep 1
roscore &
sleep 2
roslaunch turtlebot_bringup minimal.launch & # starts the turtle boot
sleep 2
roslaunch ~/AirTurtle/src/basic_functionalities/serial/launch/serial_peripherics.launch & # launch the serlial interface ACO0 and AM1
#sleep 3
roslaunch ~/AirTurtle/src/basic_functionalities/camera_module/camera_module/launch/camera_module.launch & # script that makes the moving of the camera softer
#sleep 1
roslaunch ~/AirTurtle/src/basic_functionalities/navigation/navigation/launch/navigation.launch & # it launch the navigation
#sleep 1
roslaunch kyaniteclient turtleboot_services.launch & 
#sleep 1
