# Get N from the user
N = int(input("Enter the number of characters to read from the end of the file: "))

try:
    with open("q4_story.txt", "r", encoding="utf-8") as file:  # Open with the appropriate encoding
        file.seek(0, 2)  # Move to the end of the file to get its size
        file_size = file.tell()  # Get the total file size

        # Move back by N characters from the end
        file.seek(max(0, file_size - N * 4))  # Adjust to potentially read enough bytes for multibyte characters

        # Read to the end and handle potential multibyte characters
        content = file.read()[-N:]  # Safely get the last N characters from the read content
        print("Last", N, "characters of the file:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid number of characters entered.")
