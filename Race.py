# Two person start a race where person 1 starts his race with delay of 2 sec and 
# person 2 starts his race with delay of 1 sec.
# They both complete a lap in 3 sec and 4 sec respectively 
# Find at what time the both meet 

a=2
b=1
while a!=0 and b!=0:
    a+=3
    b+=4
    if a==b:
        print("meet at: ",a)
        break
    else :
        continue
