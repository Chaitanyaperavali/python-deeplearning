# This function validates password against database rules
# Parameter - String(Password in this case).
def validatePassword(password):

    length = len(str(password))

    #flags to validate given criteria
    n_val = -1
    sc_val = -1
    lc_val = -1
    up_val = -1
    result = ""

    #checks if length is between 6-16
    if(length >=6 and length<=16):
        # Iterates over the string and checks each condition is met.If met respective flag is changed.
        for x in password:
            val = ord(x)

            # Ascii val of character is compared and respetive flag is changed

            #number check
            if(val>=48 and val<=57):
                n_val = 1

            #Uppercase
            if(val>=65 and val<=90):
                up_val = 1

            #Lowercase
            if(val>=97 and val<=122):
                lc_val = 1

            #Specialchar
            if(x in ['$','@','!','*']):
                sc_val = 1
    else:
        result = result+"Length is not in range: 6-16\n"

    # result: results from each cretria will be appended
    if(n_val == -1):
        result = result + "Should include atleast one number\n"
    if (sc_val == -1):
        result = result + "Should include atleast one from [$@!*]\n"
    if (up_val == -1):
        result = result + "Should include atleast one Uppercase char\n"
    if (lc_val == -1):
        result = result + "Should include atleast one Lowercase char\n"

    if(result != ""):
        return result
    else:
        return "Met all criteria"

# function call to test
print(validatePassword("chaitu@!8768A"))