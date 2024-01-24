copper = {'species':'pig',
          'age':'3'}
print(copper['age'])

# add key-value pair to dictionary
copper['food'] = 'waste'
#print(copper['food'])

# change the value of an existing key
copper['food'] = 'Vegies and fruits'
print(copper['food'])

# remove a key-value from dictionary
del copper['age']

"""From this part we are building the shortest path algorithm"""

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph,start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
            print(f'{node} is the starting node') #debug
        else:
            distances[node] = float('inf')
            print(f'{node} is not the starting node, thus distance is undetermined') #dg
    print(unvisited[0]) # debug line
    print(f'Unvisited: {unvisited}\nDistances: {distances}') #dg


"""Another method without use of for loop"""
def shortest_path_2(graph,start,target=''):
   print('\nnmethod 2 initializing objects...') # dg

   unvisited = list(graph)
   distances = {node:0 if node == start else float('inf') for node in graph}
   paths = {node:[]  for node in graph}

   print(f'\nstep 1. Appending start: {start} to paths dic') #dg

   paths[start].append(start)

   print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}') #dg
   print(f'\nOpening while loop while unvisited is not empty\n') #dg 

   while unvisited:
       current = min(unvisited, key=distances.get)

       print(f'current node: {current}') #dg

       for node,distance in graph[current]:
           
           print(f'inside for loop for {node}:{distance}') #dg

           if distance + distances[current] < distances[node]:
               
               print(f'\ninside if \nnext node: {node} and distance: {distance} + distance to current node: {distances[current]} < distances[node]: {distances[node]}') #dg
               print("set the value of distance of node: {node} to distance of next node + current node: {current}/n")

               distances[node] = distance + distances[current] 

               print(f' node {node} updated distances[node]: {distances[node]}') #dg
               print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}') #dg

               if paths[node] and paths[node][-1] == node: # checking for last element in paths of node
                   
                   print(f'inside if last element of paths[node]: {paths[node]} == node: {node}, {paths[node][-1]} == {node}') #dg
                   print(f"paths[current]: {paths[current]}") #dg

                   paths[current] = paths[node]

                   print(f"updated paths[current] {paths[current]}") #dg
                   print(f'Unvisited: {unvisited}\nDistances: {distances}') #dg

               else:
                   paths[node].extend(paths[current])

                   print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}') #dg

               paths[node].append(node)
            
                    
           print(f'{node} {distance}') #dg
       print(f'lis {unvisited}removing {current}') #dg
       print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}\nEnd of for loop in graph[current]') #dg

       unvisited.remove(current)

       print(f'current removed {unvisited}') #dg
   print(f'End of while loop, unvisited is empty\ntarget: {target}')
   #targets_to_print = [target if target else graph]
   targets_to_print2 = target if target else graph

   print(f'targets ro print: targets_ to_ print \ntargets ro print2: {targets_to_print2}\n')

   for node in targets_to_print2:
       if node == start:
          continue
          print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
       else:
          print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
          print(f'targets to print: {targets_to_print2}\nEnd of for loop in targets!')
   return distances, paths


shortest_path(my_graph,"A")
shortest_path_2(my_graph,"D","F")


