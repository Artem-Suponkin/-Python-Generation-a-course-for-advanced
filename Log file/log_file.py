#A text file is available to you logfile.txt with information about the time the user logs in and out of the system.
# Each line of the file contains three values separated by commas and a space character: user name, login time, exit time, where the time is specified in 24-hour format.
#
#Write a program that creates a file output.txt and outputs to it the names of all users (without changing the order) who have been online for at least an hour.




with open('logfile.txt', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
    lst = [i.strip().split() for i in file.readlines()]
    lst1 = map(lambda x: f'{x[0]} {x[1][:-1]}', filter(lambda x: ((int(x[3].split(':')[0]) * 60 + int(x[3].split(':')[1])) - (int(x[2].split(':')[0]) * 60 + int(x[2].split(':')[1].replace(',', '')))) >= 60, lst))
    for i in lst1:
        print(i, file=output)



