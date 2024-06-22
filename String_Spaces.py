# You have been given the task of making the content on a social media platform more userfriendly. Your task is to find and return an integer value representing the count of the
# number of spaces in a given string S.
# Input: A
# string S
# Output :
# Return an integer value representing the count of the number of spaces in a given string S. 

s=str(input("enter string vith spaces:"))
c,m=0,0
for i in s:
    # m+=i
    if i==' ':
        c+=1
    else:
        pass
print(int(c))