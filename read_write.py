#filename = 'C:/PYCode/Data/test_data.txt'
#with open(filename) as file_object:
    #for line in file_object:
        #print(line.rstrip())
        

#filename = 'C:/PYCode/Data/pi_million_digits.txt'
#with open(filename) as file_object:
    #lines = file_object.readlines()
#pi_string = ''
#for line in lines:
    #pi_string = pi_string + line.strip()
    
#print(pi_string[:50] + "...") 

#b_day = input("Enter Birthdate mmddyy format -> ")
#if b_day in pi_string:
    #print("Birthday in PI")
#else:
    #print("Birthday not in PI")


#filename = "C:/PYCode/Data/programming.txt"
#with open(filename, 'w') as file_object:
    #file_object.write("First line of Code\n")
    #file_object.write("Second line of Code\n")
    
#with open(filename, 'a') as file_object:
    #file_object.write("Third line of Code - appended\n")
    #file_object.write("Fourth line of Code - also appended\n")


#filename = "C:/PYCode/Data/guests.txt"
#vrun = True
#while vrun:
    #f_name = input("First Name -> ")
    #if f_name == 'q':
        #vrun = False
    #else:
        #l_name = input("Last Name --> ")
        #with open(filename, 'a') as file_object:
            #file_object.write(f_name + " " + l_name + "\n")

#build the pi_string from file
filename = 'C:/PYCode/Data/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()     

# accept input and search string
b_day = input("Enter Birthdate mmddyy format -> ")
v_found = pi_string.find(b_day)
print(v_found)
v_start = v_found - 2
v_end   = v_found + 9
print(pi_string[v_start:v_end])
#if b_day in pi_string:
    #print("Birthday in PI")
#else:
    #print("Birthday not in PI")