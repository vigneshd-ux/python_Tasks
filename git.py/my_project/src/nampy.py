import numpy as np

def marks_analysis(lst):

    marks = np.array(lst)

    print("Marks:", marks)
    print("Mean:", np.mean(marks))
    print("Median:", np.median(marks))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
    print("Standard Deviation:", np.std(marks))


marks_analysis([78, 85, 92, 67, 88, 74, 95, 81])