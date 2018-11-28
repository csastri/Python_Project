def char_counter(string):
    for char in string[::]:
        if char != ' ':
            if char not in unique:
                unique.append(char)
                charctr.append(string.count(char))
                print(char + '---' + str(string.count(char)))   

f = open('C:\PYCODE\Data\Test_Data.txt')
x = f.read()
print(x)
unique = []
charctr = []
char_counter(x)

print(unique)