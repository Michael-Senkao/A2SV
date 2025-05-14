# Problem: Delete a linked list using recursion - https://www.geeksforgeeks.org/delete-linked-list-using-recursion/

def delete_list(curr):
    # Base case: If the list is empty, return
    if curr is None:
        return

    # Recursively delete the next node
    delete_list(curr.next)

    # Delete the current node
    curr = None