# prepare function
def prepare(values, low, high):
    pivot = values[high] 
    el = low - 1

    for i in range(low, high):
        if values[i] <= pivot: 
            el = el + 1
            (values[el], values[i]) = (values[i], values[el]) # swaps elements

    (values[el + 1], values[high]) = (values[high], values[el + 1]) # swaps elements

    return el + 1

# recursive quick sort function
def quick_sort(values, low, high):
    if low < high:
        pivot = prepare(values, low, high)

        quick_sort(values, low, pivot-1)

        quick_sort(values, pivot+1, high)

values = [1, 3, 5, 4, 2, -1, -3, -2, -5, -4, 0]
total_values = len(values)

print("Pre-sort: ", values)

quick_sort(values, 0, total_values-1)

print("Post-sort: ", values)
