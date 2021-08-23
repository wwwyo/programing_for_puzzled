sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]


def howManyPeople(sched, ystart, yend):
    count = 0
    for c in sched:
        # if not(c[1] <= ystart or yend <= c[0]):
        if c[1] > ystart and yend > c[0]:
            count += 1
    print(count, 'celebrities will be attending!')

howManyPeople(sched, 9, 10)

