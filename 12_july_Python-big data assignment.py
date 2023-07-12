#!/usr/bin/env python
# coding: utf-8

# Assignment 1 - (Python)
# 1. Write a Python program to check if a given string is an anagram.
# 2. Write a Python program to find the maximum and minimum values in a
# dictionary.
# 3. Write a Python program to find the average of a list of numbers.
# 4. Write a Python program to remove all vowels from a string.
# 5. Write a Python function to calculate the factorial of a number using recursion.
# 6. Write a Python program to merge two unsorted lists into a single sorted list
# using the merge sort algorithm.
# 7. Write a Python program to find the GCD (Greatest Common Divisor) of two
# numbers.
# 8. Write a Python program to find the second-largest element in a list.
# 9. Write a Python program to find the longest common subsequence between two
# strings using dynamic programming.
# 

# In[2]:


#1ANS


def is_anagram(str1, str2):
    # Convert strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in each string and compare them
    return sorted(str1) == sorted(str2)

# Example usage
str1 = "Listen"
str2 = "Silent"
if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")




# In[3]:


#2ANS
def find_max_min_values(d):
    # Get the values from the dictionary
    values = list(d.values())

    # Find the maximum and minimum values
    max_value = max(values)
    min_value = min(values)

    return (max_value, min_value)

# Example usage
d = {"a": 10, "b": 5, "c": 20}
max_value, min_value = find_max_min_values(d)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")


# In[4]:


#3ANS
def find_average(numbers):
    # Calculate the sum of the numbers
    total = sum(numbers)

    # Calculate the number of numbers
    count = len(numbers)

    # Calculate the average
    average = total / count

    return average

# Example usage
numbers = [1, 2, 3, 4, 5]
average = find_average(numbers)
print(f"Average: {average}")


# In[5]:


#4ANS
def remove_vowels(s):
    # Define a list of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Remove the vowels from the string
    result = ""
    for char in s:
        if char.lower() not in vowels:
            result += char

    return result

# Example usage
s = "Hello, World!"
result = remove_vowels(s)
print(result)


# In[6]:


#5ANS
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
n = 5
result = factorial(n)
print(f"{n}! = {result}")


# In[7]:


#6ANS
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def merge_lists(list1, list2):
    # Merge the two lists into a single list
    merged_list = list1 + list2

    # Sort the merged list using the merge sort algorithm
    merge_sort(merged_list)

    return merged_list

# Example usage
list1 = [3, 5, 2, 8, 4]
list2 = [9, 6, 1, 7, 0]
merged_list = merge_lists(list1, list2)
print(merged_list)


# In[8]:


#7ANS
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
a = 12
b = 18
result = gcd(a, b)
print(f"GCD({a}, {b}) = {result}")


# In[9]:


#8ANS
def find_second_largest(numbers):
    # Find the maximum value
    max_value = max(numbers)

    # Remove the maximum value from the list
    numbers.remove(max_value)

    # Find the new maximum value
    second_max_value = max(numbers)

    return second_max_value

# Example usage
numbers = [3, 5, 2, 8, 4]
second_largest = find_second_largest(numbers)
print(f"Second largest element: {second_largest}")


# In[10]:


#9ANS
def lcs(s1, s2):
    # Create a 2D array to store the lengths of the LCSs
    m = len(s1)
    n = len(s2)
    lcs_lengths = [[0] * (n+1) for i in range(m+1)]

    # Compute the lengths of the LCSs
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                lcs_lengths[i][j] = lcs_lengths[i-1][j-1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i-1][j], lcs_lengths[i][j-1])

    # Construct the LCS from the lengths
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_lengths[i-1][j] > lcs_lengths[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
s1 = "ABCDGH"
s2 = "AEDFHR"
result = lcs(s1, s2)
print(f"Longest common subsequence: {result}")


# In[ ]:




