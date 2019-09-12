#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity, bag=None, cache=None):
    if len(items) == 0:
        return []
    
    if not bag:
        bag = []
    
    for i in sorted_items (from best to worst):
        if i is not in bag
        and bag will not be full
        and bag total will be better than best bag total:
            add i to bag

    RatioItem = namedtuple('RatioItem', ['index', 'size', 'value', 'ratio'])
    with_ratio = []
    for i in items:
        with_ratio.append(RatioItem(i[0], i[1], i[2], i[2] / i[1]))
    def return_ratio(el):
        return el[3]
    with_ratio.sort(key=return_ratio, reverse=True)
    
    
    for i in with_ratio:
        if i not in bag and 

    get optimal items for each capacity

    
        

    


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
