dividend=10
divisor=3
str_dividend=str(abs(dividend))
str_divisor=str(abs(divisor))
sign=1
if abs(dividend)!=dividend:
    sign=sign*(-1)
if abs(divisor)!=divisor:
    sign=sign*(-1)
i1=0
i2=0
quotient=""
str_remainder=""
while i2<len(str_dividend):
    print ("i1=",i1,"i2=",i2)
    int_partial_dividend=int(str_remainder+str_dividend[i1:i2+1])
    counter=0
    print(int_partial_dividend)
    while int_partial_dividend>=abs(divisor):
        int_partial_dividend=int_partial_dividend-abs(divisor)
        counter+=1
    quotient=quotient+str(counter)
    str_remainder=str(int_partial_dividend)
    i2+=1  
    while str_remainder[0]=="0":
        i1+=1
        str_remainder=str_remainder[1:]
        if str_remainder =="":
            break
    i1+=1
print(sign*int(quotient))