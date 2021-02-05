## Q. Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter.
## This function should return the sum of the values of all even keys.
# # 디버깅, indent 때문
# def sum_even_keys(my_dictionary):
#     su=0
#     for key,value in my_dictionary.items():
#         if (key%2)==0:
#             sum+=value
#             return (key, value)
#     return su
# print(sum_even_keys({1:2, 2:3}))
# #viewcode
# def sum_even_keys(my_dictionary):
#   total = 0
#   for key in my_dictionary.keys():
#     if key%2 == 0:
#       total += my_dictionary[key]
#   return total

# Q.
# def add_ten(my_dictionary):
#     for key in my_dictionary.keys():
#         my_dictionary[key]+=10
#     return my_dictionary


# Q.Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.
# # MY SOLUTION : FOR 문 2번, 비효율
# def values_that_are_keys(my_dictionary):
#     li=[]
#     for key in my_dictionary.keys():
#         for value in my_dictionary.values():
#             if key==value:
#                 li.append(key)
#     return li
#
# #SOLUTION BETTER
# # Write your values_that_are_keys function here:
# def values_that_are_keys(my_dictionary):
#   value_keys = []
#   for value in my_dictionary.values():
#     if value in my_dictionary: #FOR문 2번 안돌고도 바로 딕셔너리 키값 에 있는지 확인 가능!!!!!
#       value_keys.append(value)
#   return value_keys
#
# # Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# # should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# # should print ["a"]


# (Q.) The function should return the key associated with the largest value in the dictionary.
# def max_key(my_dictionary) :
#     valuemax= max(my_dictionary.values())
#     for i in my_dictionary.keys():
#         if my_dictionary[i]==valuemax:
#             return i
# #
# def max_key(my_dictionary):
#   largest_key = float("-inf")
#   largest_value = float("-inf")
#   for key, value in my_dictionary.items():
#     if value > largest_value:
#       largest_value = value
#       largest_key = key
#   return largest_key


#Q
# def word_length_dictionary(words):
#     dic={}
#     for a in words:
#         dic[a]=len(a)
#     return dic


# Q. The function should return a dictionary containing the frequency of
# each element in words.
 # 디버깅 #
# def frequency_dictionary(words):
#     dic={}
#     for a in words:
#         if dic[a] in dic : #dic[a] >= 1:
#             dic[a]+=1
#         else:
#             dic[a]=1
#     return dic
#             #(dic[a] in dic)

# 해결
# def frequency_dictionary(words):
#     dic = {}
#     for word in words:
#         if word in dic.keys():
#             dic[word]+=1
#         else:
#             dic[word]=1
#     return dic
#
# # SOLUTION
# # Write your frequency_dictionary function here:
# def frequency_dictionary(words):
#   freqs = {}
#   for word in words:
#     if word not in freqs:
#     	freqs[word] = 0
#     freqs[word] += 1
#   return freqs

# # Uncomment these function calls to test your  function:
# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# # should print {"apple":2, "cat":1, 1:1}
# print(frequency_dictionary([0,0,0,0,0]))
# # should print {0:5}

# (Q.)  The function should return the number of unique values in the dictionary.
# def unique_values(my_dictionary):
#   seen_values = []
#   for value in my_dictionary.values():
#     if value not in seen_values:
#       seen_values.append(value)
#   return len(seen_values)

# (Q.) Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
# So in example above, the function would return:
# {"S" : 4, "L": 3}

#MY
# def count_first_letter(names):
#     dic={}
#     for a in names :
#         if a[0] in dic:
#             dic[a[0]]+=len(names[a])
#         else:
#             dic[a[0]]=len(names[a])
#     return dic

#SOLUTION
# def count_first_letter(names):
#   letters = {}
#   for key in names:
#     first_letter = key[0]
#     if first_letter not in letters:
#       letters[first_letter] = 0
#     letters[first_letter] += len(names[key])
#   return letters
