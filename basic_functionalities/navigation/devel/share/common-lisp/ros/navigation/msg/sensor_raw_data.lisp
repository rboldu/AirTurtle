; Auto-generated. Do not edit!


(cl:in-package navigation-msg)


;//! \htmlinclude sensor_raw_data.msg.html

(cl:defclass <sensor_raw_data> (roslisp-msg-protocol:ros-message)
  ((averagePosition
    :reader averagePosition
    :initarg :averagePosition
    :type cl:fixnum
    :initform 0))
)

(cl:defclass sensor_raw_data (<sensor_raw_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sensor_raw_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sensor_raw_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name navigation-msg:<sensor_raw_data> is deprecated: use navigation-msg:sensor_raw_data instead.")))

(cl:ensure-generic-function 'averagePosition-val :lambda-list '(m))
(cl:defmethod averagePosition-val ((m <sensor_raw_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader navigation-msg:averagePosition-val is deprecated.  Use navigation-msg:averagePosition instead.")
  (averagePosition m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sensor_raw_data>) ostream)
  "Serializes a message object of type '<sensor_raw_data>"
  (cl:let* ((signed (cl:slot-value msg 'averagePosition)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sensor_raw_data>) istream)
  "Deserializes a message object of type '<sensor_raw_data>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'averagePosition) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sensor_raw_data>)))
  "Returns string type for a message object of type '<sensor_raw_data>"
  "navigation/sensor_raw_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sensor_raw_data)))
  "Returns string type for a message object of type 'sensor_raw_data"
  "navigation/sensor_raw_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sensor_raw_data>)))
  "Returns md5sum for a message object of type '<sensor_raw_data>"
  "d206a64c7d7498ae43986f17623d9c0b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sensor_raw_data)))
  "Returns md5sum for a message object of type 'sensor_raw_data"
  "d206a64c7d7498ae43986f17623d9c0b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sensor_raw_data>)))
  "Returns full string definition for message of type '<sensor_raw_data>"
  (cl:format cl:nil "int8 averagePosition~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sensor_raw_data)))
  "Returns full string definition for message of type 'sensor_raw_data"
  (cl:format cl:nil "int8 averagePosition~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sensor_raw_data>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sensor_raw_data>))
  "Converts a ROS message object to a list"
  (cl:list 'sensor_raw_data
    (cl:cons ':averagePosition (averagePosition msg))
))
