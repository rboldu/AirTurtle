#ifndef _ROS_navigation_navigationAutonomusEnable_h
#define _ROS_navigation_navigationAutonomusEnable_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace navigation
{

  class navigationAutonomusEnable : public ros::Msg
  {
    public:
      bool Enable;

    navigationAutonomusEnable():
      Enable(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_Enable;
      u_Enable.real = this->Enable;
      *(outbuffer + offset + 0) = (u_Enable.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->Enable);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_Enable;
      u_Enable.base = 0;
      u_Enable.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->Enable = u_Enable.real;
      offset += sizeof(this->Enable);
     return offset;
    }

    const char * getType(){ return "navigation/navigationAutonomusEnable"; };
    const char * getMD5(){ return "132b53c6b897b73e7dc72146d30f3b1e"; };

  };

}
#endif