# 問題2

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
# caps = []
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

# def pleaseConformOpt(caps):
#     #Initialization
#     start = 0
#     forward = 0
#     backward = 0
#     intervals = []

#     caps = caps + ['END']

#     #Determine intervals where caps are on in the same direction
#     for i in range(1, len(caps)):
#         if caps[start] != caps[i]:
#             # each interval is a tuple with 3 elements (start, end, type)
#             intervals.append((start, i - 1, caps[start]))
            
#             if caps[start] == 'F':
#                 forward += 1
#             else:
#                 backward += 1
#             start = i

#     if forward < backward:
#         flip = 'F'
#     else:
#         flip = 'B'
#     for t in intervals:
#         if t[2] == flip:
#             if t[0] == t[1]:
#                 print('Person at position', t[0], 'flip your cap!')
#             else:
#                 print ('People in positions', t[0], 'through', t[1], 'flip your caps!')


def pleaseConformOnepass(caps):
    if len(caps) <= 0:
        return print('no caps')
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                if caps[i] == caps[i+1]:
                    print('People in positions', i, end='')
                else:
                    print('Person at position', i, 'flip your cap!')
            elif caps[i] == caps[0] and caps[i] != caps[i-2]:
                print(' through', i-1, 'flip your caps!')

# pleaseConformOpt(caps)
pleaseConformOnepass(caps)
