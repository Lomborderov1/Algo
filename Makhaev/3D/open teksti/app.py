with open('my_file.txt','r') as file:
    lines = file.readlines()
    second_line = lines[11].split(' ')
    item = int(second_line[8])
    print(item)