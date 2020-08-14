'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # dictionary to hold the values
    if len(arr) == 1:
        return arr[0]
    values = {}
    for num in arr:
        if str(num) in values:
            del values[str(num)]
        else:
            values[str(num)] = num
    for k, v in values.items():
        return v


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
