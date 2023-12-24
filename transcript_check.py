import tkinter.filedialog as filedialog

keywords = [
    "westreet",
    "we street",
    "member",
    "membership",
    "Thank you for calling",
    "thank you",
]


input_file = filedialog.askopenfilename()

with open(input_file, "r") as f:
    for line_number, line in enumerate(f, 1):
        if any(keyword.lower() in line.lower() for keyword in keywords):
            print(f"Found a keyword in line {line_number}: {line.strip()}")
            print("---")
