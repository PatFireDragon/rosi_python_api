cmake_minimum_required(VERSION 3.0.2)
project(rosi_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  rosi_defy
  std_msgs
  sensor_msgs
  geometry_msgs
  cv_bridge
)

catkin_package(
    CATKIN_DEPENDS 
    rospy
    rosi_defy
    std_msgs
    sensor_msgs
    geometry_msgs
    cv_bridge
)

catkin_python_setup()

catkin_package()