#include <ros/ros.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Bool.h>
#include "guzergah_autonomous/actuators.h"
#include "guzergah_autonomous/sensors.h"
#include "agv2stm.h"

// actuators.msg datas
/*
float64 sol_istenen_hiz
float64 sag_istenen_hiz
float64 lift_mesafe
bool lift_kaldir
*/

// sensors.mgs datas:
/*
float64 lift_sicaklik
float64 lift_agirlik
float64 lift_akim

float64 sol_motor_hiz
float64 sol_motor_sicaklik
float64 sol_motor_akim

float64 sag_motor_hiz
float64 sag_motor_sicaklik
float64 sag_motor_akim

float64 gerilim
*/

AGV2STM agv;

void motorsCallback(const guzergah_autonomous::actuators& data)
{
    agv.motorWrite(data.sol_istenen_hiz, data.sag_istenen_hiz);
}

void liftCallback(const guzergah_autonomous::actuators& data)
{
    if (data.lift_kaldir)
    {
        agv.setLiftUp();
    }
    else
    {
        agv.setLiftDown();
    }
}

void stm2ROSPublish(ros::Publisher& pub)
{
    guzergah_autonomous::sensors status;
    status.lift_sicaklik = agv.temp1;
    status.lift_agirlik = 0.0; // not implemented in agv2stm.h
    status.lift_akim = agv.motorLiftCurrent;
    status.sol_motor_hiz = agv.motorLeftSpeed;
    status.sol_motor_sicaklik = agv.temp2;
    status.sol_motor_akim = agv.motorLeftCurrent;
    status.sag_motor_hiz = agv.motorRightSpeed;
    status.sag_motor_sicaklik = agv.temp3;
    status.sag_motor_akim = agv.motorRightCurrent;
    status.gerilim = agv.battery;
    pub.publish(status);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "can_communication_node");
    ros::NodeHandle nh;
    ros::Subscriber motors_sub = nh.subscribe("/AGV/differential_speeds", 1, motorsCallback);
    ros::Subscriber lift_sub = nh.subscribe("/AGV/lift", 1, liftCallback);
    ros::Publisher pub = nh.advertise<guzergah_autonomous::sensors>("/AGV/status", 10);

    ROS_INFO("CAN communication node has started");

    ros::Rate rate(10);
    while (ros::ok())
    {
        stm2ROSPublish(pub);
        rate.sleep();
        ros::spinOnce();
    }

    return 0;
}
