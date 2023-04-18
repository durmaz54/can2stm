#include <ncurses.h>

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
            // Up arrow key is pressed
            // do something
        } else if (ch == KEY_DOWN) {
            // Down arrow key is pressed
            // do something
        } else if (ch == KEY_LEFT) {
            // Left arrow key is pressed
            // do something
        } else if (ch == KEY_RIGHT) {
            // Right arrow key is pressed
            // do something
        } else if (ch == 'q' || ch == 'Q') {
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
