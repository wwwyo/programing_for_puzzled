#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships
#select a maximum number of friends such that no two friends dislike each other

#Optimized version that does not store all 2**n combinations, rather it
#iterates through them.

#This procedure finds the combination with the maximum number of guests       
def InviteDinnerOptimized(guestList, dislikePairs):

    n = len(guestList)
    invite = [('',0)]
    for i in range(2**n):
        Combination = []
        for j in range(n):
            if i >> j &1:
                Combination.append(guestList[n-1-j])
        #Check that it is a good combination
        good = True
        for j in dislikePairs:
            #Check that each element of j is in i
            if j[0] in list(map(lambda x: x[0], Combination)) and j[1] in list(map(lambda x: x[0], Combination)):
                good = False
        if good and len(Combination) > 0:
            #Check if it is the best combination so far
            if sum(c[1] for c in Combination) > sum(i[1] for i in invite):
                invite = Combination
                
    print ('Optimum Solution:', list(map(lambda x: x[0], invite)))
    


dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
InviteDinnerOptimized(guestList, dislikePairs)

