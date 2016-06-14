cmake_minimum_required(VERSION 2.8.3)
project(navigation)
find_package(catkin REQUIRED COMPONENTS std_msgs actionlib_msgs message_generation)

add_message_files(DIRECTORY msg
                      FILES sensor_raw_data.msg
                      navigationAutonomusEnable.msg
                 )


generate_messages(DEPENDENCIES std_msgs actionlib_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs actionlib_msgs)
