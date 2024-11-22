#Dictionary


#1
#dict = {'a': 1, 'b': 2}
#print(dict.get('b'))

#2
#dict = {'a': 1, 'b': 2}
#print('a'in dict)

#3
#dict = {'a': 1, 'b': 2}
#print(len(dict))

#4
#dict = {'a': 1, 'b': 2}
#print(list(dict.keys()))

#5
#dict = {'a': 1, 'b': 2}
#print(list(dict.values()))

#6
#dict1 = {'a': 1, 'b': 2}
#dict2 = {'b': 3, 'c': 4}
#print({**dict1, **dict2})

#7
#dict = {'a': 1, 'b': 2}
#dict.pop('a')
#print(dict)

#8
#dict = {'a': 1, 'b': 2}
#dict.clear()
#print(dict)

#9
#dict = {}
#print(len(dict) == 0)

#10
#dict = {'a': 1, 'b': 2}
#print((dict['a']))

#11
#dict = {'a': 1, 'b': 2}
#dict['a'] = 3
#print(dict)

#12
#dict = {'a': 1, 'b': 2, 'c': 1}
#print(list(dict.values()).count(1))

#13
#dict = {'a': 1, 'b': 2}
#print({v: k for k, v in dict.items()})

#14
#dict = {'a': 1, 'b': 2, 'c': 1}
#print([k for k, v in dict.items() if v == 1])

#15
#print(dict(zip(['a', 'b'], [1, 2])))

#16
#def has_nested_dictionaries(input_dict):
   
    #return any(isinstance(value, dict) for value in input_dict.values())

#input_dict = {
    #"a": 1,
    #"b": {"nested_key": "nested_value"},
    #"c": 3,
#}

#result = has_nested_dictionaries(input_dict)
#print("Does the dictionary have nested dictionaries?", result)

#19
#dict = {'a': 1, 'b': 2, 'c': 1}
#print(len(set(dict.values())))

#20
#sample_dict = {'b': 2, 'a': 1, 'c': 3}
#print(dict(sorted(sample_dict.items())))

#21
#sample_dict = {'a': 3, 'b': 1, 'c': 2}
#sorted_by_value = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
#print(sorted_by_value)

#22
#sample_dict = {'a': 3, 'b': 1, 'c': 2}
#filtered_dict = {k: v for k, v in sample_dict.items() if v > 1}
#print(filtered_dict)

#23
#dict1 = {'a': 1, 'b': 2}
#dict2 = {'b': 3, 'c': 4}
#print(set(dict1.keys()) & set(dict2.keys()))

#24
#tuple_pairs = (('a', 1), ('b', 2))
#print(dict(tuple_pairs))

#25
#sample_dict = {'a': 1, 'b': 2}
#print(next(iter(sample_dict.items())))


#Tuples


#1
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#element = 2
#print("Count Occurrences:", #sample_tuple.count(element))


#2
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Max Element:", max(sample_tuple))

#3
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Min Element:", min(sample_tuple))

#4
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#element = 2
#print("Check Element:", element in sample_tuple)

