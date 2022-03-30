def func1(x):
    main = []
    for i in range(0,x):
        y = input()
        main.append(y)
    print("label operator Left Right")
    for i in range(0,x):
        q = main[i]
        if q[0] not in res:
            res.append(q[0])
        if (len(q)>3):
            print("    ",q[0],"    ",q[3],"    ",q[2],"    ",q[4])
        else:
            print("    ",q[0],"    ",q[1],"    ",q[2],"    ")
    print(main)
    print(res)

x = int(input("enter the number of 3 address code: "))
res = []
func1(x)