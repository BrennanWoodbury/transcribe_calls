# Readme
You'll need to install a list of dependencies. 
> Note this currently only runs on python 3.8-python 3.10.

### Required dependencies: 
torch 

whisper

ffmpeg (install through chocolatey or install the binary from their website and add the path to your system path. )

> If you're unable to add ffmpeg to your path, you'll need to add it temporarily anytime you're in the command prompt, with the following command: 

```
set PATH=%PATH%;C:\path\to\ffmpeg\bin
```

ffmpeg-python

## How to use transcribe.py
You simply save this script and then run it with 
```
python transcribe.py
```
Then a file dialog will pop up and wait for you to browse to and select the file that you want to transcribe. Once done, it will take a few moments (may take minutes, depending on file size) and transcribe the audio/video file. Then it will output a transcript.txt file in the same directory that you ran this script from. 

Then run the transcript_check.py file and it will search the transcript for key terms and return to you which line they're on.

## How to use transcribe_folder.py
You simply save this script and then run it with 
```
python transcribe_folder.py
```
Then a file dialog will pop up and wait for you to browse and select the folder that contains all the files that you want to transcribe within it. Once done, it will take a few moments (may take minutes, depending on file size) and transcribe the audio/video files. Then it will output a {user}_{session_id}_transcript.txt file in the directory that you selected at the start.   

## Whisper docs: 
[Docs](https://github.com/openai/whisper)