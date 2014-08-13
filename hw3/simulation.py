import selection_sort  # Import the selection_sort module
import merge_sort  # Import the merge_sort module
import quick_sort  # Import the quick_sort module
import random
import timeit
import matplotlib.pyplot as plt

def iterations(sort_type, n):  # This function sorts randomly generated numbers of length n that range from -500 to 500
	if sort_type == "selection sort":
		selection_sort.selection_sort([random.randint(-500,500) for number in range(n)])
	elif sort_type == "merge sort":
		merge_sort.merge_sort([random.randint(-500,500) for number in range(n)])
	elif sort_type == "quick sort":
		quick_sort.quick_sort([random.randint(-500,500) for number in range(n)])

time_selection = []
for n in range(1,1000):
	t = timeit.Timer('iterations("selection sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_selection.append(t)

time_merge = []
for n in range(1,1000):
	t = timeit.Timer('iterations("merge sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_merge.append(t)

time_quick = []
for n in range(1,1000):
	t = timeit.Timer('iterations("quick sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_quick.append(t)

plt.figure()  # Open a figure to plot

plt.plot(range(1,1000), time_selection, label="selection sort: O(n^2)")
plt.plot(range(1,1000), time_merge, label="merge sort: O(nlogn)")
plt.plot(range(1,1000), time_quick, label="quick sort: O(nlogn) - average")
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Runtime by Size")
plt.legend(loc="upper left") 

plt.savefig("runtime_by_size.pdf")