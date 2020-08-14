'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zeros = []
    non_zeros = []
    for num in arr:
        if num == 0:
            zeros.append(0)
        else:
            non_zeros.append(num)
    non_zeros.extend(zeros)
    return non_zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")