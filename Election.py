# You are the head of the election committee in your village. Each Political party is associated
# with a unique number and the votes are represented as an integer array A. where each
# element contains the party number voted for by the villagers. For a party to win, they must
# have a majority of votes. our task is to find and return an integer value denoting the winning
# party's number
# Note: If only one vote is there he is the winner.
# Input Format : input1: An integer value representing the number the
# number of voters input2: An integer array A representing the votes of the
# voters. output Format:
# Return an integer value denoting the winning party's number



n=int(input("Enter the Candidates:"))
l=list(map(int,input("Enter No. of Votes:").split()))
Count=[0]*n
for i in l:
    Count[i-1]=Count[i-1]+1
print("Winner is:",max(Count))
