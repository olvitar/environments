"""чтение файла и запись определенных строк в новый файл"""
file = open("text.txt") # open file 'text.txt'

bugs = []
for line in file.readlines():
	if 'bug' in line.lower():
		bugs.append(line) # add lines with 'bug' to the 'bugs' list
		
parsed_file = open("report.txt", "w") # open file 'report.txt' with WRITE permission
parsed_file.write("".join(bugs)) # add list 'bugs' to the file
parsed_file.close()
