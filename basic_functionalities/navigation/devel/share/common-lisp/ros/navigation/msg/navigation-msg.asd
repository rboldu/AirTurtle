
(cl:in-package :asdf)

(defsystem "navigation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "sensor_raw_data" :depends-on ("_package_sensor_raw_data"))
    (:file "_package_sensor_raw_data" :depends-on ("_package"))
  ))