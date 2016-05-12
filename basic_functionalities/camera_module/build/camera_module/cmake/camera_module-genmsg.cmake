# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "camera_module: 1 messages, 0 services")

set(MSG_I_FLAGS "-Icamera_module:/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/indigo/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(camera_module_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg" NAME_WE)
add_custom_target(_camera_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "camera_module" "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(camera_module
  "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_module
)

### Generating Services

### Generating Module File
_generate_module_cpp(camera_module
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_module
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(camera_module_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(camera_module_generate_messages camera_module_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg" NAME_WE)
add_dependencies(camera_module_generate_messages_cpp _camera_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_module_gencpp)
add_dependencies(camera_module_gencpp camera_module_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_module_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(camera_module
  "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_module
)

### Generating Services

### Generating Module File
_generate_module_lisp(camera_module
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_module
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(camera_module_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(camera_module_generate_messages camera_module_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg" NAME_WE)
add_dependencies(camera_module_generate_messages_lisp _camera_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_module_genlisp)
add_dependencies(camera_module_genlisp camera_module_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_module_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(camera_module
  "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_module
)

### Generating Services

### Generating Module File
_generate_module_py(camera_module
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_module
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(camera_module_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(camera_module_generate_messages camera_module_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ahlab/AirTurtle/basic_functionalities/camera_module/src/camera_module/msg/camera_orientation.msg" NAME_WE)
add_dependencies(camera_module_generate_messages_py _camera_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_module_genpy)
add_dependencies(camera_module_genpy camera_module_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_module_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_module
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(camera_module_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(camera_module_generate_messages_cpp actionlib_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_module
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(camera_module_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(camera_module_generate_messages_lisp actionlib_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_module)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_module\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_module
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(camera_module_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(camera_module_generate_messages_py actionlib_msgs_generate_messages_py)
