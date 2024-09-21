import os
import tkinter as tk
from tkinter import filedialog, Listbox, Label, Scrollbar, PhotoImage
from PIL import Image, ImageTk


class ImageExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Explorer")
        self.geometry("800x600")

        # Create a frame for the file list
        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        # Listbox to display files
        self.file_listbox = Listbox(self.frame, width=50)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox.bind("<<ListboxSelect>>", self.show_preview)

        # Scrollbar for the listbox
        self.scrollbar = Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.file_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)

        # Label to show image preview
        self.preview_label = Label(self, text="Select an image to preview", bg="gray", width=50, height=25)
        self.preview_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Load files
        self.load_files()

    def load_files(self):
        folder_path = "data/front_2"#filedialog.askdirectory()
        if folder_path:
            files = os.listdir(folder_path)
            image_files = [f for f in files]#if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            for file in image_files:
                self.file_listbox.insert(tk.END, os.path.join(folder_path, file))

    def show_preview(self, event):
        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        image = Image.open(selected_file)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.preview_label.config(image=photo, text="")
        self.preview_label.image = photo


if __name__ == "__main__":
    app = ImageExplorer()
    app.mainloop()