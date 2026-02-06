doc={}
for i in range(int(input())):
    cmd=input().split()
    if cmd[0]=="set":
        doc[cmd[1]]=cmd[2]
    else:
        if cmd[1] in doc:
            print(doc[cmd[1]])
        else:
            print("KE: no key",cmd[1],"found in the document")