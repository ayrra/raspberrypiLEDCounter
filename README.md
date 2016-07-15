# raspberrypiLEDCounter

<img class="alignnone wp-image-1166 size-large" src="http://www.yrra.net/data/uploads/2015/09/IMG_2640-1024x768.jpg" alt="IMG_2640" width="1024" height="768" />

Binary LED Counter Using A Raspberry Pi!
For a starter program into using GPIO pins I decided to build a LED Binary Counter using 2 buttons and 8 LED’s. The 8 LED’s will represent a number in binary from 0 up to 255, and the buttons will either increment or decrement the counter.

The code is written in python using the raspberry pi’s own python package (RPi.GPIO) to control the GPIO pins, and the time package to allow sleeps.

The setup is fairly simple, we set our code to run in BCM mode, setup the 8 output pins for the LED’s and the 2 input pins for the buttons, then we set all the output pins to low just in case a past program didn’t clean up.

Now to the real code, we declare a counter that we will be using throughout the program. This counter value will be represented in binary by the LED’s.

Next we define our first function, buttonHandler()

This function will be using pin 27 as the increment button, and pin 17 as the decrement button. There are 4 different if conditions for the buttons, the first two are for the increment button.

We check if the button is pressed and the counter is not at 255, then we will increment the counter by 1, output to the console, and sleep.

The second checks if the button is pressed and the counter is 255, then we will set the counter back to 0. (We don’t want to go over 255 since we can’t display any higher using our LED’s)

The last two if conditions work the same but decrement and instead of using 255 we check for 0. (if we decrement at 0 we set the counter to 255)

Our second function is ledLogic(c),

This is where all the LED logic will take place, and its fairly simple.
We will be feeding the parameter c into the bin() function. This bin function will convert an integer into a string of 0’s and 1’s representing that integer.
The leading [2:].zfill(8) will cut off the first 2 characters of the string and force the string to be 8 characters.
For example if the counter is 9, we will get a 00001001 (note that this string will always be 8 characters, and we have 8 LED’s)

So in essence we always have a string of 8 0’s and 1’s.
Next we enumerate through this string, we check the value at each index, if we have a ‘1’ then we turn on that LED at that index.
If we have a ‘0’ we turn off the LED at that index. Turning the LED’s on and off is handled by passing the index to a ledOn or LedOff function.
For example, continuing with the counter = 9 example we will enumerate through
index
0 1 2 3 4 5 6 7
value
0 0 0 0 1 0 0 1
and these are the functions that will be ran.
ledOff(0)
ledOff(1)
ledOff(2)
ledOff(3)
ledOn(4)
ledOff(5)
ledOff(6)
ledOn(7)

The ledOn(pin) and ledOff(pin) functions both consist of 8 if statements, where depending on the fed parameter (index) will turn on or off the corresponding LED.

Now to put the code together,
Just run buttonHandler() and ledLogic(counter) in an infinite while loop!
