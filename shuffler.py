import os
import random
import tkinter as tk
from tkinter import filedialog

avoid_extensions = [".NONE", ".NONE"]  # add more extensions if needed
image_extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".mp3", ".mp4"]  # idk how to explain this

def get_files_grouped_by_type(folder_path, avoid_extensions):
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, file)) and 
             not any(file.endswith(ext) for ext in avoid_extensions)]

    return {
        "images": [file for file in files if any(file.endswith(ext) for ext in image_extensions)],
        "others": [file for file in files if not any(file.endswith(ext) for ext in image_extensions)]
    }

def swap_file_contents(folder_path, avoid_extensions):
    file_groups = get_files_grouped_by_type(folder_path, avoid_extensions)

    def swap_data(file_list):
        if len(file_list) < 2:
            return

        file_data = [open(file, "rb").read() for file in file_list]

        while True:
            random.shuffle(file_data)

            if all(open(file, "rb").read() != file_data[i] for i, file in enumerate(file_list)):
                break

        for file, data in zip(file_list, file_data):
            with open(file, "wb") as f:
                f.write(data)

    swap_data(file_groups["images"])
    swap_data(file_groups["others"])

    print("Success!")

# Use tkinter to show folder picker
root = tk.Tk()
root.withdraw()  # Hide the main window
selected_folder = filedialog.askdirectory(title="Select Folder")

if selected_folder:
    print(f"Selected Folder: {selected_folder}")
    swap_file_contents(selected_folder, avoid_extensions)
else:
    print("No folder selected.")
