A simple python script with no gui that can be used in conjunction with LD Player to automate refreshing alliance mobilization tasks for the mobile game WhiteOut Survival (WOS).

Limitations:
Unable to work in the background. So your computer is dedicated to WOS while this is running. That said you can alt tab out just fine, it just won't do anything unless a similar picture appears on your screen.

How to use:

There are 4 arrays in the script:
- LIST_OF_TASKS_TO_REFRESH contains what you need to refresh immediately.
- LIST_OF_TASKS_TO_CHECK contains what you might want to keep. But as we know, each task has 4 tiers so...
- LIST_OF_TASK_DESCRIPTIONS and LIST_OF_DESCRIPTIONS_TO_REFRESH contains the description of the tasks. One uses computer vision to look for the text box (LIST_OF_TASK_DESCRIPTIONS) and the other uses OCR to read the actual description (LIST_OF_DESCRIPTIONS_TO_REFRESH).

You can comment/uncomment the array elements as necessary.

The current pictures are what I needed so you might want to get your own screenshots and put them into the arrays.

Once done setting, simply run the script and if your LD Player (or any other android emulator I guess) is on screen at the alliance mobilization tab, it'll start the grind for you. To stop the script press CTRL + C in the terminal. Good luck~
