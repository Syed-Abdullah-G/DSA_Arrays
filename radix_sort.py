def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    print(f"Count array for exp={exp}: {count}")

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    print(f"Array after sorting with exp={exp}: {arr}")


def radix_sort(arr):
    print(f"Original array: {arr}")
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    print(f"\nSorted array: {arr}")


# Example usage
if __name__ == "__main__":
    user_input = input("Enter non-negative numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    radix_sort(arr)
