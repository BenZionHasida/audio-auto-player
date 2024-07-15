# Audio-Auto-Player

This is a simple audio player that plays audio files in a directory in a loop. It is intended to be used in EC2s for phone calls testing.
* script.py - include the player logic
* dist folder with the following files:
  * mp3_player.exe - the executable file
  * start_costumer_audio.bat - a batch file that starts the player
  * Customer.mp3 - an audio file that is played by the player
  * playTask.xml - a task scheduler file that starts the player every time the machine starts
  
## How to use
1. Download the dist folder
2. Edit the start_costumer_audio.bat file and change the path to mp3_player_log.txt to absolute path
3. Edit the playTask.xml file and change the following fields: 
    * <Author></Author> - run "echo %USERDOMAIN%\%USERNAME%" in the command line to get the user name
    * <UserId></UserId> - run "wmic useraccount where name='%USERNAME%' get sid" in the command line to get the user sid
    * <Command></Command> - change the path to the start_costumer_audio.bat file
4. open Task Scheduler and import the playTask.xml file

The player will start playing the audio file every time the machine starts or user logged in.