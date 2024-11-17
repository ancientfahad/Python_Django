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

def tripletSum(size, array_num, sum):
    
    arr = []

    for i in range(size):
        arr.append(array_num.split()[i])
    
    arr.sort()

    current_sum = 0

    for i in range(size):
        left = i - 1
        right = i + 1

        current_sum = i + left + right

        if (current_sum == sum):
            print('Yay')    

def main():
    size = int(input())
    array_num = input()
    sum = int(input())

    tripletSum(size, array_num, sum)

if __name__ == "__main__":
    main()