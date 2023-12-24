# Readme
You'll need to install a list of dependencies. 
> Note this currently only runs on python 3.8-python 3.10.

### Required dependencies: 
torch 

whisper

## How to use this script
You simply save this script and then run it with 
```
python transcribe.py
```
Then a file dialog will pop up and wait for you to browse to and select the file that you want to transcribe. Once done, it will take a few moments (may take minutes, depending on file size) and transcribe the audio/video file. Then it will output a transcript.txt file in the same directory that you ran this script from. 

Then run the transcript_check.py file and it will search the transcript for key terms and return to you which line they're on. 

## Whisper docs: 
[Docs](https://github.com/openai/whisper)