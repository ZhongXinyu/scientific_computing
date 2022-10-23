def write_func(list):
    '''
    -argument: list of coeeficient of polynomials
        e.g. [3,0,-2] means polynomial function of 3x^2+0x^1-2
    -output:
        (polynomial equation, derivative of polynomial equation)
    '''
    order=len(list)-1
    func=""
    i=0
    while order >= 1:
        func+=f'{list[i]}*x**{order}+'
        i+=1
        order+=-1
    func += f'{list[i]}'
    return (func)

def newton_raphson(func,dfunc,x,n):
    '''
    Argument: (function,derivative of the function,location of the starting point, n is the number of interation)
    '''
    x_new=x-func(x)/dfunc(x)
    if abs(x_new-x)<=10**(-9):
        return x_new
    else:
        n+=1
        if n<=50: 
            return newton_raphson(func,dfunc,x_new,n)
        else:  ### iterate 50 times still cannot find a zero, zero is non-existence between two turning points
            return False  

def zeros(co_list1):
    '''
    argument:
        -list: list of coefficient
    output:
        -list: location of zeros
    alogorithm:
        if order == 1:
            return location of zero
        else:
            find zeros of the lower order:
            use the zeros in lower order (turning point) to find locations of zeros
                (use newton_raphson method)
    '''

    order=len(co_list1)-1
    co_list2=[]
    if order==1:
        return ([-co_list1[1]/co_list1[0]])
    else:
        '''
        Find the derivative the polynomial function
        -------------------------------------------
        '''
        for i in range(order):
            co_list2.append(((order-i)*co_list1[i]))
        '''
        -------------------------------------------
        The turning point of the polynomial is the zeros of the derivative of the polynomial
        -------------------------------------------
        '''
        list_of_turningpoints=zeros(co_list2)
        if list_of_turningpoints == []: 
            list_of_turningpoints = [0]
        func,dfunc=write_func(co_list1),write_func(co_list2)
        list_of_zeros=[]
        for i in range(len(list_of_turningpoints)-1):
            zero=newton_raphson(
                (lambda x: eval(func)),
                (lambda x: eval(dfunc)),
                0.5*(list_of_turningpoints[i]+list_of_turningpoints[i+1]),
                0
            )
            '''
                POSSSIBLE IMPROVEMENT
                ============================
                if turning_point_1 and turning_point_2 is one positive and one negative:
                    zero exist
                if turning_point_1 and turning_point_2 same sign:
                    zero does not exist
                if anyturning_point is 0:
                    this point can be added to the list of zeros straight away
            '''
            if zero != False:
               list_of_zeros.append(zero)
        if len(list_of_turningpoints)>=1:
            zero=newton_raphson(
                    (lambda x: eval(func)),
                    (lambda x: eval(dfunc)),
                    list_of_turningpoints[-1]+0.01,
                    0
                )
            if zero != False:
                list_of_zeros.append(zero)
            zero=newton_raphson(
                    (lambda x: eval(func)),
                    (lambda x: eval(dfunc)),
                    list_of_turningpoints[0]-0.01,
                    0
                )
            if zero != False:
                list_of_zeros.append(zero)
        #remove duplicates
        list_of_zeros=list(set(list_of_zeros))
        #sort list
        list_of_zeros.sort()
        return (list_of_zeros)


'''
Test Newton_Raphson Method
==========================
This can only find one zero(near point -0.74)
print(
    newton_raphson(
    (lambda x: eval(func)),
    (lambda x: eval(dfunc)),
    -0.74,
    0)
)
'''

n = int(input("Enter highest order of polynomial : "))
 
polynomial_list=[]
for i in range (n+1):
    polynomial_list.append(float(input(f"Enter coefficient of {n-i}th order : ")))

print ("Zeros are:",zeros(polynomial_list))
