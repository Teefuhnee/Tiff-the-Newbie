#!/usr/bin/env python
# ==================================================================
# TUPLE
# ==================================================================
print "== TUPLES ==================================================="
tup1 = ('hello', "wassup", 2344, ["l1", "l2", "l3"]) #tuples are sequences but immutable
                                #immutable - obj can't be altered
                                #mutables - can be altered & keep id
                                # ^^ called "tuple packing"
a, b, c, d = tup1          #upacks tuple, needs same # of elems = vars

tup2 = 'a', "b", 'c'         #uses parenthese / none
tup3 = 33,                      #need a comma for 1 val
tup4 = ()                       #empty tuple
                                #can be sliced, concat
tup2 += tup3
print "tup1 = " + str(tup1)
#print tup2
print "tup2 = " + str(tup2)

print "=============================================================" + '\n'
# ==================================================================

# ==================================================================
# SETS
# ==================================================================
print "== SETS ====================================================="
colors = ["red", "orange", "red", "green", "blue", "orange"]

setColors = set(colors)    # gets rid of dups, no mutables
print setColors # can use set math ops (union / intersect...)

print "red" in colors # T
colors2 = ["red", "green"]
setColors2 = set(colors2)

newSet = setColors - setColors2
print newSet


print "=============================================================" + '\n'
# ==================================================================


# ==================================================================
# DICTIONARY
# ==================================================================
print "== DICTIONARY ==============================================="
#dictionary - set of unordered key:val pairs (keys uniq)
dict1 = { "abc" :  000,             # data type dictionary start w/ curly
          "asdfg" : 111,            # unordered & changeable
          20 : 222,                 # left side are keys -- have to be immutable
          "aslkdjf" : "string",
          ("abc", "123", 890) : 444}            # such as nums, strings, & tuples w/ immutables
          #"ab", "cd", "ef" : 555 }    # tuple need parentheses if in a dict
#print dict1
for word in dict1:
    print ("%s-%s" %(word, dict1[word]))
print "=============================================================" + '\n'
# ==================================================================
