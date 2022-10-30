for x in range(5):
    for y in range(5-x):
        print ("* ",end = "")
    print ("\n")

for x in range(5):
    for y in range(x+1):
        print ("* ",end = "")
    print ("\n")

for x in range(5):
    s = ""
    u = ""
    for y in range(x):
        s = s+" "
    for z in range (5-x):
        u = u+"* "
    print (s+u)

for x in range(5):
    s = ""
    u = ""
    for y in range(5-x):
        s = s+" "
    for z in range (x+1):
        u = u+"* "
    print (s+u)

for x in range (5):
    s = ""
    u = ""
    for y in range(5-x):
        s = s+" "
    for z in range (x+1):
        u = u+"*"
    print (s+u)