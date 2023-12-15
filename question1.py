def stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.insert(0, new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
    return our_list

def queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
    return our_list

# Example usage
new_list = [1, 2, 3, 4]


print("Stack implementation")
print("Array: " + str(new_list))

print("Adding new element 0 to the stack")
new_list = stack(new_list, 'add', 0)
print(new_list)

print("Removing an element from the stack")
new_list = stack(new_list, 'remove')
print(new_list)


print("Queue implementation")

new_list = [1, 2, 3, 4]

print("Array: " + str(new_list))

print("Adding new element 5 to the queue")
new_list = queue(new_list, 'add', 5)
print(new_list)

print("Removing an element from the queue")
new_list = queue(new_list, 'remove')
print(new_list)
