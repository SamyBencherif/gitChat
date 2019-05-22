

# CLI Messenger

This program uses no external dependancies. It will run on any UNIX compliant machine running Python 2.X or higher. To start it, `cd` into the correct directory and run:

```bash
chmod +x messenger
./messenger
```

# Help

### The backspace key does not work

open messenger in a text editor and change the variable BACKSPACE to the correct keycode for your system. There is a next to that line that tells you
about a couple common systems. 

Search for "disp pressed char", and you uncomment the following line to allow the messenger program to report the keycodes it recieves.

### How to close the program
 
Press Ctrl-C. You will be prompted with a list of options. Press the down arrow key once to select "Quit". Press Enter.
