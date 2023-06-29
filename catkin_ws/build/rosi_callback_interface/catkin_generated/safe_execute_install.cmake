execute_process(COMMAND "/workspaces/rosi_python_api/catkin_ws/build/rosi_callback_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/workspaces/rosi_python_api/catkin_ws/build/rosi_callback_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
