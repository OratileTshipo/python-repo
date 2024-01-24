"""In this project, you will solve the mathematical puzzle known as the Tower of Hanoi.
The puzzle consists of three rods and a number of disks of different diameters.
The goal of this puzzle is moving the disks from the first rod to the third rod, following specific rules that restrict placing a larger disk on top of a smaller one.
Start by creating an empty dictionary named rods to represent the rods."""

#Initialise variables
NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1

print( f'number of moves: {number_of_moves}') #dg

rods = {'A':list(range(NUMBER_OF_DISKS,0,-1)),
        'B':[],
        'C':[]}

print(type(rods['A'])) # dg
print(rods['A']) #dg

# Hanoi puzzel solved through iteration
def move(n,source,auxiliary,target):
    # Display starting configuration
    print(f'rods: {rods}')
    for move in range(0,number_of_moves):
        print(f'move num: {move+1}')

        remainder = (move + 1) % 3
        
        # move between A <--> C
        if remainder == 1:
            if n % 2 != 0:
                print(f'allowed between {source} and {target}\n')
        # move between A <--> B
        elif remainder == 2:
            print(f'allowed between {source} and {auxiliary}\n')
            make_allowed_move(source,auxiliary)
        # move between B <--> C
        elif remainder == 0:
            #print(f'allowed between {target} and {auxiliary}')
            print(f'allowed between {auxiliary} and {target}\n')
            print("made changes for gitHub")
            make_allowed_move(auxiliary,target)

            
def make_allowed_move(rod1,rod2):
    forward = False
    # check if rods is empty
    if rods:
        print(f'rods dictionary is not empty: {rods}')
    else:
        print(f'rods is empty {rods}')

    # check if target is empty
    if  not rods[rod2]:
        print( f'target rod is empty: {rods[rod2]}')
        forward = True
    else:
        print( f'target rod is not empty: {rods[rod2]}')
        print( f'target rod last element: {rods[rod2][-1]}')
        #print(forward)

    # check if source is empty
    if   not rods[rod1]:
        print( f'source rod is empty: {rods[rod1]}')
        print( f'source rod last element: {rods[rod1][-1]}')
        #forward = False
    else:
        print( f'source rod is not empty: {rods[rod1]}')
        print( f'source rod last element: {rods[rod1][-1]}')
        rods[rod2].append(rods[rod1][-1].pop())
        #print(forward)
        
    # check if source in rods dictionary and last element in source rod of the dictionary is lower than last element of the target rod 
    #if rods[rod1][-1] and rods[rod1] < rods[rod2][-1]:
    #   forward = True
    #   if forward == True:
    #        print(f'Moving disk {rods[rod1[-1]]} from {rod1} to {rod2}')
            # move last element from source to target rod
    #        rods[rod2].append(rods[rod1][-1].pop())
        #else:
        #    print(f'Moving disk {rods[rod1]} from {rod2} to {rod1}')
            #rods[rod2].append(rods[rod1].pop())
        # display our progress
        #    print(F' TESTING OUTPUT {rods}')

# initiate function call from Source A to target C with auxiliary B
move(NUMBER_OF_DISKS,'A','B','C')
make_allowed_move('A','C')