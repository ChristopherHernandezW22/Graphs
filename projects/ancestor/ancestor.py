
def earliest_ancestor(ancestors, starting_node):
    # pass

    earliest_ancestor = -1
    current_length = 0

    # Adjacency list for all nodes/edges in ancestors
    ancestor_dictionary = {}

    # Add all nodes and edges to adjacency list
    for a in ancestors:
        if a[0] in ancestor_dictionary:
            ancestor_dictionary[a[0]].add(a[1])
        else:
            ancestor_dictionary[a[0]] = set()
            ancestor_dictionary[a[0]].add(a[1])
    
    # Begin BFS
    queue = Queue()
    visited = set()
    queue.enqueue([starting_node])
    while queue.size() > 0:
        

    # return earliest_ancestor