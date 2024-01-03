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

# input_folder = filedialog.askdirectory()


pattern = re.compile(r"(?<!\d:)(?<!-\s)\d(?!\d*:)(?!\d*-\s)")
result = ""
input_file = filedialog.askopenfilename()
output_path = os.path.dirname(input_file)
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file_name = f"{output_path}\\transcript_{now}.txt"

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model(loaded_model).to(device)


def return_files(input_folder):
    files = os.listdir(input_folder)
    files = [file for file in files if os.path.isfile(os.path.join(input_folder, file))]
    results = []
    for i in files:
        try:
            result = model.transcribe(i, fp16=False)
            results.append(result)
        except Exception as e:
            result = "Exception transcribing {i} -- {e}"
            print(f"Exception transcribing {i} -- {e}")
            return result

    return results


def transcode_file(input_file):
    try:
        result = model.transcribe(input_file, fp16=False)
    except Exception as e:
        print("Error transcribing: ", e)
    return result


transcode_file(input_file)

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

try:
    with open(output_file_name, "r+", encoding="utf-8") as f:
        for line in f:
            print(line)
except Exception as e:
    print("Exception:", e)

try:
    os.system(f"start {output_file_name}")
except Exception as e:
    print("Error in opening file:", e)
