# Given an array of integers, return a new array such that each element at index i of the new array
# is the 'product' of 'all' numbers in the original array except the one at i

def products(nums):
    # Generate prefix products. 
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products.
    suffix_products = [] 
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
        

    # Generate result from product of prefixes and suffixes. 
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(
                    prefix_products[i - 1] * suffix_products[i + 1]
            )        

    return result

print(products([4,3,4,5,6,7,8]))
