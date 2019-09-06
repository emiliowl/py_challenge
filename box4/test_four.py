from .my_arrays import MyArray
from .improved_arrays import *

def test_order_array():
    assert MyArray([3,5,4,1,2]).quick_sort() == [1,2,3,4,5]
