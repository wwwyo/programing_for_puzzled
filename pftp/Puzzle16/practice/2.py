#Programming for the Puzzled -- Srini Devadas
#Greed is Good
#A greedy algorithm is used to find the most packed course schedule, i.e.,
#the one with the maximum number of non-conflicting classes

#This procedure is given a course and a list of other courses, and removes
#all courses in the list that conflict with the given course. 
def removeConflictingCourses(selCourse, courses):
    nonConflictingCourses = []
    for s in courses:
        if s[1] <= selCourse[0] or s[0] >= selCourse[1]:
            nonConflictingCourses.append(s)
    
    return nonConflictingCourses

#This procedure iteratively picks a course using a function selectionRule that is
#an argument to the procedure, and removes all conflicting courses, and repeats
#until the list of courses is empty
def executeSchedule(courses, selectionRule):
    selectedCourses = []
    while len(courses) > 0:
        selCourse = selectionRule(courses)
        selectedCourses.append(selCourse)
        courses = removeConflictingCourses(selCourse, courses)
    return selectedCourses


#This procedure implements the earliest start time rule
def earliestStartTime(courses):
    for s in courses:
        if s == courses[0]: 
            earliestStartTime = s
        if s[0] < earliestStartTime[0]:
            earliestStartTime = s
    return earliestStartTime

#This procedure implements the shortest duration time rule
def shortDuration(courses):
    shortDuration = courses[0]
    for s in courses:
        if s[1] - s[0] < shortDuration[1] - shortDuration[0]:
            shortDuration = s
    return shortDuration

#This procedure implements the least number of conflicts rule
def leastConflicts(courses):
    conflictTotal = []
    for i in courses:
        conflictList = []
        for j in courses:
            if i == j or i[1] <= j[0] or i[0] <= j[1]:
                continue
            conflictList.append(courses.index(j))
        conflictTotal.append(conflictList)
    leastConflict = min(conflictTotal, key = len)
    leastConflictCourse = courses[conflictTotal.index(leastConflict)]
    return leastConflictCourse

#This procedure implements the earliest finish time rule
def earliestFinishTime(courses):
    earliestFinishTime = courses[0]
    for i in courses:
        if i[1] < earliestFinishTime[1]:
            earliestFinishTime = i
    return earliestFinishTime

def recursiveSelect(courses):
    max_selected = []
    if len(courses) == 0:
        return []
    for i in courses:
        after_courses = [x for x in courses if x[0] >= i[1]]
        selected = [i] + recursiveSelect(after_courses)

        if len(max_selected) == 0:
            max_selected = selected
        else:
            max_selected = selected if (sum(x[2] for x in max_selected) < sum(y[2] for y in selected)) else max_selected
    return max_selected

mycourses = [[8,10,1],[9,12,3],[11,12,1],[12,13,4],[15,16,1],[16,17,1],[18,20,2],[17,19,2],[13,20,7]]


# print ('Shortest duration:', executeSchedule(mycourses, recursiveSelect))
print ('Shortest duration:', recursiveSelect(mycourses))

