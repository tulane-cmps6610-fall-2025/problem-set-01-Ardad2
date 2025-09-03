"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(x):
    a, b = x  # unpack the pair

    if a == 0:
        return b
    if b == 0:
        return a

    s = min(a, b)
    l = max(a, b)
    return foo((s, l % s))

def longest_run(mylist, key):
    """
    Return the length of the longest contiguous run of `key` in `mylist`.
    Example: longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    """
    max_sequence = 0
    cur_sequence = 0
    for v in mylist:  
        if v == key:
            cur_sequence += 1
            if cur_sequence >= max_sequence:
                max_sequence = cur_sequence
        else:
            cur_sequence = 0
    return max_sequence


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if not mylist:
        return 0

    def recurse(low, high):
        #Base Case: Only one element.

        if high - low == 1:
            count = 1 if mylist[low] == key else 0
            return Result(count, count, count, bool(count))
        
        #Divide and recursively solve both halves.
        mid = (low + high) // 2
        left_half, right_half = recurse(low, mid), recurse(mid, high)
 
        #Check if either of the entire sequences matches with the given key.
        is_entire_range = left_half.is_entire_range and right_half.is_entire_range

        #Finding the longest sequences on both the left and right halves.
        left  = left_half.left_size  + (right_half.left_size  if left_half.is_entire_range else 0)
        right = right_half.right_size + (left_half.right_size if right_half.is_entire_range else 0)

        # The longest sequence can be entirely in the left half, entirely in the right half, and aslo in the middle.
        longest = max(left_half.longest_size, right_half.longest_size, left_half.right_size + right_half.left_size)

        #Return the result for this current sequence being traversed.
        return Result(left, right, longest, is_entire_range)
    #Start recursion from the first index.
    return recurse(0, len(mylist)).longest_size


        

## Feel free to add your own tests here.

def test_foo():
    assert foo((18, 30)) == 6
    assert foo((12, 6)) == 6
    assert foo((7, 13)) == 1
    assert foo((0, 5)) == 5
    assert foo((18, 30)) == foo((30, 18))
    assert foo((12, 6)) == foo((6, 12))
    assert foo((5, 5)) == 5


def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([], 1) == 0
    assert longest_run([2,3,4], 1) == 0
    assert longest_run([7], 7) == 1
    assert longest_run([7], 8) == 0
    assert longest_run([5,5,5,5], 5) == 4
    assert longest_run([9,9,9,1,2,3], 9) == 3
    assert longest_run([1,2,3,4,4,4], 4) == 3
    assert longest_run([1,2,1,2,1,2], 1) == 1
    assert longest_run([0,7,7,7,1,7,7,0], 7) == 3

def test_longest_run_recursive():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([1,1,1,1], 1) == 4
    assert longest_run_recursive([1,2,3], 4) == 0
    assert longest_run_recursive([], 5) == 0
    assert longest_run_recursive([7], 7) == 1
    assert longest_run_recursive([7], 8) == 0
    assert longest_run_recursive([9,9,9,1,2,3], 9) == 3
    assert longest_run_recursive([1,2,3,4,4,4], 4) == 3

