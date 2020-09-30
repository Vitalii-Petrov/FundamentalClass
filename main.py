from airtravel import *
from pprint import pprint as pp
a = Flight("SS001", Aircraft("ABC", "G-234", num_rows=10, num_seats=6))
#print(a.seating_plan())
#print(a._seating)
pp(a._seating)

a.allocate_seat("2A", "Mike")
print("-------------------------------------------")
pp(a._seating[:-5])