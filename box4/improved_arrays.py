from .my_arrays import MyArray
## This is an awesome bubble sort implementation...
## Lets remember how does it works?
## 1. First of all, you need to make swap through all elements from the left that are lower than the elements on the right
## 2. You don't need to compare with all elements all the time, since every time you pass through the origin array, bigger element go to right, so reduce one index at each iteration
## 3. Stop when no more swaps happens in a full scan cycle OR
##    whenever your iterator reaches zero
def quick_sort(self):
    right_iterator = len(self)-1
    swap_el = "go"

    while swap_el != None:
        swap_el = None
        for index in range(0, right_iterator):
            if self[index] > self[index+1]:
                swap_el = self[index]
                self[index] = self[index + 1]
                self[index + 1] = swap_el
        right_iterator = right_iterator - 1

    return self

MyArray.quick_sort = quick_sort