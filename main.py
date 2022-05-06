import os

file_path = input("Please enter the directory you would like to save the file: ")

if not os.path.exists(file_path):
    os.makedirs(file_path)

file_name = input("Please enter the file name: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
number = input("Please enter your number: ")

w_file = open(os.path.join(file_path, file_name), 'w+')
w_file.write(name + ", " + address + ", " + number)
w_file.close()

r_file = open(os.path.join(file_path, file_name), 'r')
line = r_file.readline()
r_file.close()

print(line)
