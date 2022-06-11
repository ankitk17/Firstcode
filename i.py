inp_lst1 = []
inp_lst2 = []
n = int(input("Enter number of elements for 1st list : "))
for i in range(0, n):
    element_type = int(input(f'datatype for element {i+1}(type 1 for int, 2 for float, 3 for complex, 4 for list, 5 for tuple, 6 for string)'))
    if (element_type == 1):
        element1 = input(f'Enter the element {i+1}: ')
        element1 = int(element1)
        inp_lst1.append(element1)
    elif (element_type == 2):
        element1 = input(f'Enter the element {i+1}: ')
        element1 = float(element1)
        inp_lst1.append(element1)
    elif (element_type == 3):
        element1 = input(f'Enter the element {i+1}: ')
        element1 = complex(element1)
        inp_lst1.append(element1)
    elif (element_type == 4):
        o = int(input("Enter number of elements for inner list : "))
        inner_list = []
        for k in range(o):
            element = int(input(f'Enter the element {k+1}: '))
            inner_list.append(element)
        inp_lst1.append(inner_list)
    elif (element_type == 5):
        a = int(input("Enter number of elements for inner tuple : "))
        inner_tupple = []
        for b in range(a):
            element6 = int(input(f'Enter the element {b+1} '))
            inner_tupple.append(element6)
        inp_lst1.append(tuple(inner_tupple))
    else:
        element1 = input(f'Enter the element {i+1}: ')
        element1 = str(element1)
        inp_lst1.append(element1)
p = int(input("Enter number of elements for 2nd list : "))
for j in range(0, p):
    element_type = int(input(f'datatype for element {j+1}(type 1 for int, 2 for float, 3 for complex, 4 for list, 5 for tuple, 6 for string)'))
    if (element_type == 1):
        element2 = input(f'Enter the element {j+1}: ')
        element2 = int(element2)
        inp_lst2.append(element2)
    elif (element_type == 3):
        element2 = input(f'Enter the element {j+1}: ')
        element2 = complex(element2)
        inp_lst2.append(element2)
    elif (element_type == 2):
        element2 = input(f'Enter the element {j+1}: ')
        element2 = float(element2)
        inp_lst2.append(element2)
    elif (element_type == 4):
        t = int(input("Enter number of elements for inner list : "))
        inner_list2 = []
        for r in range(t):
            element5 = int(input(f'Enter the element {r+1}: '))
            inner_list2.append(element5)
        inp_lst2.append(inner_list2)
    elif (element_type == 5):
        c = int(input("Enter number of elements for inner tuple : "))
        inner_tupple1 = []
        for d in range(c):
            element7 = int(input(f'Enter the element {d+1}: '))
            inner_tupple1.append(element7)
        inp_lst2.append(tuple(inner_tupple1))
    else:
        element2 = input(f'Enter the element {j+1}: ')
        element2 = str(element2)
        inp_lst2.append(element2)
print(inp_lst1)
print(inp_lst2)
e = int(input('Enter the number of elements which are same'))
count = 0
for x in range(len(inp_lst1)):
    for y in range(len(inp_lst2)):
        if (inp_lst1[x] == inp_lst2[y]):
            count = count + 1
if (count>=e):
    print('True')
else:
    print('False')
