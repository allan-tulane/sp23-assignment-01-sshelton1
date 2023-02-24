"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
      return x
    else:
      return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
  i = 0
  runs = [0]
  counter = 0
  while i < len(mylist):
    if mylist[i] == key:
      counter += 1
      if mylist[i+1] != key:
        runs.append(counter)
        counter = 0
    i += 1
  return max(runs)
        
class Result:
    """ done """
    def __init__(self, left_side, right_side, longest_size, is_entire_range):
        self.left_side = left_side               # run on left side of input
        self.right_side = right_side             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_side, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  ### TODO
  def combine(rleft, rright):
    if rleft.is_entire_range == True and rright.is_entire_range == True:
      sum = rleft.longest_size + rright.longest_size
      return Result(sum, sum, sum, True)
    else:
      sum = -1
      if rleft.is_entire_range == True:
        left = rleft.left_side + rright.left_side
      else:
        left = rleft.left_side
      if rright.is_entire_range == True:
        right = rright.right_side + rleft.right_side
      else:
        right = rright.right_side
      if rleft.right_side != 0 and rright.left_side != 0:
        sum = rleft.right_side + rright.left_side
      sum = max([sum, rright.longest_size, rleft.longest_size])
      return Result(left, right, sum, False)
        
  def split_combine(mylist,key):
    if len(mylist) == 1:
      if mylist[0] == key:
        return Result(1, 1, 1, True)
      else:
        return Result(0, 0, 0, False)
    else:
      return(combine(split_combine(mylist[0:(len(mylist)//2)], key), split_combine(mylist[(len(mylist)//2):], key)))
  
  final = split_combine(mylist,key)
  return final.longest_size
    
## Feel free to add your own tests here.
def test_longest_run():
  assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

