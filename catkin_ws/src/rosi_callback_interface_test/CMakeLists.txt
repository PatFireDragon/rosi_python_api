cmake_minimum_required(VERSION 3.0.2)
project(rosi_callback_interface_test)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    rosi_callback_interface
    cv_bridge
)

catkin_package(
    CATKIN_DEPENDS 
    rospy
    std_msgs
    rosi_callback_interface
    cv_bridge
)

catkin_install_python(PROGRAMS
  scripts/test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
