import heapq

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList)  # turn myList into a Min Heap
print(myList)    # => [1, 3, 2, 5, 9, 4]
print(myList[0]) # first value is always the smallest in the heap

heapq.heappush(myList, 10)  # insert 10
x = heapq.heappop(myList)   # pop and return smallest item
print(x)                    # => 1


myList = [9, 5, 4, 1, 3, 2]
myList = [-val for val in myList]  # multiply by -1 to negate
heapq.heapify(myList)

x = heapq.heappop(myList)
print(-x)  # => 9 (multiply by -1 again)

# ===== HEAPPOP: Removing the smallest =====
x = heapq.heappop(myList)
# Step 1: Return the root (smallest value)
#         x = 1
# Step 2: Move LAST element to the root
#         [10, 3, 2, 5, 9, 4]
# Step 3: "BUBBLE DOWN" - compare with children and swap with smallest child
#         10 > 3 (left child), so swap
#         [3, 10, 2, 5, 9, 4]
#         10 > 5 (left child now at index 3), so swap
#         [3, 5, 2, 10, 9, 4]
# Now valid! Smallest at root again.
print(x)        # => 1
print(myList)   # => [2, 3, 4, 5, 9, 10] (2 is now smallest!)


# ===== MAX HEAP EXAMPLE =====
myList = [9, 5, 4, 1, 3, 2]
myList = [-val for val in myList]  # Negate: [-9, -5, -4, -1, -3, -2]
heapq.heapify(myList)
# Now -9 is at root (smallest negative = largest positive)
# When we pop, we get -9, negate again to get 9

x = heapq.heappop(myList)
print(-x)  # => 9
