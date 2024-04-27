import numpy as np 
import searchUtilsTeam06 as search

testArraySorted = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float64).reshape(-1,1)
testArrayUnsorted = np.array([8, 6, 7, 5, 3, 0, 9, 2, 1, 4], dtype=np.float64).reshape(-1,1)

print(np.shape(testArraySorted))

test1 = search.searchutils.linearsearch(testArraySorted,5)
test2 = search.searchutils.linearsearch(testArrayUnsorted,5)
test3 = search.searchutils.binarysearch(testArraySorted,5)

print("Linear Sorted: ", test1)
print("Linear Unsorted: ", test2)
print("Binary Sorted: ", test3)



