import customtkinter
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

import os
from tkinter import filedialog, Canvas, Scrollbar, VERTICAL, HORIZONTAL


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Athensoft PDF Helper - Merger v2.4.2")
        self.geometry("960x720+20+20")

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

        # Add file chooser button
        self.file_button = customtkinter.CTkButton(self.home_frame, text="Choose PDF", command=self.choose_file)
        self.file_button.grid(row=1, column=0, padx=20, pady=20)

        # Create a canvas to enable scrolling
        self.canvas = Canvas(self.home_frame)
        self.canvas.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Horizontal and Vertical Scrollbars
        self.h_scrollbar = Scrollbar(self.home_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.grid(row=3, column=0, sticky="ew")

        self.v_scrollbar = Scrollbar(self.home_frame, orient=VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.grid(row=2, column=1, sticky="ns")

        # Configure the canvas to use the scrollbars
        self.canvas.configure(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)

        # Create a frame inside the canvas to hold the table contents
        self.table_frame = customtkinter.CTkFrame(self.canvas, corner_radius=0, fg_color="transparent")
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        # Ensure the canvas scroll region updates when the table frame changes
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Ensure the frame expands with the window
        self.home_frame.grid_rowconfigure(2, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Add "Move Up" and "Move Down" buttons below the table
        # Create a new button_frame inside the parent container (self.home_frame)
        self.button_frame = customtkinter.CTkFrame(self.home_frame, fg_color="transparent")
        self.button_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Add "Move Up" and "Move Down" buttons to the button_frame, stacked horizontally
        self.move_up_button = customtkinter.CTkButton(self.button_frame, text="Move Up", command=self.move_up)
        self.move_up_button.grid(row=0, column=0, padx=10, pady=5)

        self.move_down_button = customtkinter.CTkButton(self.button_frame, text="Move Down", command=self.move_down)
        self.move_down_button.grid(row=0, column=1, padx=10, pady=5)

        # Add merge button
        self.merge_button = customtkinter.CTkButton(self.home_frame, text="Merge", command=self.merge_pdfs)
        self.merge_button.grid(row=5, column=0, padx=20, pady=20)

        # To hold selected files
        self.selected_files = []

        # To hold table rows
        self.table_rows = []


        # -------------------
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

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

        if selected_files:
            self.selected_files.extend(selected_files)  # Add multiple files to the list
            self.update_table()

    def update_table(self):
        # Clear existing table rows
        for row in self.table_rows:
            row.grid_forget()
        self.table_rows.clear()

        # Add new rows to the table for each selected file
        for index, file in enumerate(self.selected_files):
            row_frame = customtkinter.CTkFrame(self.table_frame, corner_radius=0, fg_color="#ffffff")
            row_frame.grid(row=index, column=0, padx=1, pady=3, sticky="nsew")

            # Checkbox for each row
            checkbox = customtkinter.CTkCheckBox(row_frame, text="", width=20,
                                                 command=lambda i=index: self.set_active_row(i))
            checkbox.grid(row=0, column=0, padx=1, pady=3)

            # PDF file path label
            file_label = customtkinter.CTkLabel(row_frame, text=file)
            file_label.grid(row=0, column=1, padx=5, pady=5)

            # Save row frame to list for future reference
            self.table_rows.append(row_frame)

    def set_active_row(self, index):
        # Mark the clicked row as active by saving the index
        self.active_row_index = index
        print(f"Active row: {self.active_row_index}")

    def move_up(self):
        if self.active_row_index is not None and self.active_row_index > 0:
            # Swap the files in the list and update the table
            self.selected_files[self.active_row_index], self.selected_files[self.active_row_index - 1] = \
                self.selected_files[self.active_row_index - 1], self.selected_files[self.active_row_index]
            self.active_row_index -= 1
            self.update_table()

    def move_down(self):
        if self.active_row_index is not None and self.active_row_index < len(self.selected_files) - 1:
            # Swap the files in the list and update the table
            self.selected_files[self.active_row_index], self.selected_files[self.active_row_index + 1] = \
                self.selected_files[self.active_row_index + 1], self.selected_files[self.active_row_index]
            self.active_row_index += 1
            self.update_table()

    def merge_pdfs(self):
        input_pdfs = self.selected_files
        merger = PdfWriter()

        for pdf in input_pdfs:
            with open(pdf, 'rb') as file:
                reader = PdfReader(file)
                print(f"[INFO] {pdf} loaded.")
                for page in reader.pages:
                    merger.add_page(page)

        # Save merged PDF to the Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "merged_output.pdf")
        with open(desktop_path, 'wb') as merged_file:
            merger.write(merged_file)

        print(f"Merged PDF saved to {desktop_path}")


if __name__ == "__main__":
    app = App()
    app.mainloop()

