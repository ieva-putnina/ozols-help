a = ["A","B","BC","D","B"]
s = "B"
if a.count(s) > 0:
    print(a.count(s))
    print(s+"_"+ str(a.count(s)+1))
