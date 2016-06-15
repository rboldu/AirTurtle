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
      int8_t rawData;
      int8_t Density;

    sensor_raw_data():
      averagePosition(0),
      rawData(0),
      Density(0)
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
      union {
        int8_t real;
        uint8_t base;
      } u_rawData;
      u_rawData.real = this->rawData;
      *(outbuffer + offset + 0) = (u_rawData.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->rawData);
      union {
        int8_t real;
        uint8_t base;
      } u_Density;
      u_Density.real = this->Density;
      *(outbuffer + offset + 0) = (u_Density.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->Density);
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
      union {
        int8_t real;
        uint8_t base;
      } u_rawData;
      u_rawData.base = 0;
      u_rawData.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->rawData = u_rawData.real;
      offset += sizeof(this->rawData);
      union {
        int8_t real;
        uint8_t base;
      } u_Density;
      u_Density.base = 0;
      u_Density.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->Density = u_Density.real;
      offset += sizeof(this->Density);
     return offset;
    }

    const char * getType(){ return "navigation/sensor_raw_data"; };
    const char * getMD5(){ return "4289632367261194ad885af894d145a0"; };

  };

}
#endif