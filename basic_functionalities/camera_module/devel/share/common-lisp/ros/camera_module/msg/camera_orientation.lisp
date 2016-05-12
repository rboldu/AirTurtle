; Auto-generated. Do not edit!


(cl:in-package camera_module-msg)


;//! \htmlinclude camera_orientation.msg.html

(cl:defclass <camera_orientation> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:fixnum
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:fixnum
    :initform 0))
)

(cl:defclass camera_orientation (<camera_orientation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <camera_orientation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'camera_orientation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera_module-msg:<camera_orientation> is deprecated: use camera_module-msg:camera_orientation instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <camera_orientation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_module-msg:x-val is deprecated.  Use camera_module-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <camera_orientation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_module-msg:y-val is deprecated.  Use camera_module-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <camera_orientation>) ostream)
  "Serializes a message object of type '<camera_orientation>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <camera_orientation>) istream)
  "Deserializes a message object of type '<camera_orientation>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<camera_orientation>)))
  "Returns string type for a message object of type '<camera_orientation>"
  "camera_module/camera_orientation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'camera_orientation)))
  "Returns string type for a message object of type 'camera_orientation"
  "camera_module/camera_orientation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<camera_orientation>)))
  "Returns md5sum for a message object of type '<camera_orientation>"
  "727012f6868afa655d78dc8b436d2c91")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'camera_orientation)))
  "Returns md5sum for a message object of type 'camera_orientation"
  "727012f6868afa655d78dc8b436d2c91")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<camera_orientation>)))
  "Returns full string definition for message of type '<camera_orientation>"
  (cl:format cl:nil "uint8 x~%uint8 y~%#x base rotation~%#y camera inclination~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'camera_orientation)))
  "Returns full string definition for message of type 'camera_orientation"
  (cl:format cl:nil "uint8 x~%uint8 y~%#x base rotation~%#y camera inclination~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <camera_orientation>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <camera_orientation>))
  "Converts a ROS message object to a list"
  (cl:list 'camera_orientation
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
