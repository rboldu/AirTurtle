#!/bin/bash
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=127.0.0.1

rosnode kill /serial_navigation_sensor
rosnode kill /serial_node_camera
rosnode kill /cameracontrol
rosnode kill /navigationfollowline
rosnode kill /app_manager
rosnode kill /bumper2pointcloud
rosnode kill /capability_server
rosnode kill /capability_server_nodelet_manager
rosnode kill /cmd_vel_mux
rosnode kill /diagnostic_aggregator
rosnode kill /interactions
rosnode kill /master
rosnode kill /mobile_base
rosnode kill /mobile_base_nodelet_manager
rosnode kill /robot_state_publisher
rosnode kill /rosout
rosnode kill /turtlebot_laptop_battery
rosnode kill /zeroconf/zeroconf
rosnode kill /ButtonsService
rosnode kill /rosout




killall -9 rosmaster
killall -9 roscore
exit

