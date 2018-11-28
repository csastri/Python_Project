def char_counter(string):
    for char in string[::]:
        if char != ' ':
            if char not in unique:
                unique.append(char)
                charctr.append(string.count(char))
                print(char + '---' + str(string.count(char)))    
unique = []
charctr = []
char_counter('Hello World')
char_counter('Hello World')
#string = 'Hello World'
#unique = []
#charctr = []
#for char in string[::]:
    #if char != ' ':
        #if char not in unique:
            #unique.append(char)
            #charctr.append(string.count(char))
            #print(char + '---' + str(string.count(char)))
print(unique)
print(charctr)