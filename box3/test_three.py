from .sort import super_sort

def test_order_array():
    assert super_sort([3,5,4,1,2]) == [1,2,3,4,5]
