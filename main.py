
userstring = ""
prompt = ""
while (prompt != "stop"):
    prompt = input()
    if (prompt == "stop"):
        userstring = userstring
    else:
        userstring = userstring + prompt + " "
print(userstring)