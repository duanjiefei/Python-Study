count = 0
while count < 3:
    user_name = input("please input the username :")
    pass_word = input("please input the password :")
    if user_name == "djf" and pass_word == "129824":
        print ("login sucess!!!")
        break
    else:
        print ("the user_name or password is error......")
    count = count + 1

print ("the programe is over....")
