#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <linux/can.h>
#include <linux/can/raw.h>


using namespace std;
int main(){
    int s;
struct sockaddr_can addr;
struct ifreq ifr;

s = socket(PF_CAN, SOCK_RAW, CAN_RAW);

strcpy(ifr.ifr_name, "can0" ); // VCAN0 arayüzünün adı
ioctl(s, SIOCGIFINDEX, &ifr);

addr.can_family = AF_CAN;
addr.can_ifindex = ifr.ifr_ifindex;

bind(s, (struct sockaddr *)&addr, sizeof(addr));

struct can_frame frame;
frame.can_id = 0x17;
frame.can_dlc = 8;
frame.data[0] = 0x11;
frame.data[1] = 0x22;

for (int8_t  i = 0; i < 8; i++)
{
    frame.data[i] = 0x54;
}

float f = 3.14159f;

memcpy(frame.data, &f, 4);

write(s, &frame, sizeof(struct can_frame));


    return 0;
}