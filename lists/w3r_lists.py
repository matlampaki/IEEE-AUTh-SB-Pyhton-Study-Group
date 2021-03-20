# 1 Write a Python program to sum all the items in a list

# def sum_list(items):
#     sum = 0;
#     for x in items:
#         sum += x
#     return sum
#
# a = [1,2,-8]
# print(sum_list(a))

# 2  Write a Python program to multiplies all the items in a list.

# def mul_list(items):
#     product = 1;
#     for x in items:
#         product *= x
#     return product
#
# a = [1, 2, -8, -2]
# print(mul_list(a))


# 4 Write a Python program to get the smallest number from a list.

# def min_list(items):
#     min_item = min(items)
#     return min_item
#
# a = [1, 2, -8, -2]
# print(min_list(a))

# 5  Write a Python program to count the number of strings where the string length is 2 or more and the first and ...
# last character are same from a given list of strings.

# Sample_List = ['abc', 'xyz', 'aba', '1221']
#
# def num_of_words(words):
#     counter = 0
#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             counter += 1
#     return counter
#
# print(num_of_words(Sample_List))

# 7. Write a Python program to remove duplicates from a list.

# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
#
#
# def remove_dup(words):
#     dup_items = set()
#     uni_items = []
#     for word in words:
#         if word not in uni_items:
#             uni_items.append(word)
#             dup_items.add(word)
#     return [uni_items, dup_items]
#
#
# print(remove_dup(a))
