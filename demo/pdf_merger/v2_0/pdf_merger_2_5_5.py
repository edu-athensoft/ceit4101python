import customtkinter
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

import os
from tkinter import filedialog, Canvas, Scrollbar, VERTICAL, HORIZONTAL
from tkinter import messagebox
from tkinter import PhotoImage


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ---------------
        # Settings
        self.title("Athensoft PDF Toolkit - Merger v2.5.4")
        self.geometry("1020x720+20+20")

        # Set main window grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Set image path
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        # Set custom icon (.png example, use iconphoto for cross-platform support)
        icon_path = os.path.join(image_path, "logo-roundedsquare-07.png")
        icon_image = PhotoImage(file=icon_path)
        self.iconphoto(True, icon_image)

        # Load images icon on menu
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo-roundedsquare-07.png")), size=(26, 26))
        self.large_banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_banner.png")), size=(768, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.help_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "help_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "help_dark.png")), size=(20, 20))
        self.guide_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "guide_light.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "guide_dark.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings_dark.png")), size=(20, 20))

        # Set key button
        self.BUTTON_HOVER_COLOR = "#82eaed"

        # Set the default system desktop path
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.default_path = self.desktop_path

        # ------------------
        # Navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        
        # Navigation frame - Logo and Title
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Athensoft PDF Merger ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=20)

        # Navigation frame - Menu items
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.guide_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Guide",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.guide_image, anchor="w", command=self.guide_button_event)
        self.guide_button.grid(row=2, column=0, sticky="ew")

        self.help_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.help_image, anchor="w", command=self.help_button_event)
        self.help_button.grid(row=3, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.settings_image, anchor="w",
                                                      command=self.settings_button_event)
        self.settings_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event, width=200)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # Navigation frame - Ad slots
        self.img_sidebar_ad_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ad_sidebar_1.png")), size=(200, 150))
        self.img_sidebar_ad_2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ad_sidebar_2.png")), size=(200, 150))

        self.adslot_sidebar_label_1 = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.img_sidebar_ad_1)
        self.adslot_sidebar_label_1.grid(row=5, column=0, padx=10, pady=5, sticky="s")

        self.adslot_sidebar_label_2 = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.img_sidebar_ad_2)
        self.adslot_sidebar_label_2.grid(row=6, column=0, padx=10, pady=5, sticky="s")

        # -------------------------------------------------------------------------
        # Home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Home frame - Large Banner Ad Slot
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_banner_image)
        self.home_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=0, pady=(0, 10))

        # Home frame - Button frame top
        # --- button_frame inside the parent container (self.home_frame)
        self.button_frame_top = customtkinter.CTkFrame(self.home_frame, fg_color="transparent")
        self.button_frame_top.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Home frame - Button frame top - "File chooser" button
        self.file_button = customtkinter.CTkButton(self.button_frame_top, text="Choose PDF", command=self.choose_file,
                                                   width=70, fg_color=("orange", "orange"),
                                                   text_color=("black", "black"),
                                                   hover_color=(self.BUTTON_HOVER_COLOR, self.BUTTON_HOVER_COLOR))
        self.file_button.grid(row=0, column=0, padx=10, pady=5)

        # Home frame - Button frame top - "Select All" button
        self.select_all_button = customtkinter.CTkButton(self.button_frame_top, text="Select All", command=self.select_all,
                                                         width=70, state="disabled")
        self.select_all_button.grid(row=0, column=1, padx=10, pady=5)

        # Home frame - Button frame top - "Unselect All" button
        self.unselect_all_button = customtkinter.CTkButton(self.button_frame_top, text="Unselect All",
                                                           command=self.unselect_all, width=70, state="disabled")
        self.unselect_all_button.grid(row=0, column=2, padx=10, pady=5)

        # Home frame - Button frame top - "Remove" button
        self.remove_button = customtkinter.CTkButton(self.button_frame_top, text="Remove Selected PDF",
                                                     command=self.remove_selected,
                                                     width=70, state="disabled")
        self.remove_button.grid(row=0, column=3, padx=10, pady=5)

        # Home frame - Scrollable Canvas
        self.canvas = Canvas(self.home_frame)
        self.canvas.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Home frame - Scrollbars for Canvas
        self.h_scrollbar = Scrollbar(self.home_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.grid(row=3, column=0, sticky="ew")

        self.v_scrollbar = Scrollbar(self.home_frame, orient=VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.grid(row=2, column=1, sticky="ns")

        self.canvas.configure(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)

        # Home frame - Table frame for table contents
        self.table_frame = customtkinter.CTkFrame(self.canvas, corner_radius=0, fg_color="transparent")
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        # --- ensure the canvas scroll region updates when the table frame changes
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # --- bind the scroll event to the canvas for vertical scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        # --- ensure the frame expands with the window
        self.home_frame.grid_rowconfigure(2, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Home frame - Button frame
        # --- button_frame inside the parent container (self.home_frame)
        self.button_frame = customtkinter.CTkFrame(self.home_frame, fg_color="transparent")
        self.button_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Home frame - Button frame - "Edit Save Path" button
        self.edit_save_path_button = customtkinter.CTkButton(self.button_frame, text="Edit Save Path",
                                                             command=self.show_settings_frame, width=60)
        self.edit_save_path_button.grid(row=0, column=0, padx=10, pady=5)

        # Home frame - Button frame - "Move to Top" button
        self.move_to_top_button = customtkinter.CTkButton(self.button_frame, text="Move to Top",
                                                          command=self.move_to_top, width=60, state="disabled")
        self.move_to_top_button.grid(row=0, column=1, padx=10, pady=5)

        # Home frame - Button frame - "Move Up" button
        self.move_up_button = customtkinter.CTkButton(self.button_frame, text="Move Up", command=self.move_up,
                                                      width=70, state="disabled")
        self.move_up_button.grid(row=0, column=2, padx=10, pady=5)

        # Home frame - Button frame - "Move Down" button
        self.move_down_button = customtkinter.CTkButton(self.button_frame, text="Move Down", command=self.move_down,
                                                        width=70, state="disabled")
        self.move_down_button.grid(row=0, column=3, padx=10, pady=5)

        # Home frame - Button frame - "Move to Bottom" button
        self.move_to_bottom_button = customtkinter.CTkButton(self.button_frame, text="Move to Bottom",
                                                             command=self.move_to_bottom, width=60, state="disabled")
        self.move_to_bottom_button.grid(row=0, column=4, padx=10, pady=5)

        # Home frame - "Merge" button
        self.merge_button = customtkinter.CTkButton(self.home_frame, text="Merge", command=self.merge_pdfs, height=42,
                                                    fg_color=("orange", "orange"),
                                                    text_color=("black", "black"),
                                                    hover_color=(self.BUTTON_HOVER_COLOR, self.BUTTON_HOVER_COLOR))
        self.merge_button.grid(row=5, column=0, padx=10, pady=20)

        # Home frame - Home footer frame
        self.home_footer_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent", height=28, bg_color="transparent")
        self.home_footer_frame.grid(row=6, column=0, padx=20, pady=(0, 15), sticky="sew")
        # --- configure the column to expand with the window for proper alignment
        self.home_frame.grid_rowconfigure(6, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Home frame - Home footer frame - status bar
        # --- label to display the current value of save_to_path_entry
        self.save_to_path_label = customtkinter.CTkLabel(self.home_footer_frame, text="Save to:    "+self.default_path)
        self.save_to_path_label.place(x=10, y=-5)

        # END OF Home frame
        # -------------------------------------------------------------------------

        # Guide frame
        self.guide_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.guide_frame.grid_columnconfigure(0, weight=1)

        # Guide frame - Large Banner Ad Slot
        self.guide_frame_large_image_label = customtkinter.CTkLabel(self.guide_frame, text="",
                                                                   image=self.large_banner_image)
        self.guide_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=0, pady=(0, 10))

        # END OF Guide frame
        # -------------------------------------------------------------------------

        # Help frame
        self.help_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.help_frame.grid_columnconfigure(0, weight=1)

        # Help frame - Large Banner Ad Slot
        self.help_frame_large_image_label = customtkinter.CTkLabel(self.help_frame, text="",
                                                                    image=self.large_banner_image)
        self.help_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=0, pady=(0, 10))

        # END OF Guide frame
        # -------------------------------------------------------------------------

        # Settings frame
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid_columnconfigure(0, weight=1)

        # Settings frame - Large Banner Ad Slot
        self.settings_frame_large_image_label = customtkinter.CTkLabel(self.settings_frame, text="",
                                                                   image=self.large_banner_image)
        self.settings_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=0, pady=(0, 10))

        # Settings frame - Text title
        self.settings_frame_text_label = customtkinter.CTkLabel(self.settings_frame, text="Settings",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.settings_frame_text_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 10), sticky="w")

        # Settings frame - Entry save_to_path_entry
        # --- with the default value as the desktop path (self.default_path)
        self.save_to_path_entry = customtkinter.CTkEntry(self.settings_frame, width=400)
        self.save_to_path_entry.insert(0, self.default_path)
        self.save_to_path_entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        # --- configure the column to expand with the window
        self.settings_frame.grid_columnconfigure(0, weight=1)

        # Settings frame - "Select Folder" button
        self.select_folder_button = customtkinter.CTkButton(self.settings_frame, text="Select Folder", command=self.select_folder)
        self.select_folder_button.grid(row=2, column=1, padx=20, pady=10)

        # Settings frame - settings_button_frame
        self.settings_button_frame = customtkinter.CTkFrame(self.settings_frame, fg_color="transparent")
        self.settings_button_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Settings frame - settings_button_frame - "Reset Folder" button
        self.reset_folder_button = customtkinter.CTkButton(self.settings_button_frame, text="Reset", command=self.reset_folder)
        self.reset_folder_button.grid(row=0, column=0, padx=(0, 10), pady=10)

        # # Settings frame - settings_button_frame - "Go to Merge" button
        self.go_home_button = customtkinter.CTkButton(self.settings_button_frame, text="Back to Home", command=self.show_home_frame,
                                                      fg_color=("orange", "orange"),
                                                      text_color=("black", "black"),
                                                      hover_color=(self.BUTTON_HOVER_COLOR, self.BUTTON_HOVER_COLOR))
        self.go_home_button.grid(row=0, column=1, padx=10, pady=10)
        # END OF Settings frame
        # -------------------------------------------------------------------------

        # -------------------------------------------------------------------------
        # select default frame
        self.select_frame_by_name("home_frame")

        # to hold selected files
        self.selected_files = []

        # to hold table rows
        self.table_rows = []

        # to hold status of active row
        self.active_row_index = None

    # --------------------------------------------------
    # main window
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home_frame" else "transparent")
        self.guide_button.configure(fg_color=("gray75", "gray25") if name == "guide_frame" else "transparent")
        self.help_button.configure(fg_color=("gray75", "gray25") if name == "about_frame" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings_frame" else "transparent")

        # show selected frame
        if name == "home_frame":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "guide_frame":
            self.guide_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.guide_frame.grid_forget()

        if name == "about_frame":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()

        if name == "settings_frame":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home_frame")

        # refresh status bar at bottom
        self.update_save_to_path_label()

    def guide_button_event(self):
        self.select_frame_by_name("guide_frame")

    def help_button_event(self):
        self.select_frame_by_name("about_frame")

    def settings_button_event(self):
        self.select_frame_by_name("settings_frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def show_settings_frame(self):
        # Switch to settings_frame
        # Hide the current frame (for example, self.home_frame)
        self.home_frame.grid_forget()

        # Show the settings_frame
        self.settings_frame.grid(row=0, column=1, sticky="nsew")

    def show_home_frame(self):
        # Switch to settings_frame
        # Hide the current frame (for example, self.home_frame)
        self.settings_frame.grid_forget()

        # Show the settings_frame
        self.home_frame.grid(row=0, column=1, sticky="nsew")

        self.update_save_to_path_label()

    # --------------------------------------------------
    # home_frame
    def choose_file(self):
        # Open file dialog to choose multiple PDFs
        filetypes = [('PDF files', '*.pdf')]
        selected_files = filedialog.askopenfilenames(title="Select PDFs", filetypes=filetypes)

        if selected_files:
            self.selected_files.extend(selected_files)  # Add multiple files to the list
            self.update_table()

    def _on_mousewheel(self, event):
        # Method to handle the mouse wheel scrolling
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

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

        # Update button states based on table content
        self.update_button_states()

    def set_active_row(self, index):
        # Mark the clicked row as active by saving the index
        self.active_row_index = index
        # print(f"Active row: {self.active_row_index}")

    def select_all(self):
        # Method to select all checkboxes
        for row in self.table_rows:
            checkbox = row.winfo_children()[0]  # Assuming the checkbox is the first widget in each row
            checkbox.select()  # Select the checkbox

    def unselect_all(self):
        # unselect all checkboxes
        for row in self.table_rows:
            checkbox = row.winfo_children()[0]  # Assuming the checkbox is the first widget in each row
            checkbox.deselect()  # Unselect the checkbox

    def remove_selected(self):
        # remove selected rows
        # Iterate through the table rows and remove the selected ones
        to_remove = []
        for index, row in enumerate(self.table_rows):
            checkbox = row.winfo_children()[0]  # Assuming the checkbox is the first widget in each row
            if checkbox.get() == 1:  # Check if the checkbox is selected
                to_remove.append(index)

        # Remove rows from bottom to top to avoid index shifting issues
        for index in reversed(to_remove):
            self.table_rows[index].grid_forget()
            self.table_rows.pop(index)
            self.selected_files.pop(index)

        # Update table
        self.update_table()

        # Update button states based on table content
        self.update_button_states()

    def move_up(self):
        if self.active_row_index is not None and self.active_row_index > 0:
            # Swap the files in the list and update the table
            self.selected_files[self.active_row_index], self.selected_files[self.active_row_index - 1] = \
                self.selected_files[self.active_row_index - 1], self.selected_files[self.active_row_index]
            self.active_row_index -= 1
            self.update_table()

            # keep the selected row ticked
            # Re-select the active row and check its checkbox after moving
            self.set_active_row(self.active_row_index)
            self.table_rows[self.active_row_index].winfo_children()[0].select()  # Re-check the checkbox

    def move_down(self):
        if self.active_row_index is not None and self.active_row_index < len(self.selected_files) - 1:
            # Swap the files in the list and update the table
            self.selected_files[self.active_row_index], self.selected_files[self.active_row_index + 1] = \
                self.selected_files[self.active_row_index + 1], self.selected_files[self.active_row_index]
            self.active_row_index += 1
            self.update_table()

            # keep the selected row ticked
            # Re-select the active row and check its checkbox after moving
            self.set_active_row(self.active_row_index)
            self.table_rows[self.active_row_index].winfo_children()[0].select()  # Re-check the checkbox

    def move_to_top(self):
        # move the selected line to the top of the table
        if self.active_row_index is not None:
            selected_file = self.selected_files.pop(self.active_row_index)  # Remove the selected item
            self.selected_files.insert(0, selected_file)  # Insert it at the top
            self.active_row_index = 0  # Update the active row index
            self.update_table()  # Update the table

            # keep the selected row ticked
            # Re-select the active row and check its checkbox after moving
            self.set_active_row(self.active_row_index)
            self.table_rows[self.active_row_index].winfo_children()[0].select()  # Re-check the checkbox

    def move_to_bottom(self):
        # move the selected line to the bottom of the table
        if self.active_row_index is not None:
            selected_file = self.selected_files.pop(self.active_row_index)  # Remove the selected item
            self.selected_files.append(selected_file)  # Insert it at the bottom
            self.active_row_index = len(self.selected_files) - 1  # Update the active row index
            self.update_table()  # Update the table

            # keep the selected row ticked
            # Re-select the active row and check its checkbox after moving
            self.set_active_row(self.active_row_index)
            self.table_rows[self.active_row_index].winfo_children()[0].select()  # Re-check the checkbox

    def update_button_states(self):
        if len(self.table_rows) > 0:
            # Enable all buttons
            self.select_all_button.configure(state="normal")
            self.unselect_all_button.configure(state="normal")
            self.remove_button.configure(state="normal")
            self.move_up_button.configure(state="normal")
            self.move_down_button.configure(state="normal")
            self.move_to_top_button.configure(state="normal")
            self.move_to_bottom_button.configure(state="normal")
            # self.merge_button.configure(state="normal")
        else:
            # Disable all buttons
            self.select_all_button.configure(state="disabled")
            self.unselect_all_button.configure(state="disabled")
            self.remove_button.configure(state="disabled")
            self.move_up_button.configure(state="disabled")
            self.move_down_button.configure(state="disabled")
            self.move_to_top_button.configure(state="disabled")
            self.move_to_bottom_button.configure(state="disabled")
            # self.merge_button.configure(state="disabled")

    # --------------------------------------------------
    # settings_frame
    def select_folder(self):
        # open file dialog and set the selected folder path
        folder_selected = filedialog.askdirectory(title="Select Folder")
        if folder_selected:  # If a valid folder is selected
            self.save_to_path_entry.delete(0, "end")  # Clear current entry content
            self.save_to_path_entry.insert(0, folder_selected)  # Set the new folder path
        self.update_save_to_path_label()

    def reset_folder(self):
        # reset the path to default path (as Desktop)
        # default_path = os.path.join(os.path.expanduser("~"), "Desktop")  # Get the Desktop path again
        default_path = self.desktop_path  # Get the Desktop path again
        self.save_to_path_entry.delete(0, "end")  # Clear current entry content
        self.save_to_path_entry.insert(0, default_path)  # Reset to default path
        self.update_save_to_path_label()

    def update_save_to_path_label(self):
        # update the label whenever the value of save_to_path_entry changes
        self.save_to_path_label.configure(text="Save to:    "+self.save_to_path_entry.get())

    # --------------------------------------------------
    # core business
    def merge_pdfs(self):
        input_pdfs = self.selected_files

        if len(input_pdfs) <= 0:
            messagebox.showwarning("Warning", "Please choose PDF file(s) first!")
            return

        merger = PdfWriter()

        try:
            # Process each PDF and merge the pages
            for pdf in input_pdfs:
                with open(pdf, 'rb') as file:
                    reader = PdfReader(file)
                    print(f"[INFO] {pdf} loaded.")
                    for page in reader.pages:
                        merger.add_page(page)

            # Get the current save path from the entry
            current_path = self.save_to_path_entry.get()

            # Check if the selected path exists
            if not os.path.exists(current_path):
                raise FileNotFoundError(f"The path {current_path} does not exist.")

            # Save merged PDF to the specified path
            merged_pdf_name = "merged_output.pdf"
            save_path = os.path.join(current_path, merged_pdf_name)
            with open(save_path, 'wb') as merged_file:
                merger.write(merged_file)

            print(f"Merged PDF saved to {save_path}")
            messagebox.showinfo("Message", f"Saved {merged_pdf_name} to {save_path}")

        except FileNotFoundError as e:
            # If the path doesn't exist, show an error dialog
            messagebox.showwarning("Invalid Path", str(e))

            # Auto-reset
            # self.reset_folder()

            # switch to settings panel
            self.show_settings_frame()

        except Exception as e:
            # Catch any other exceptions and show a generic error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = App()
    app.mainloop()

