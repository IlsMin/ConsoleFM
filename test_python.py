import math 

def filter_odd_num(num):
    return (num % 2) == 0

nums_1_10 = [1,2,3,4,5,6,7,8,9,10]
rez_list = list(filter(filter_odd_num, nums_1_10))
#print (rez_list)
# filter
assert len(rez_list)==5, "bad filter rezult"
rez = rez_list.index(2)
#print (rez) 
assert rez==0, str(f"bad filter : rezult is {rez}")
# map
rez_list = list(map (lambda n: n*2, nums_1_10))
#print (type(rez_list))
assert len(rez_list)==10, "bad map rezult"
rez = rez_list.index(2)
assert rez==0, str(f"bad map : rezult is {rez}")
# sorted
rez_list = sorted(nums_1_10, reverse=True)
rez = rez_list.index(2)
assert rez==8, str(f"bad sorted: rezult is {rez}")

# math
assert (math.pi>3.14 and math.pi <3.15) , str(f"bad pi: rezult is {math.pi}")
assert math.sqrt(4) == 2  , str(f"bad sqrt: rezult is {math.sqrt(4) }")
assert math.pow(2,3) == 8  , str(f"bad pow: rezult is {math.pow(2,3) }")
assert math.pow(3,2) == 9  , str(f"bad pow: rezult is {math.pow(3,2) }")
assert math.hypot(4,3) == 5 , str(f"bad hypot: rezult is { math.hypot(4,3) }")


print('all good')