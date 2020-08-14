class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

#Enqueue: Adds an item to the queue. 
#Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. 

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    current_node = starting_node
    relationships = {}
    for node in ancestors:
        if node[1] not in relationships:
            relationships[node[1]] = set()
        relationships[node[1]].add(node[0])
#If no parents return -1
    if starting_node in relationships:
        queue.enqueue(relationships[current_node])
    else:
        return -1
#If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. First in first out
    while True:
        relations = queue.dequeue()
        current_node = min(relations)
        if current_node not in relationships:
            return current_node
        else:
            queue.enqueue(relationships[current_node])