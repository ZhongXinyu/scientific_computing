from itertools import permutations
from itertools import product

number_list=[1,2,3,4]
def display_formula(operation_list,origin_list):
    display=""
    for i in range (0,3):
        display+=str(origin_list[i])+operation_list[i]
    display+=str(origin_list[3])
    return (display)
def calculate(operation_list,operation_index,number_list):
    a=number_list[operation_index]
    b=number_list[operation_index+1]
    operation=operation_list[operation_index]
    if operation=="+":
        ab=a+b
    elif operation=="-":
        ab=a-b
    elif operation=="*":
        ab=a*b
    elif operation=="/":
        ab=a/b
    del(number_list[operation_index:operation_index+2])
    del(operation_list[operation_index])
    number_list.insert(operation_index, ab)
    return (operation_list,operation_index-1,number_list)



for number_element in permutations(number_list):
    for operation_element in product('+-*/', repeat=3):
        number_list=list(number_element)
        operation_list=list(operation_element)
        M_D=[]
        i=0
        while i < len(operation_list):
            if operation_list[i] in ["*","/"]:
                operation_list,i,number_list = calculate(operation_list,i,number_list)
            i+=1
        i=0
        while i < len(operation_list):
            operation_list,i,number_list = calculate(operation_list,i,number_list)
            i+=1
        if number_list[0]==24:
            print (display_formula(list(operation_element),list(number_element)))

                

