def func1(x):
    main = []
    for i in range(0,x):
        y = input()
        main.append(y)
    print("address operator argument1 argument2")
    for i in range(0,x):
        q = main[i]
        if q[0] not in res:
            res.append(q[0])
        e = func2(q[2])
        if (len(q)>3):
            r = func2(q[4])
            print("    (",i,")","    ",q[3],"    ",e,"    ",r)
        else:
            print("    (",i,")","    ",q[1],"    ",e,"    ",)
    print(main)
    print(res)

def func2(q):
    try:
        z = res.index(q)
        return(z)
    except:
        return(q)

x = int(input("enter the number of productions: "))
res = []
func1(x)