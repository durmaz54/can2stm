#include <ncurses.h>
#include <iostream>
#include <stdio.h>
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

using namespace std;
int main() {

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
memcpy(&frame.data[4], &c, 4);


    // Initialize ncurses library
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, true);

    // Main loop
    while (true) {
        // Read a key press
        int ch = getch();
        
        // Check if any arrow key is pressed
        if (ch == 'w') {
             f+=0.01;
            // Up arrow key is pressed
            // do something
        } else if (ch == 's') {
             f-=0.01;
            // Down arrow key is pressed
            // do something
        } else if (ch == 'a') {
                    c-=0.01;

            // Left arrow key is pressed
            // do something
        } else if (ch == 'd') {
                    c+=0.01;
        } else if (ch == 'q' || ch == 'Q') {
            cout << "q" << endl;
            f=0.0f;
            c=0.0f;
            memcpy(frame.data, &f, 8);
            write(s, &frame, sizeof(struct can_frame));
            break;
        } else {
            // Unknown key is pressed
        }
        float a = f-c;
        float b = f+c;
        cout << a << "   " << b << endl;
        memcpy(frame.data, &a, 4);
        memcpy(&frame.data[4], &b, 4);
        write(s, &frame, sizeof(struct can_frame));

    }

    // Clean up ncurses library
    endwin();

    return 0;
}
