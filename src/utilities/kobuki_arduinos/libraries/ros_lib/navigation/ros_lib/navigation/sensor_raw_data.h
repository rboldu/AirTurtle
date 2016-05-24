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
      int8_t averagePosition;

    sensor_raw_data():
      averagePosition(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_averagePosition;
      u_averagePosition.real = this->averagePosition;
      *(outbuffer + offset + 0) = (u_averagePosition.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->averagePosition);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int8_t real;
        uint8_t base;
      } u_averagePosition;
      u_averagePosition.base = 0;
      u_averagePosition.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->averagePosition = u_averagePosition.real;
      offset += sizeof(this->averagePosition);
     return offset;
    }

    const char * getType(){ return "navigation/sensor_raw_data"; };
    const char * getMD5(){ return "d206a64c7d7498ae43986f17623d9c0b"; };

  };

}
#endif