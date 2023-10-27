def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    # Create a dataset of 30 names
    names = [
        "John",
        "Mary",
        "Robert",
        "Linda",
        "William",
        "Elizabeth",
        "James",
        "Susan",
        "David",
        "Patricia",
        "Richard",
        "Jessica",
        "Joseph",
        "Sarah",
        "Charles",
        "Karen",
        "Thomas",
        "Nancy",
        "Daniel",
        "Lisa",
        "Matthew",
        "Betty",
        "Anthony",
        "Dorothy",
        "Donald",
        "Sandra",
        "Mark",
        "Ashley",
        "Paul",
    ]
    
    print("Unsorted Names:")
    print(names)
    
    # Sort the names using bubble sort
    names.sort()
    
    print("Sorted Names:")
    print(names)