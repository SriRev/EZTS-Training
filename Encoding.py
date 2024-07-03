# You work in the message encoding department of a national security agency. Every message that is sent from or received in your office is encoded. You have an integer N, and each digit of N is squared and the squares are concatenated together to encode the original number. Your task is to find and return an integer value representing the encoded value of the number.
# input1: An integer value N representing the number to be encoded.
# Output :
# Return an integer value representing the encoded value of the number.
# Sample Input:
# 167
# Sample Output:
# 13649


n=int(input("Enter a No:"))
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
ans=rev(n)
print(ans)
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10+digit
        n=n//10
    return ans2
print(rev2(ans))