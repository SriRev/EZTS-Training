# Find the number of commas when printing the integer from 1 to 100,000(inclusive).

def count_commas():
    num = int(input("Enter the number up to which the commas should be counted: "))
    if num < 1000:
        print(0)
    elif num < 1000000:
        print((num - 1000) + 1)
    else:
        commas_one = 999000
        commas_two = (num - 999999) * 2 
        total_commas = commas_one + commas_two
        print(total_commas)

count_commas()
