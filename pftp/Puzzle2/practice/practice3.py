

sched2 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToPartySmart(sched):
    max_val = time = 0
    for y in sched:
        val = 0
        for c in sched:
            if c[0] <= y[0] < c[1]:
                val += c[2]
        if max_val < val:
            max_val = val
            time = y[0]

    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', max_val, 'value will be getting!')

bestTimeToPartySmart(sched2)

