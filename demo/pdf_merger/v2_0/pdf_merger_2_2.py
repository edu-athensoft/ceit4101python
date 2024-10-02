import customtkinter
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

import os
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Athensoft PDF Helper - Merger v2.0")
        self.geometry("1280x720+20+20")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-roundedsquare-07.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "weather-utility.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Athensoft", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Guide",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # -------------------
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="Input a city name")
        # self.entry.grid(row=2, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #
        # self.main_button_1 = customtkinter.CTkButton(master=self.home_frame, fg_color="transparent", border_width=2,
        #                                              text_color=("gray10", "#DCE4EE"), text="Query Weather",
        #                                              command=self.on_main_button_1_click)
        # self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Add file chooser button
        self.file_button = customtkinter.CTkButton(self.home_frame, text="Choose PDF", command=self.choose_file)
        self.file_button.grid(row=1, column=0, padx=20, pady=20)

        # Create a listbox to display selected files
        self.file_listbox = customtkinter.CTkTextbox(self.home_frame, height=150)
        self.file_listbox.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # To hold selected files
        self.selected_files = []

        # Add merge button
        self.merge_button = customtkinter.CTkButton(self.home_frame, text="Merge", command=self.merge_pdfs)
        self.merge_button.grid(row=3, column=0, padx=20, pady=20)

        # -------------------
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def on_main_button_1_click(self):
        input_text = self.entry.get()
        print(input_text)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # home_frame
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

    def merge_pdfs(self):

        # Get the content from the file listbox
        files_content = self.file_listbox.get("1.0", "end").strip()  # Read the text and strip extra spaces

        # Split the content by lines to get the list of file paths
        file_list = files_content.split("\n")

        # Filter out empty strings (if any)
        file_list = [f for f in file_list if f.strip()]

        # Save to self.selected_files
        self.selected_files = file_list

        input_pdfs = self.selected_files

        merger = PdfWriter()

        for pdf in input_pdfs:
            with open(pdf, 'rb') as file:
                reader = PdfReader(file)
                print(f"[INFO] {pdf} loaded.")

                # Add all the pages from the current PDF
                for page in reader.pages:
                    merger.add_page(page)

        # Get the user's Desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "merged_output.pdf")
        # merged_pdf = 'merged.pdf'

        merged_pdf = desktop_path
        # Write the merged output to a new file
        with open(merged_pdf, 'wb') as merged_file:
            merger.write(merged_file)

        # return merged_pdf


if __name__ == "__main__":
    app = App()
    app.mainloop()

