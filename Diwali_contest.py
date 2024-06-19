def max_problems_solved(T):
    
    hours, minutes = map(int, T.split(':'))
    start_minutes = hours * 60 + minutes
    
   
    party_start = 20 * 60
    
   
    available_time = party_start - start_minutes
    
    
    problems_solved = 0
    time_spent = 0
    
    
    while True:
        next_problem_time = 5 * (problems_solved + 1)
        if time_spent + next_problem_time <= available_time:
            time_spent += next_problem_time
            problems_solved += 1
        else:
            break
    
    return problems_solved


T = str(input("Enter time in 24 hour format:"))
result = max_problems_solved(T)
print(f"Max can solve {result} problems before the party.")