def compute_average(grades):
    grades.sort()
    return sum(grades[1:4])/3


### Solution:

def compute_average(grades):
    grades.sort()
    return sum(grades[1:4])/3


### Explanation:
#The function takes a list of grades as an argument. The list is sorted in ascending order. The function then returns the average of the grades excluding the highest and lowest grades. The average is computed by summing the grades from index 1 to index 3 and dividing by 3.
