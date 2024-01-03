import whisper
import torch
import tkinter.filedialog as filedialog
import datetime
import os
import sys
import re

# TODO
# Accept multiple files at a time and place transcripts in their respective files
# Rename transcripts to match their respective video file
# Create a selection box to allow user to select base, medium, or large AI model

# options are base, tiny, medium, and large
loaded_model = "base"

input_folder = filedialog.askdirectory()


pattern = re.compile(r"(?<!\d:)(?<!-\s)\d(?!\d*:)(?!\d*-\s)")
result = ""
output_path = input_folder
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file_name = f"{output_path}\\transcript_{now}.txt"

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model(loaded_model).to(device)


file_extensions = [".mp4", ".mov", ".flac", ".mp3", ".wav", ".mkv"]

files = os.listdir(input_folder)
files = [
    os.path.join(input_folder, file)
    for file in os.listdir(input_folder)
    if os.path.isfile(os.path.join(input_folder, file))
]
file_names = [
    file for file in files if os.path.isfile(os.path.join(input_folder, file))
]
parse_filename = []
session_ids = []
users = []
session_id = ""
user = ""
for i in files:
    parse_filename.append(i.split("/"))
for i in parse_filename:
    session_id = i[-1:][0].split("\\")[-1].split("_")[0]
    user = i[-1:][0].split("\\")[-1].split("_")[-1].split(".")[0]
    session_ids.append(session_id)
    users.append(user)

results = []
for i in range(len(files)):
    if not os.path.isfile(files[i]):
        continue
    _, extension = os.path.splitext(files[i])
    if extension.lower() in file_extensions:
        try:
            transcription = {}
            result = model.transcribe(files[i], fp16=False)
            transcription[f"{file_names[i]}"] = result
            results.append(transcription)
        except Exception as e:
            result = f"Exception transcribing {files[i]} -- {e}"
            print(f"Exception transcribing {files[i]} -- {e}")
    else:
        continue

    output_file_name = f"{output_path}\\{users[i]}_{session_ids[i]}_transcript.txt"

    try:
        with open(output_file_name, "w", encoding="utf-8") as f:
            for i in result["segments"]:
                f.write(
                    f'{int(i["start"] / 60)}:{int(i["start"] % 60)} - {int(i["end"] / 60)}:{int(i["end"] % 60)}: {i["text"]} \n'
                )
    except Exception as e:
        print("Error in file writing:", e)

    with open(output_file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_file_name, "w", encoding="utf-8") as f:
        for line in lines:
            modified_line = pattern.sub("9", line)
            f.write(modified_line)
