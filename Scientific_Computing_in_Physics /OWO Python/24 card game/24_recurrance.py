import random

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

k=24

def display_formula(operation_history,origin_list):
    display=f'{origin_list[0]}'
    i=0
    while i<3:
        if operation_history[i]==0:
            display=f'({display}+{origin_list[i+1]})'
        elif operation_history[i]==1:
            display=f'-({display}+{origin_list[i+1]})'
        elif operation_history[i]==2:
            display=f'({display}-{origin_list[i+1]})'
        elif operation_history[i]==3:
            display=f'({origin_list[i+1]}-{display})'
        elif operation_history[i]==4:
            display=f'({display}*{origin_list[i+1]})'
        elif operation_history[i]==5:
            display=f'-({display}*{origin_list[i+1]})'
        elif operation_history[i]==6:
            display=f'({display}/{origin_list[i+1]})'
        elif operation_history[i]==7:
            display=f'({origin_list[i+1]}/{display})'
        elif operation_history[i]==8:
            display=f'-({display}/{origin_list[i+1]})'
        elif operation_history[i]==9:
            display=f'-({origin_list[i+1]}/{display})'
        i+=1
    return (display)

def two_number_all_solution(number_list,operation_history,origin_list):
    a=number_list[0]
    b=number_list[1]
    if b!=0 and a!=0:
        solution_list=[a+b,-(a+b),a-b,-(a-b),a*b,-(a*b),a/b,b/a,-a/b,-b/a] #加一些操作
    else:
        solution_list=[a,-a,a,-a,0,0]
    if 24 in solution_list and len(operation_history)==2:
        operation_history.append(solution_list.index(24))
        #print (display_formula(operation_history,origin_list))
        return ("found")
    else:
        return solution_list

def all_solution(number_list,operation_history,origin_list):
    l=len(number_list)
    if l==2:
        if two_number_all_solution(number_list,operation_history,origin_list)=="found":
            return "found"
    else:
        no_one_two=two_number_all_solution(number_list[0:2],operation_history,origin_list)
        i=0
        breakloop=0
        while i in range (len(no_one_two)) and breakloop == 0:
            operation_history.append(i)
            now_list=[no_one_two[i]]
            now_list+=number_list[2:]
            if all_solution(now_list,operation_history,origin_list)=="found":
                breakloop=1
            operation_history.pop()
            i+=1
        if breakloop==1:
            return "found"
        if l==4:
            no_one_two=two_number_all_solution(number_list[0:2],operation_history,origin_list)
            no_three_four=two_number_all_solution(number_list[2:4],operation_history,origin_list)
            i=0
            j=0
            breakloop=0
            while i in range (len(no_one_two)) and breakloop == 0:
                while j in range (len(no_three_four)) and breakloop == 0:
                    operation_history.append(i)
                    now_list=[no_one_two[i]]
                    now_list+=[no_three_four[j]]
                    if all_solution(now_list,operation_history,origin_list)=="found":
                        breakloop=1
                    operation_history.pop()
                    j+=1
                i+=1
'''
all_combination=list(combinations_with_replacement(range(1,14), 4))
total_number=0
for combination in all_combination:
    number_list=list(combination)
    permutations_object = list(permutations(number_list))
    i=0
    breakloop=0
    #for number_list in permutations_object:
    while i<=23 and breakloop==0:
        number_list=permutations_object[i]
        origin_list=number_list
        operation_history=[]
        if all_solution(list(number_list),operation_history,origin_list)=="found":
            breakloop=1
        i+=1
    total_number+=breakloop
    if breakloop==0:
        print (number_list)

print (total_number,len(all_combination),total_number/len(all_combination))
'''
total_number=0
no_test=70000
for j in range (no_test):
    number_list=[]
    for k in range (4):
        number_list.append(random.randint(1,13))
    permutations_object = list(permutations(number_list))
    i=0
    breakloop=0
    #for number_list in permutations_object:
    while i<=23 and breakloop==0:
        number_list=permutations_object[i]
        origin_list=number_list
        operation_history=[]
        if all_solution(list(number_list),operation_history,origin_list)=="found":
            breakloop=1
        i+=1
    total_number+=breakloop
    #if breakloop==0:
        #print (number_list)

print (total_number,no_test,total_number/no_test)


