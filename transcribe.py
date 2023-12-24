import whisper
import torch
import tkinter.filedialog as filedialog
import datetime
import os
import sys

result = ""
input_file = filedialog.askopenfilename()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base").to(device)

try:
    result = model.transcribe(input_file, fp16=False)
except Exception as e:
    print("Error transcribing: ", e)

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"transcript_{now}.txt"

try:
    with open(file_name, "w") as f:
        for i in result["segments"]:
            f.write(
                f'{int(i["start"] / 60)}:{int(i["start"] % 60)} - {int(i["end"] / 60)}:{int(i["end"] % 60)}: {i["text"]} \n'
            )
except Exception as e:
    print("Error in file writing:", e)

try:
    os.system(f"start {file_name}")
except Exception as e:
    print("Error in opening file:", e)

counter = 1
for i in result["segments"]:
    print(
        f'{counter} {int(i["start"] / 60)}:{int(i["start"] % 60)} - {int(i["end"] / 60)}:{int(i["end"] % 60)}: {i["text"]}'
    )
    counter += 1
# print(result)
