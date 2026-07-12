# file = open("notes.txt","r")
# content = file.read()
# print(content)
# file.close()


# from pathlib import Path

# print("Current working directory:", Path.cwd())
# print("Script directory:", Path(__file__).parent)

# file_path = Path(__file__).parent / "notes.txt"
# print("Looking for:", file_path)
# print("Exists?", file_path.exists())

# with open(file_path, "r") as file:
#     print(file.read())



file = open("file_handling/notes.txt", "r")

content = file.read()
print(content)

file.close()