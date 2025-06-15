def read(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copyFile(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        
        with open(destination, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"Copied content from {source} to {destination}.")
    except FileNotFoundError:
        print(f"The file {source} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

with open('firstFile.txt', 'w') as file:
    file.write("This is the content of the firstFile.txt.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")
print("Reading firstFile.txt:")
read('firstFile.txt')
copyFile('firstFile.txt', 'firstCopy.txt')
print("\nReading firstCopy.txt:")
read('firstCopy.txt')
