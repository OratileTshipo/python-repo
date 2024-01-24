"""In this project, you will solve the mathematical puzzle known as the Tower of Hanoi.
The puzzle consists of three rods and a number of disks of different diameters.
The goal of this puzzle is moving the disks from the first rod to the third rod,
following specific rules that restrict placing a larger disk on top of a smaller one"""

# Initialise global values
NUMBER_OF_DISKS = 4
number_of_moves = (2**NUMBER_OF_DISKS)-1
# rods has rods_ as keys, and list of values as disks in rod, 
rods = {'A':list(range(NUMBER_OF_DISKS,0,-1)),
        'B':[],
        'C':[]
        }

# move disks between rods using iterative approach to solve the problem
def move(n,source,auxiliary,target):
    # displaying starting configuration
    print(f'\nStarting configuration: {rods}')

    # iterative solution to Tower of Hanoi puzzel
    for move in range(number_of_moves):
        # initialise local variables
        remainder = (move + 1) % 3

         # move A-C 1st, 4th and 7th, where division of move num by 3 is = 1
        if remainder == 1:
            if n%2 != 0:
                print(f'\nmove: {move+1}\nAllowed from {source} to {target} or from {target} to {source}')
                # check rods and make moves
                make_allowed_move(source,target)
                check_rods(source,auxiliary,target)
            else:
                print(f'\nmove: {move+1}\nAllowed from {source} to {auxiliary} or vise versa')
                make_allowed_move(source,auxiliary)
                check_rods(source,auxiliary,target)

        # move A-B 2nd and 5th where remainder = 2
        elif remainder == 2:
                if n%2 != 0:
                    print(f'\nmove: {move+1}\nAllowed from {source} to {auxiliary} or vise versa')
                    make_allowed_move(source,auxiliary)
                    check_rods(source,auxiliary,target)
                else:
                    print(f'\nmove: {move+1}\nAllowed from {source} to {target} or vise versa')
                    make_allowed_move(source,target)
                    check_rods(source,auxiliary,target)
        # move B-C 3rd and 6th, where reminder = 0  
        elif remainder == 0:
                print(f'\nmove: {move+1}\nAllowed from {auxiliary} to {target} or vise versa')
                #check_rods(source,auxiliary,target)
                make_allowed_move(auxiliary,target)
                check_rods(source,auxiliary,target)

# recursive approach to the solution
def move2(n,source,auxiliary,target):
    # move n -1 disks from source to auxiliary, so they are out of the way
    if n > 0:
        move2(n-1,source,target,auxiliary)
    # move the nth disk from source to target
        rods[target].append(rods[source][-1])
        del rods[source][-1]
        # move the n - 1 disk that we left on auxiliary onto target
        move2(n-1,source,auxiliary,target)
        # display our progress
        print(f'progress: {rods}')

    
# check rods
def check_rods(source,auxiliary,target):
    print('Checking contents of lists from dictionary...\n')
    if not rods[source]:
        print(f'\nrod 1: Source is empty {rods[source]}')
        forward = False
    else:
        print(f'rod 1: Source is not empty {rods[source]}')
        # check auxiliary rod contents
    if not rods[auxiliary]:
        print(f'rod 2: Auxiliary is empty {rods[auxiliary]}')
    else:
        print(f'rod 2: Auxiliary is not empty {rods[auxiliary]}')
        # check target rod contents
    if not rods[target]:
        print(f'rod 3: Target is empty, forward moves allowed {rods[target]}')
    else:
        print(f'rod 3: Target is not empty, forward moves may or may not be allowed {rods[target]}\n')

# allowed moves
def make_allowed_move(rod1,rod2):
    forward = False 
    # check target rod contents and set rod move direction
    if not rods[rod2]:
       forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
       forward = True
       print(f'rod 3: Traget is not empty, but forward moves allowed {rods[rod2]}\n')
    if forward:
        print(f'\n...moving disk {rods[rod1][-1]} from {rod1} to {rod2}...')
        rods[rod2].append(rods[rod1][-1])
        del rods[rod1][-1]
        #rods[target].append(rods[source].pop())
    else:
        print(f'...moving disk {rods[rod2][-1]} from {rod2} to {rod1}...')
        rods[rod1].append(rods[rod2][-1])
        del rods[rod2][-1]
        #rods[target].append(rods[source].pop())


# initiate move from Source: A to Target: C, with Auxiliary: B
#move(NUMBER_OF_DISKS,'A','B','C')
#check_rods('A','B','C')
#make_allowed_move('A','B')
move2(NUMBER_OF_DISKS,'A','B','C')