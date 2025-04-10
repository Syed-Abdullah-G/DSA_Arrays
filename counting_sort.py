def counting_sort(arr):
    print(f"Original array: {arr}")
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
    print(f"Count array after counting: {count}")

    index = 0
    for i, c in enumerate(count):
        while c > 0:
            arr[index] = i
            print(f"Placing {i} at index {index}")
            index += 1
            c -= 1

    print(f"\nSorted array: {arr}")


# Example usage
if __name__ == "__main__":
    user_input = input("Enter non-negative numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    counting_sort(arr)
