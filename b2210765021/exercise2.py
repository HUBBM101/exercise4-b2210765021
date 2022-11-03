mail=input("Pleas enter an e-mail:")
sayac=0
def valid(mail):
    global sayac
    for i in mail:
        if i in "@":
            sayac+=1
        elif i in ".":
            sayac+=1
    if sayac>1:
        return "This is a valid e-mail."
    else:
        return "This is invalid e-mail. Your e-mail must contain '@' and '.'"
y=valid(mail)
print(y)
