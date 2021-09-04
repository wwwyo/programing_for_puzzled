#Programming for the Puzzled -- Srini Devadas
#Counting the Ways You Can Count Change
#Given a target value, and a set of bill denominations, figure out
#all the different ways that you can reach target value using various bills

#This procedure finds the different ways to make change treating
#bills of the same denomination as identical
def makeSmartChange(bills, target, highest, sol = []):
    global min_sol
    #Recursion base case -- reached the target
    if sum(sol) == target:
        if len(min_sol) == 0:
            min_sol = sol
        else:
            min_sol = sol if len(min_sol) > len(sol) else min_sol
        return

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
	    return

    #Recursive calls: explore adding each bill denomination
    for bill in bills:
        #Add bill only if bill is large enough
        if bill[0] >= highest and sol.count(bill[0]) < bill[1]:
            newSol = sol[:]
            newSol.append(bill[0])
            makeSmartChange(bills, target, bill[0], newSol)

    return

# bills = [1, 2, 5]
# makeSmartChange(bills, 6, 1)
# bills2 = [1, 2, 5, 10]
# makeSmartChange(bills2, 16, 1)
yourMoney =  [(1,3),(2,3),(5,1)]
min_sol = []
makeSmartChange(yourMoney, 6, 1)
print(min_sol)

