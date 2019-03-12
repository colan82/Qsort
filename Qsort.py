def IsEven(Num):
    return Num%2 == 0


def Qsort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = nums[len(nums)//2]
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return Qsort(l_nums) + e_nums + Qsort(b_nums)


length_of_array = int(input())
array = list(map(int, input().split()[:length_of_array]))
even_nums = []
odd_nums = []

for i in array:
    if IsEven(i):
        even_nums.append(i)
    else:
        odd_nums.append(i)

even_nums = Qsort(even_nums)
odd_nums = Qsort(odd_nums)

print(even_nums + odd_nums[::-1])
