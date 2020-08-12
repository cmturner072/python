num_list = range(1, 11)

#want a set of cubed numbers

cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)


print(list(num_list))
#output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cubed_nums)
#output [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]