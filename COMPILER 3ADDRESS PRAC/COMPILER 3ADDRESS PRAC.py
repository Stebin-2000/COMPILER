postfix = input("enter postfix operator:").split()
operators = ['+','-','/','*','^']
stack = []
result = ' '
str1 = ' '
count = 0
print("3-ADDRESS CODE")
for i in postfix:
    if i not in operators:
        stack.append(i)
        #print("stack = ",stack)
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        result = op2+i+op1
        str1 = 'T' + str(count)
        stack.append(str1)
        print("T", count, "=", result)
        count += 1