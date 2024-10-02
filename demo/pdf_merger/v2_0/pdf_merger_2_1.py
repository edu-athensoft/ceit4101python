import customtkinter
import os
from PIL import Image
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Athensoft PDF Helper - Merger v2.0")
        self.geometry("1280x720+20+20")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Add file chooser button
        self.file_button = customtkinter.CTkButton(self.home_frame, text="Choose PDF", command=self.choose_file)
        self.file_button.grid(row=1, column=0, padx=20, pady=20)

        # Create a listbox to display selected files
        self.file_listbox = customtkinter.CTkTextbox(self.home_frame, height=150)
        self.file_listbox.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # To hold selected files
        self.selected_files = []

        # select default frame
        self.select_frame_by_name("home")

    def choose_file(self):
        # Open file dialog to choose multiple PDFs
        filetypes = [('PDF files', '*.pdf')]
        selected_files = filedialog.askopenfilenames(title="Select PDFs", filetypes=filetypes)

        # Check if files are selected and add them to the list
        if selected_files:
            self.selected_files.extend(selected_files)  # Add multiple files to the list
            self.update_file_listbox()

    def update_file_listbox(self):
        # Clear the listbox and update with new file list
        self.file_listbox.delete("1.0", "end")
        for file in self.selected_files:
            self.file_listbox.insert("end", file + "\n")

    def select_frame_by_name(self, name):
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")

    def home_button_event(self):
        self.select_frame_by_name("home")


if __name__ == "__main__":
    app = App()
    app.mainloop()
