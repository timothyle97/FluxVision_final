# FluxVision
FluxVision is a set of scripts for playing a YouTube playlist on loop on a Raspberry Pi. Anyone with access to a designated YouTube account can add a video to the playlist. This allows for simple administration of an easy to update, collaboratively-curated (if desired), looping video installation that doesn't require physical access to the player.

##### Features:
* Videos are downloaded once (not streamed)
* Automatically detects and downloads new videos when they are added to the YouTube playlist, usually available within one playthrough
* Automatically mutes at night (times can be edited)
* Support for a character LCD ticker that displays the title of the current video (requires [Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD))
* Support for an external skip button that advances to the next video
* Support for an external volume knob that adjusts video volume in real time (using a simple analog-to-digital converter with a linear potentiometer connected via GPIO pins)
* Support for blacklisting videos by title (Add the blacklisted title or phrase as a line to 'blacklist.txt')

##### Note:
* Recommended operating system is Raspbian Jessie, on which FluxVision was developed and stress tested. (Omxplayer was found to randomly hang between videos on Raspbian Wheezy.)
* Latest tested on Raspberry Pi OS Lite (Legacy)
  * Release date: April 4th 2022
  * System: 32-bit
  * Kernel version: 5.10
  * Debian version: 10 (buster)
  * Size: 284MB
  * SHA256 file integrity hash: 42fd907a0da36b8a8ce9db9cd1cb77746b6a10c4b77f8d0ae0b8065a3b358a37
* Original repository: https://github.com/jasoneppink/FluxVision
* Forked repository: https://github.com/amin24099/FluxVision_final

## Installation

1. Install yt-dlp (https://github.com/yt-dlp/yt-dlp).

   youtube-dl was downloading videos very slowly from YouTube (~500Kbps); therefore, switched to yt-dlp. 


    ~~sudo pip install --upgrade youtube_dl~~
  ```
  sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
  sudo chmod a+rx /usr/local/bin/yt-dlp
  ```
2. Install omxplayer and libav-tools.

  ```
  sudo apt-get install omxplayer libav-tools
  ```
3. Download FluxVision files to your Raspberry Pi.

  ```
  git clone https://github.com/timothyle97/FluxVision_final
  ```
4. Update "config.txt" with your playlist ID and other details.

  ```
  cd FluxVision
  nano config.txt
  ```
5. (optional) Uncomment lines in "startup.sh" if you are using a ticker, skip button, or volume knob.

  ```
  nano startup.sh
  ```
6. Open /etc/rc.local:

  ```
  sudo nano /etc/rc.local
  ```
  and add this line so FluxVision starts at boot:

  ```
  sudo -u pi /home/pi/FluxVision/startup.sh
  ```
7. (optional) Clear disk space for downloaded videos. If you're running Raspbian, this command can remove up to 1GB of applications you probably don't use.

  ```
  sudo apt-get remove wolfram-engine minecraft-pi python-minecraftpi sonic-pi oracle-java8-jdk pistore scratch nuscratch python3-pygame
  ```
8. Reboot! Videos play as soon as they're downloaded.

  ```
  sudo reboot
  ```
