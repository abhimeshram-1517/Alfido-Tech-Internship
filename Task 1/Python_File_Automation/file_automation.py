import os
import csv
import shutil


# 1. READ A TEXT FILE

try:
    # Open input.txt in read mode ("r")
    with open("input.txt", "r") as file:
        content = file.read()

    # Display the content of the text file
    print("----- TEXT FILE CONTENT -----")
    print(content)

except FileNotFoundError:
    # This message is displayed if input.txt does not exist
    print("Error: input.txt was not found.")

# 2. WRITE TO A TEXT FILE

try:
    # Open output.txt in write mode ("w")
    # If the file does not exist, Python creates it
    with open("output.txt", "w") as file:
        file.write("This file was created using Python.\n")
        file.write("Python file writing is successful.")

    print("\noutput.txt created successfully.")

except Exception as e:
    # Handle any error while writing the file
    print("Error while writing the text file:", e)

# 3. READ A CSV FILE

try:
    print("\n----- CSV FILE CONTENT -----")

    # Open students.csv in read mode
    with open("students.csv", "r") as file:

        # csv.reader reads the CSV file row by row
        reader = csv.reader(file)

        # Print every row from the CSV file
        for row in reader:
            print(row)

except FileNotFoundError:
    # This message appears if students.csv does not exist
    print("Error: students.csv was not found.")

except Exception as e:
    # Handle other CSV errors
    print("Error while reading CSV:", e)

# 4. WRITE TO A CSV FILE

try:
    # Create a new CSV file
    with open("new_students.csv", "w", newline="") as file:

        # Create a CSV writer
        writer = csv.writer(file)

        # Write the column headings
        writer.writerow(["Name", "Age", "Course"])

        # Write student information
        writer.writerow(["Neha", 21, "Python"])
        writer.writerow(["Arjun", 22, "Web Development"])

    print("\nnew_students.csv created successfully.")

except Exception as e:
    # Handle errors while creating the CSV file
    print("Error while writing CSV:", e)

# 5. RENAME A FILE

try:
    # Create a sample file that we will rename
    with open("old_file.txt", "w") as file:
        file.write("This file will be renamed.")

    # Rename old_file.txt to renamed_file.txt
    os.rename("old_file.txt", "renamed_file.txt")

    print("File renamed successfully.")

except Exception as e:
    # Handle errors during renaming
    print("Error while renaming:", e)

# 6. MOVE A FILE

try:
    # Create a sample file to move
    with open("move_me.txt", "w") as file:
        file.write("This file will be moved.")

    # Move the file into the files folder
    shutil.move("move_me.txt", "files/move_me.txt")

    print("File moved successfully.")

except Exception as e:
    # Handle errors during moving
    print("Error while moving:", e)

# 7. DELETE A FILE

try:
    # Create a sample file that will be deleted
    with open("delete_me.txt", "w") as file:
        file.write("This file will be deleted.")

    # Delete the file
    os.remove("delete_me.txt")

    print("File deleted successfully.")

except Exception as e:
    # Handle errors during deletion
    print("Error while deleting:", e)

# PROGRAM COMPLETED

print("\n----- FILE AUTOMATION COMPLETED -----")