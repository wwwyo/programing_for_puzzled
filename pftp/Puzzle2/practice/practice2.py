sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]


def bestTimeToPartySmart(sched):
    maxcount = time = 0
    for y in sched:
        count = 0
        for c in sched:
            if c[0] <= y[0] < c[1]:
                count += 1
        if maxcount < count:
            maxcount = count
            time = y[0]

    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')

bestTimeToPartySmart(sched2)

