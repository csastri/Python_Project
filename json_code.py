##accept user input and create a json file with that file name
#import json
#vrun = True
#while vrun:
    #user_name = input("Enter your name or q to quit -> ")
    #if user_name == 'q':
        #vrun = False
    #else:
        #file_name = "C:/PYCODE/Data/" + user_name.strip() + ".json"
        #with open(file_name, 'a') as f_obj:
            #json.dump(user_name, f_obj)
#print("Good Bye!")

#accept user input and create a json file multiple values CSV
#import json
#file_name = "C:/PYCODE/Data/user_names.json"
#vrun = True
#while vrun:
    #user_name = input("Enter your name or q to quit -> ")
    #if user_name == 'q':
        #vrun = False
    #else:
        #with open(file_name, 'a') as f_obj:
            #json.dump(user_name, f_obj)
#print("Good Bye!")

#check if input value is in the file created
#print if found, print and add to list if not
import json
#check if user exists
def check_user():
    try:
        with open(file_name) as f_obj:
            user_value = json.load(f_obj)
    except FileNotFoundError:
        print(file_name + " File Not found")
        return None
    else:
        return user_value
    
#add user 
def add_user():
    with open(file_name, 'w') as f_obj:
        json.dump(user_name, f_obj)

vrun = True
while vrun:
    user_name = input("Enter your name or q to quit -> ")
    if user_name == 'q':
        vrun = False
    else:
        file_name = "C:/PYCODE/Data/" + user_name.strip() + ".json"
        print(file_name)
        check_user()
        print ("User Name-->" + user_name)
        if user_value == "":
            add_user()
            print("Hi, " + user_name + " you are new!")            
        else:
            print("Hello " + user_value + " welcome back")
print("Good Bye!")