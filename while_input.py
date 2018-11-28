#move from one list to another based on comparison
v_uc_users = ['alice','brian','candace','tommy','fred']
v_chk_list = ['brian','fred']
v_cf_users = []

while v_uc_users:
    v_cur_user = v_uc_users.pop()
    if v_cur_user in v_chk_list:
        v_cf_users.append(v_cur_user)
        print("User : " + v_cur_user + " verified.")
    else:
        print("User : " + v_cur_user + " not verified.")


#print("\nConfirmed User List")
#print("===================")
#for cf_user in sorted(v_cf_users):
    #print(cf_user.title())

#collect user input into a dictionary and print results
#v_responses = {}
#v_status = True

#while v_status:
    #v_names = input("What is your name? -> ")
    #v_mtns = input("What mountain do you want to climb?-> ")
    #v_responses[v_names] = v_mtns
    #v_repeat = " "
    #while v_repeat.upper() not in ['Y','N']:
        #v_repeat = input("Is there another person Y/N -> ")
        #if v_repeat.upper() == 'N':
            #v_status = False
#print("---- Results ------")
#for v_name, v_mtn in sorted(v_responses.items()):
    #print(v_name.title() + " would like to climb " + v_mtn.title())

