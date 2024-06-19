# Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and
# will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the party venue
# within this time which takes him P minutes. The contest comprises of N problems that are
# arranged in order of difficulty, with problem 1 being the simplest and problem N being the
# most difficult. Max is aware that he will require 5*i minutes to solve the ith problem.
# Your task is help Max find and return an integer value, representing the number of
# problems Max can solve and reach the party venue within the given time frame of 4 hours.
# Note: Max will leave his home at exactly 8 PM to reach the party venue.
# Input Format:
# input1: An integer value N, representing the total number of problems.
# input2: An integer value P, Representing the time to travel in minutes from his home to the
# party venue


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
