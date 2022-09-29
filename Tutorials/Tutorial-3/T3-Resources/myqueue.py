MAX_LEN = 10


def enqueue(queue, value):
    """Adds a value to the end of the provided queue list

    Args:
        queue (list): Queue list object
        value (any): Value to be added to the end of the queue

    Returns:
        boolean: Returns True if succesfully added and False if the queue is out of space
    """
    if len(queue) >= MAX_LEN:
        return False

    queue.append(value)
    return True


def dequeue(queue):
    if isempty(queue):
        return None
    return queue.pop(0)


def peek(queue):
    if isempty(queue):
        return None
    return queue[0]


def isempty(queue):
    return len(queue) == 0


def multienqueue(queue, items):
    # num_added serves as both a increment counter for the while loop and also a variable to keep track of the number of items successfully added to the queue
    num_added = 0

    # sentinel value
    should_continue = True

    while should_continue:
        should_continue = enqueue(queue, items[num_added])
        if should_continue:
            num_added += 1
    return num_added


def multidequeue(queue, number):
    dequeued_list = []
    for i in range(0, number):
        removed_item = dequeue(queue)
        if removed_item == None:
            break  # break the loop if dequeue(queue) returned None
        dequeued_list.append(removed_item)
    return dequeued_list
