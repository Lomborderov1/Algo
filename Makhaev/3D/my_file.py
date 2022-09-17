with open('my_file.txt','r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')
    item = int(second_line[7])
    print(item)