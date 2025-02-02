class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    count = 0
    
    for x in numbers:
        if x % divide == 0:
            count += 1
    return count

def test_list_divide():
    """
    Test listDivide
    """
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        # If you change 100 below to 1 it will break as return check != 2 
        assert list_divide([30,54,63,98,100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
        
        print("No errors in test")
    except: 
        # If test fails raise ListDivide Exception funciton 
        raise ListDivideException("Test case failed.")

if __name__ == "__main__":
    test_list_divide()
