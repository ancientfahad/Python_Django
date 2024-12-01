# ### Count how many 0's appear

# def countLoneZeroes(num):
#     count = 0
#     strNum = str(num)

#     for i in range(len(strNum)):
#         if(strNum[i] == '0'):
#             if(i == '0' and strNum[i+1] != '0'):
#                 count += 1
#             elif(strNum[i - 1] != '0' and strNum[i+1] != '0'):
#                 count += 1
    
#     print(count)

# def main():
#     num = int(input())
#     countLoneZeroes(num)

# if __name__ == "__main__":
#     main()

### Triplet Sum

def find_triplet_sum(arr, N, P):
    arr.sort()

    for i in range(N):
        left = i + 1
        right = N - 1

        while left < right:
            arrI = arr[i]
            arrLeft = arr[left]
            arrRight = arr[right]

            sum = arrI + arrLeft + arrRight

            if sum == P:
                return arrI, arrLeft, arrRight
            elif sum < P:
                left += 1
            else:
                right -= 1
    
    return None  # If no triplet is found

N = int(input())
arr = list(map(int, input().split()))
P = int(input())

result = find_triplet_sum(arr, N, P)

if result:
    print(" ".join(map(str, result)))
else:
    print("No triplet found")