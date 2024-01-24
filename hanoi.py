NUMBER_OF_DISKS = 4
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, target, auxiliary)
        
        # move the nth disk from source to target
        rods[target].append(rods[source][-1])
        del rods[source][-1]
        
        # display our progress
        print(rods, '\n')
        
        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1,  auxiliary, source, target)

def move2(n, source, auxiliary, target):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, target, auxiliary)
        
        # move the nth disk from source to target
        target.append(source.pop())
        
        # display our progress
        print(rods, '\n')
        
        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
#move(NUMBER_OF_DISKS, 'A', 'B', 'C')
move2(NUMBER_OF_DISKS, A, B, C)