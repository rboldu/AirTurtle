#ifndef _ROS_navigation_sensor_raw_data_h
#define _ROS_navigation_sensor_raw_data_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace navigation
{

  class sensor_raw_data : public ros::Msg
  {
    public:
      uint8_t averagePosition;

    sensor_raw_data():
      averagePosition(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->averagePosition >> (8 * 0)) & 0xFF;
      offset += sizeof(this->averagePosition);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->averagePosition =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->averagePosition);
     return offset;
    }

    const char * getType(){ return "navigation/sensor_raw_data"; };
    const char * getMD5(){ return "f80e0dc5f527e8deac131616f6c00d42"; };

  };

}
#endif