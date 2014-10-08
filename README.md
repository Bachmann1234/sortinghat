sortinghat
==========

Harry Potter Sorting Hat.

I don't own the audio. I think I can make an argument for fair use but I can takedown if necessary

To install:
Install homebrew
brew install portaudio
pip install -r requirements.txt


running python sort.py builds and plays a script randomly generated from
some stalling lines a potential announcement of 'I KNOW', then finally the house.

Only the house is guaranteed, any other sound is random

Pass in a serial port and the script will read from it. If it gets ```YEP``` the script will play. Once it is done the script will block until something other than ```YEP``` is read.

And yes, the ravenclaw sound is kinda lame... sorry.. the hat does not seem to say it in the movie