#ifndef _ROS_camera_module_camera_orientation_h
#define _ROS_camera_module_camera_orientation_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace camera_module
{

  class camera_orientation : public ros::Msg
  {
    public:
      uint8_t x;
      uint8_t y;

    camera_orientation():
      x(0),
      y(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->x >> (8 * 0)) & 0xFF;
      offset += sizeof(this->x);
      *(outbuffer + offset + 0) = (this->y >> (8 * 0)) & 0xFF;
      offset += sizeof(this->y);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->x =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->x);
      this->y =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->y);
     return offset;
    }

    const char * getType(){ return "camera_module/camera_orientation"; };
    const char * getMD5(){ return "727012f6868afa655d78dc8b436d2c91"; };

  };

}
#endif