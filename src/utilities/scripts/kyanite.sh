#!/bin/bash

#setting up the enviroment
source /opt/ros/indigo/setup.bash
source /home/kyanite/AirTurtle/devel/setup.sh 
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=127.0.0.1

echo "------------------------"
echo "Turning off"
echo "------------------------"
#turnng of all the old thinkgs
sudo bash ~/AirTurtle/src/utilities/scripts/stopkyaniteCamera.sh
bash ~/AirTurtle/src/utilities/scripts/kyaniteStop.sh
sleep 1
echo "------------------------"
echo "All the systems are off"
echo "------------------------"

echo "------------------------"
echo "Turning on the camera"
echo "------------------------"
sudo bash ~/AirTurtle/src/utilities/scripts/kyaniteCamera.sh

echo "------------------------"
echo "Launching the kyanite services"
echo "------------------------"
bash ~/AirTurtle/src/utilities/scripts/kyaniteservices.sh &


sleep 10
echo "------------------------"
echo "Inializing connection with the server"
echo "------------------------"
bash ~/AirTurtle/src/utilities/scripts/kyaniteclient.sh &

sleep 1
echo "------------------------"
echo "All the services Runing!!"
echo "------------------------"

rostopic pub /mobile_base/commands/sound kobuki_msgs/Sound "value: 1 "

