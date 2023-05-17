def checkEmailInput(): 
    letterString = "abcdefghijklmnopqrstuvwxyz" 
    letterList = list(letterString) 
    localCharacterString = "!#$%&?/|[{<]}>^`'\"*+=~," 
    localCharacterList = list(localCharacterString) 
    domainCharacterString = "!#$%&?/|[{<]}>^`'\"*+=~,_"
    domainCharacterList = list(domainCharacterString) 
    emailString = input("Please enter an email address to check: ") 
    emailList = list(emailString.lower()) 
    if len(emailList) > 2 and len(emailList) < 255: 
        pass 
    else: 
        print("\nThe length of an email address must be between 3 and 254 characters.") 
        return checkEmailInput() 
    if emailList[0] in letterList: 
        pass 
    else: 
        print("\nThe address you have entered does not start with a letter.") 
        return checkEmailInput() 
    atCounter = emailList.count("@") 
    if atCounter == 1: 
        pass 
    elif atCounter == 0: 
        print("\nThe address you have entered does not contain the @ character.") 
        return checkEmailInput() 
    else: 
        print("\nThe address you have entered contains more than one @ character.") 
        return checkEmailInput() 
    atPosition = emailList.index("@") 
    localPart = emailList[:atPosition] 
    domainPart = emailList[atPosition + 1:] 
    domainLength = len(domainPart) 
    for localListItem in localPart: 
        if localListItem not in localCharacterList: 
            pass 
        else: 
            print("\nThe local part contains prohibited special characters.") 
            return checkEmailInput() 
    dotCounter = domainPart.count(".") 
    if dotCounter >= 1: 
        pass 
    else: 
        print("\nThe domain part does not contain a period.") 
        return checkEmailInput() 
    if domainPart[0] != ".": 
        pass 
    else: 
        print("\nThe domain part starts with a period.") 
        return checkEmailInput() 
    if domainPart[domainLength - 1] != ".": 
        pass 
    else: 
        print("\nThe domain part ends with a period.") 
        return checkEmailInput()
    for domainListItem in domainPart: 
        if domainListItem not in domainCharacterList: 
            pass 
        else: 
            print("\nThe domain part contains prohibited special characters.") 
            return checkEmailInput() 
    print("\nThe address", emailString, "is a valid email address!")

def main(): 
    print("\nEmail parser") 
    emailChecker = checkEmailInput() 

main() 