#5
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("First Element:", sample_tuple[0] if #sample_tuple else None)

#6
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Last Element:", sample_tuple[-1])

#7
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Tuple Length:", len(sample_tuple))

#8
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Slice Tuple:", sample_tuple[:3])

#9
#tuple1 = (1, 2, 3)
#tuple2 = (4, 5, 6)
#print("Concatenate Tuples:", tuple1 + tuple2)

#10
#sample_tuple = ()
#print("Check if Tuple is Empty:", #len(sample_tuple) == 0)

#11
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#element = 4
#print("All Indices of Element:", [i for i, x in #enumerate(sample_tuple) if x == element])

#12
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Second Largest Element:", #sorted(set(sample_tuple))[-2])

#13
#sample_tuple = (1, 2, 2, 3, 4, 4, 5, 6)
#print("Second Smallest Element:", #sorted(set(sample_tuple))[1])

#14
#element = 42
#single_element_tuple = (element,)
#print("Single Element Tuple:", #single_element_tuple)

#15
#sample_list = [1, 2, 3, 4]
#print("Convert List to Tuple:", #tuple(sample_list))

#16
#sample_tuple = (1, 2, 3, 4, 5)
#print("Check if Tuple is Sorted:", sample_tuple == tuple(sorted(sample_tuple)))

#17
#sample_tuple = (1, 2, 3, 4, 5, 6)
#subtuple = sample_tuple[1:4]
#print("Max of Subtuple:", max(subtuple))

#18
#sample_tuple = (1, 2, 3, 4, 5, 6)
#subtuple = sample_tuple[1:4]
#print("Min of Subtuple:", min(subtuple))

#19
#def remove_element(input_tuple, element):
    #if element in input_tuple:
        #i = sample_tuple.i(element)
        #return sample_tuple[:i] + sample_tuple[i + 1:]
    #return sample_tuple 
#sample_tuple = (1, 2, 3, 4, 2, 5)
#element_to_remove = 2
#result = remove_element(sample_tuple, element_to_remove)
#print("Original tuple:", sample_tuple)
#print("Tuple after removing element: ", result)


#20
#def create_nested_tuple(sample_tuple, group_size):
    #if group_size <= 0:
        #raise ValueError("Group size must be greater than 0.")
    
    #nested_tuple = tuple(sample_tuple[i:i + group_size] for i in range(0, len(input_tuple), group_size))
    #return nested_tuple


#sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
#group_size = 3
#result = create_nested_tuple(sample_tuple, group_size)
#print("Original tuple:", sample_tuple)
#print("Nested tuple:", result)

#21
#def repeat_elements(sample_tuple, repeat_count):
    #if repeat_count <= 0:
        #raise ValueError("Repeat count must be greater than 0.")
    
    #repeated_tuple = tuple(element for element in sample_tuple for _ in range(repeat_count))
    #return repeated_tuple

#sample_tuple = (1, 2, 3)
#repeat_count = 3
#result = repeat_elements(sample_tuple, repeat_count)
#print("Original tuple:", sample_tuple)
#print("Repeated tuple:", result)

#22
#start, end = 1, 10
#print("Range Tuple:", tuple(range(start, end + 1)))

#23
#sample_tuple = (1, 2, 3, 4, 5)
#print("Reverse Tuple:", sample_tuple[::-1])

#24
#sample_tuple = (1, 2, 3, 2, 1)
#print("Check Palindrome:", sample_tuple == #sample_tuple[::-1])

#25
#def get_unique_elements(sample_tuple):
    #seen = set()
    #unique_elements = []
    #for i in sample_tuple:
        #if i not in seen:
            #seen.add(i) 

    #unique_elements.append(i)
    #return
    #tuple(unique_elements)

#sample_tuple = (1, 2, 2, 3, 4, 3, 5, 6, 5)
#result = get_unique_elements(sample_tuple)
#print("Original tuple:", sample_tuple)
#print("Tuple with unique elements: ", result)


#Lists

#1
#sample_list = [3, 4, 4, 5, 6, 7, 7, 8, 9]
#element = 4
#print("Count Occurrences:", sample_list.count(element))

#2
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Sum of Elements:", sum(sample_list))

#3
#sample_list = [ 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Max Element:", max(sample_list))

#4
#sample_list = [ 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Min Element:", min(sample_list))

#5
#sample_list = [ 3, 4, 4, 5, 6, 7, 7, 8, 9]
#element = 2
#print("Check Element:",  element in sample_list)

#6
#list = [ 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("First Element:", list[0] if list else None)

#7
#sample_list = [ 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Last Element:", sample_list[-1] if sample_list else None)

#8
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Slice List:", sample_list[:3])

#9
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Reverse List:", sample_list[::-1])

#10
#sample_list = [ 2, 3, 4, 4, 5, 6, 1, 12,  7, 7, 8, 9]
#print("Sort List:", sorted(sample_list))

#11
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Remove Duplicates:", list(set(sample_list)))

#12
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#element = 2
#print("Index of Element:", sample_list.index(element) if element in sample_list else -1)

#13
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#element = 2
#print("Index of Element:", sample_list.index(element) if element in sample_list else -1)

#14
#sample_list = []
#print("Check for Empty List:", len(sample_list) == 0)

#15
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Count Even Numbers:", sum(1 for x in sample_list if x % 2 == 0))

#16
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Count Odd Numbers:", sum(1 for x in sample_list if x % 2 != 0))

#19
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#sample_list[sample_list.index(3)] = 100
#print(sample_list)

#20
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Second Largest Element:", sorted(set(sample_list))[-2])

#21
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Second Smallest Element:", sorted(set(sample_list))[1])

#22
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Filter Even Numbers:", [x for x in sample_list if x % 2 == 0])

#23
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Filter Odd Numbers:", [x for x in sample_list if x % 2 != 0])

#24
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("List Length:", len(sample_list))

#25
#sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
#print("Create a Copy:", sample_list[:])

#26
#sample_list = [1, 2, 3, 4, 5]
#middle = len(sample_list) // 2
#if len(sample_list) % 2 == 0:
    #print("Middle Element:", sample_list[middle-1:middle+1])
#else:
    #print("Middle Element:", sample_list[middle])

#27
#my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#start = int(input("Enter the start index of the sublist: "))
#end = int(input("Enter the end index of the sublist: "))
#sublist = my_list[start:end+1]
#max_element = max(sublist)
#print("Maximum of sublist:", max_element)

#28
#my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#start = int(input("Enter the start index of the sublist: "))
#end = int(input("Enter the end index of the sublist: "))
#sublist = my_list[start:end+1]
#min_element = min(sublist)
#print("Minimum of sublist:", min_element)

#29
#my_list = input("Enter a list of elements separated by spaces: ").split()
#index = int(input("Enter the index to remove: "))
#if 0 <= index < len(my_list):
    #my_list.pop(index)
#print("List after removal:", my_list)

#30
#my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#is_sorted = my_list == sorted(my_list)
#print("Is the list sorted in ascending order?", is_sorted)

#31
#my_list = input("Enter a list of elements separated by spaces: ").split()
#repeat_count = int(input("Enter the number of times to repeat each element: "))
#repeated_list = [element for element in my_list for _ in range(repeat_count)]
#print("List with elements repeated:", repeated_list)

#32
#l1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
#l2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
#merged_sorted_list = sorted(l1 + l2)
#print("Merged and sorted list:", merged_sorted_list)

#33
#list = input("Enter a list of elements separated by spaces: ").split()
#element = input("Enter the element to find indices for: ")
#indices = [index for index, value in enumerate(list) if value == element]
#print(f"Indices of element '{element}':", indices)

#34
#list = input("Enter a list of elements separated by spaces: ").split()
#shift = int(input("Enter the number of positions to rotate right: "))
#rotated_list = list[-shift:] + list[:-shift]
#print("Rotated list:", rotated_list)

#35
#start = int(input("Enter the start of the range: "))
#end = int(input("Enter the end of the range: "))
#range_list = list(range(start, end + 1))
#print("Range list:", range_list)

#36
#my_list = list(map(int, input("Enter a list of negative numbers separated by spaces: ").split()))
#negative_sum = sum(num for num in my_list if num < 0)
#print("Sum of negative numbers:", negative_sum)

#37
#my_list = list(map(int, input("Enter a list of negative numbers separated by spaces: ").split()))
#negative_sum = sum(num for num in my_list if num < 0)
#print("Sum of negative numbers:", negative_sum)

#38
#list = input("Enter a list of elements separated by spaces: ").split()
#is_palindrome = list == list[::-1]
#print("Is the list a palindrome?", is_palindrome)

#39
#list = input("Enter a list of elements separated by spaces: ").split()
#size = int(input("Enter the number of elements per sublist: "))
#nested_list = [list[i:i + size] for i in range(0, len(list), size)]
#print("Nested list:", nested_list)

#40
#list = input("Enter a list of elements separated by spaces: ").split()
#unique_list = []
#[unique_list.append(item) for item in list if item not in unique_list]
#print("List with unique elements in order:", unique_list)

#Sets

#import random

#def union_of_sets(set1, set2):
    #return set1 | set2
#print(union_of_sets(sample_set1, sample_set2))

#def intersection_of_sets(set1, set2):
    #return set1 & set2
#print(intersection_of_sets(sample_set1, sample_set2))

#def difference_of_sets(set1, set2):
    #return set1 - set2
#print(difference_of_sets(sample_set1, sample_set2))

#def check_subset(set1, set2):
    #return set1 <= set2 or set2 <= set1
#print(check_subset(sample_set1, sample_set2))

#def check_element(s, element):
    #return element in s
#print(check_element(sample_set1, 3))

#def set_length(s):
    #return len(s)
#print(set_length(sample_set1))

#def convert_list_to_set(lst):
    #return set(lst)
#print(convert_list_to_set(sample_list))

#def remove_element(s, element):
    #s.discard(element)
    #return s
#print(remove_element(sample_set1.copy(), 2))

#def clear_set(s):
    #return set()
#print(clear_set(sample_set1))

#def is_set_empty(s):
    #return len(s) == 0
#print(is_set_empty(sample_set1))

#def symmetric_difference(set1, set2):
    #return set1 ^ set2
#print(symmetric_difference(sample_set1, sample_set2))

#def add_element(s, element):
    #s.add(element)
    #return s
#print(add_element(sample_set1.copy(), 9))

#def pop_element(s):
    #return s.pop() if s else None
#print(pop_element(sample_set1.copy()))

#def find_maximum(s):
    #return max(s) if s else None
#print(find_maximum(sample_set1))

#def find_minimum(s):
    #return min(s) if s else None
#print(find_minimum(sample_set1))

#def filter_even_numbers(s):
    #return {x for x in s if x % 2 == 0}
#print(filter_even_numbers(sample_set1))

#def filter_odd_numbers(s):
    #return {x for x in s if x % 2 != 0}
#print(filter_odd_numbers(sample_set1))

#def create_set_of_range(start, end):
    #return set(range(start, end + 1))
#print(create_set_of_range(1, 10))

#def merge_and_deduplicate(lst1, lst2):
    #return set(lst1 + lst2)
#print(merge_and_deduplicate(sample_list, [4, 5, 6, 7]))

#def check_disjoint_sets(set1, set2):
    #return set1.isdisjoint(set2)
#print(check_disjoint_sets(sample_set1, sample_set2))

#def remove_duplicates_from_list(lst):
    #return list(set(lst))
#print(remove_duplicates_from_list(sample_list))

#def get_unique_elements_in_order(lst):
    #seen = set()
    #return [x for x in lst if not (x in seen or seen.add(x))]
#print(get_unique_elements_in_order(sample_list))

#def create_nested_sets(*args):
    #return {frozenset(arg) for arg in args}
#print(create_nested_sets({1, 2}, {3, 4}, {5}))

#def count_unique_elements(lst):
    #return len(set(lst))
#print(count_unique_elements(sample_list))

#def generate_random_set(size, start, end):
    #return {random.randint(start, end) for _ in range(size)}
#print(generate_random_set(5, 1, 10))

#sample_set1 = {1, 2, 3, 4, 5}
#sample_set2 = {4, 5, 6, 7, 8}
#sample_list = [1, 2, 2, 3, 4, 4, 5]


