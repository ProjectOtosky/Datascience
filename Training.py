
# x = 20
# y = 30
# mynumber = 20.234
# rounded_num = round(mynumber, 2)
# print(rounded_num)
# num = 22
# den = 7
# # pi = num/den
# # print(pi)
# # rounded_num = round(pi, 3)
# # print(rounded_num)
# name = 'Elson'
# # phone = 7035034302 * 6
# # print(phone)
# surname = 'John'
# fullname = name + " " + surname
# print(fullname)
# day = '20'
# month = 'may'
# year = '2019'
# print(day + ' ' + month + ' ' + year)
# pi = 22/7
# round_pi = round(pi, 2)
# statement = "pi is " + str(round_pi)
# print(statement)
# x = "123456"
# int(x)
# print(int(x))
# # rounded_num = round(statement, 3)

# name = input ("What is your name")
# print(name)
# print(name [0], [2], [6])
# print(name [-1])
# print(name[0:7])
# word = input("Any word of your chioce ")
# length = input("what is the length of the word ")
# half_length = int(int(length)/2)
# print(word[half_length:])
# half_length = int(int(length)/2) - 1
# two_chars_up = half_length + 2
# first_two = word[0:2]
# last_two = word[-2:]
# mid_point = word[half_length:two_chars_up]
# statement = first_two + mid_point + last_two
# print(statement)
# print(word[::-1])
# mod = 6 % 4
# print(mod)
# x = 20
# x = x+1
# print(x)
# a = int(input("a number of your choice"))
# b = input("an even number")
# b = int(b)
# formular_c = (a**2 + b**2)**0.5
# print(a)
# print(b)
# print(formular_c)

# round_number = round(formular_c, 3)
# print(round_number)

# a = int(input ("odd number"))
# b = int(input ("even number"))
# c = int(input ("any number"))
# print(a)
# print(b)
# print(c)
# x1 = -b + ((b**2)-(4*a*c))**0.5/2*a
# x2 = -b - ((b**2)-(4*a*c))**0.5/2*a
# print(x1)
# print(x2)

# statement = f'x is either {x1} or {x2}'
# print(statement)
# round_number = round(x1, 2) 

# print(word[0:2], word[4:6], word[10:])
# first_2letters = int(int(length):2)
# print(word[first_2letters])



# word = input('Please enter word : ')
# reversed_word = word [::-1]
# print(f'{word} is a palindrome : {word == reversed_word}')

# a = 1
# b = 2
# c = 3
# d = 4
# x = (a*d) + (b*c)
# y = (b*d)
# print(f'{x}/{y}')

# fraction = input('Please enter a fraction in the format "a/b+c/d" : ')
# splitted_fraction = fraction.split('+')
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]

# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')

# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# print(splitted_frac1, splitted_frac2)
# print(a + b + c + d)

# Dob = input('Please enter your date of birth in this format 2019-11-18')
# splitted_Dob = Dob.split('-')
# Year = splitted_Dob[0]
# print(Year)
# print(Year[0], Year[1], Year[2], Year[3])

# print(1,2,3...sep ='\n')
# file = open('mydata.csv', 'w')
# print('S/No', 'First Name', 'Surname', 'Sex', 'Age', 'State', 'Due', file = file, sep = ",")
# Candidates = input('Using this format S/No-First Name-Surname-Sex-Age-State-Due : ')
# splitted_Candidates = Candidates.split('-')
# x = splitted_Candidates[0]
# y = splitted_Candidates[1]
# z = splitted_Candidates[2]
# a = splitted_Candidates[3]
# b = splitted_Candidates[4]
# c = splitted_Candidates[5]
# d = splitted_Candidates[6]

# print(x, y, z, a, b, c, d, file = file, sep = ",")
# print('ade', 20, 'Osun_state', 20000, file = file, sep = ",")

# filename = "Barack.txt"
# mode = "r"
# data = open(filename, mode)

# Biography = data.read()
# print(Biography)

# filename = "file.csv"
# mode = "w"
# file = open(filename, mode)

# text = 'Obama wrote his first book and saw it published'
# file.write(text)
# r = range(20,60)
# print(r)
# print(type(r))
# print(list(r))
# print(list(r))

# r1 = range(20,60,2)
# print(r)
# print(r1)
# print(list(r1))

# print(list(reversed(r1)))

# x = [1,2,5,3,10,1,0,4]
# print(sorted(x))
# # print(sorted(reversed(x)))
# print(reversed(sorted(x)))
# # print(sorted(x, reverse = True))

# y = list("Abimbolami")
# print(sorted(y))
# my_list = ['seed', 'bae', 'a', 'checked', 'print']
# print(sorted(my_list, key = len))
# print(sorted(my_list))
# print(sorted(my_list, key = len, reverse = True))
# print(sorted(my_list, key = len, reverse = False))

# dict
# my_dict = dict(a = 20, b = 30)
# print(my_dict)
# print(my_dict['a'])

# map
# nums = [1,2,3,4,5,6]
# mapped = map(lambda x : x*2, nums)
# print(list(mapped)) 
# names = ['ade', 'john', 'shola']
# mapped = map(lambda x :'Mr' + x, names)
# print(list(mapped))

# ANY

# word = 'sharp'.upper()
# # print(any(word))

# print(word)
# i = [1,3,1,2,2,4]
# mean = sum(i)/len(i)
# mapped = list(map(lambda x : (x-mean)**2, i))
# print(mapped)
# variance = sum(mapped)/(len(mapped)-1)
# print(variance)

# a = ['Mr', '/Mrs']
# print(''.join(a))

# filename = "Lyrics.txt"
# mode = "r"
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics)


# # print(lyrics.find('Lupita'))
# print(lyrics.count('love'))
# name = [('Bola', 'f'), ('Shola', 'f'), ('Segun', 'm'), ('John', 'm')]
# # mapped1= map(lambda x :'Mr' + x, names[1] = 'm') 
# mapped2 = map(lambda x : 'Mrs' + x, name[1] = 'f')
# print(list(mapped2))

Candy = input('The total number of Candy to be shared')
Shared_candy = int('Candy/3')
Crushed_Candy = (Candy % 3)
print(Shared_candy)
print(Crushed_Candy)


# nums = range(1,6)
# print(list(nums))


