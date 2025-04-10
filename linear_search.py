def linear_search(arr, target):
    print(f"Searching for {target} in {arr}")
    for i, val in enumerate(arr):
        print(f"Checking index {i}: {val}")
        if val == target:
            print(f"Found {target} at index {i}")
            return i
    print(f"{target} not found in the array.")
    return -1


# Example usage
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    target = int(input("Enter the number to search for: "))
    linear_search(arr, target)
