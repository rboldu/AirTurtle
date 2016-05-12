
(cl:in-package :asdf)

(defsystem "camera_module-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "camera_orientation" :depends-on ("_package_camera_orientation"))
    (:file "_package_camera_orientation" :depends-on ("_package"))
  ))