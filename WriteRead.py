# Read a file and save lines that contain a specific word into a new file 

word = "ERROR"

with open("server_log.txt", "r" , encoding="utf-8") as file, \
    open("errors_only.txt", "w", encoding="utf-8") as new_file:
    for line in file:
        if word in line:
            print(line.strip())
            new_file.write(line)