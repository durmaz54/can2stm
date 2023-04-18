#include <ncurses.h>
#include <iostream>

using namespace std;
int main() {
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
        if (ch == KEY_UP) {
            cout << "up" << endl;
            // Up arrow key is pressed
            // do something
        } else if (ch == KEY_DOWN) {
            cout << "down" << endl;
            // Down arrow key is pressed
            // do something
        } else if (ch == KEY_LEFT) {
            cout << "left" << endl;
            // Left arrow key is pressed
            // do something
        } else if (ch == KEY_RIGHT) {
            cout << "right" << endl;
            // Right arrow key is pressed
            // do something
        } else if (ch == 'q' || ch == 'Q') {
            cout << "q" << endl;
            // Q key is pressed
            break;
        } else {
            // Unknown key is pressed
        }
    }

    // Clean up ncurses library
    endwin();

    return 0;
}
