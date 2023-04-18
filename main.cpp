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
#include <unistd.h>
#include <chrono>
#include <thread>

using namespace std::chrono_literals;





using namespace std;
int main(){
    useconds_t usec = 1000;
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

float f = 0.0f;
float c = 0.0f;

memcpy(frame.data, &f, 4);
memcpy(frame.data[4], &c, 4);

while (1)
{
   write(s, &frame, sizeof(struct can_frame));
   f+=0.01;
   c-=0.01;
   memcpy(frame.data, &f, 4);
   memcpy(frame.data[4], &c, 4);

   cout << "data send " << f << endl;
   sleep(1);
}


    return 0;
}