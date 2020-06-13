# automation-spammer
This is a automation script that searches for a lyrics of any specified song on genius.com and then send its entire lyrics word by word on whatsapp.

## Requirements
we need to download chromedriver extension seperately so that our script can control chrome, otherwise our script wont be able to run.
download the latest WebDriver version from [here](https://sites.google.com/a/chromium.org/chromedriver/)

## working
ones we have installed requirements we just need to run the script.
Here how it works
1) open chrome window
2) searcher for the specified song on [genius.com](https://genius.com)
3) copy the lyrics and stores them in a new text file by the song name
4) closes the browser
5) opens whatsapp web in another browser
6) ask the user to enter the person name/group name to send the messages.
7) Read the previously creaed text file and send its content word by word to the person/group
8) closes the browser and terminates

## video
check the visual workinng of he script in the [video](https://drive.google.com/file/d/1r_Bso4XTRTXw3Js9t4AagoEtx8GYL6R9/view?usp=sharing)
