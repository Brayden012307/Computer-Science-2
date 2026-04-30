print("QUESTION 1")
def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    
    if n <= 1:
        return n
    
    
    return n + sum_natural(n - 1)


print(f"sum_natural(5): {sum_natural(5)}")   
print(f"sum_natural(10): {sum_natural(10)}") 
print(f"sum_natural(1): {sum_natural(1)}")   

def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """
    
    if n < 10:
        return 1
    
    
    return 1 + count_digits(n // 10)


print(f"count_digits(1234): {count_digits(1234)}")      
print(f"count_digits(987654321): {count_digits(987654321)}") 
print(f"count_digits(5): {count_digits(5)}")            

def is_palindrome(s):
    """
    Check if string s is a palindrome recursively.
    Ignore case and consider only alphanumeric characters.
    """
    
    def check_recursive(clean_s):
        
        if len(clean_s) <= 1:
            return True
        
        
        if clean_s[0] != clean_s[-1]:
            return False
        
        
        return check_recursive(clean_s[1:-1])

    
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    return check_recursive(cleaned)


print(f"is_palindrome('racecar'): {is_palindrome('racecar')}") 
print(f"is_palindrome('hello'): {is_palindrome('hello')}")     
print(f"is_palindrome('a'): {is_palindrome('a')}")             
print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}") 
print(f"is_palindrome('race a car'): {is_palindrome('race a car')}") 

def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    """
    
    if n == 0:
        return 1
    
    
    return x * power(x, n - 1)


print(f"power(2, 5): {power(2, 5)}")   
print(f"power(3, 0): {power(3, 0)}")   
print(f"power(5, 3): {power(5, 3)}")  

def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    """
    results = []

    def helper(current_string):
        
        if len(current_string) == n:
            results.append(current_string)
            return
        
        
        helper(current_string + '0')
        helper(current_string + '1')

    helper("")
    return results


print(f"generate_binary_strings(2): {generate_binary_strings(2)}") 

print(f"generate_binary_strings(1): {generate_binary_strings(1)}") 


def subset_sum(nums, target):
    """
    Check if any subset of nums adds up to target.
    """
    def solve(index, current_target):
        
        if current_target == 0:
            return True
        
        if index == len(nums) or current_target < 0:
            return False
        
        
        include = solve(index + 1, current_target - nums[index])
        
        
        exclude = solve(index + 1, current_target)
        
        
        return include or exclude

    return solve(0, target)


print(f"subset_sum([3, 34, 4, 12, 5, 2], 9): {subset_sum([3, 34, 4, 12, 5, 2], 9)}") 


print(f"subset_sum([1, 2, 3, 4], 10): {subset_sum([1, 2, 3, 4], 10)}") 


print(f"subset_sum([1, 2, 3], 7): {subset_sum([1, 2, 3], 7)}") 

print("PART V")

"""
Analysis of recursive_sum:
1. Recurrence Relation:
T(n) = T(n-1) + O(1)
T(0) = O(1)
2. Time Complexity: O(n)
- Makes n recursive calls
- Each call does O(1) work
- Total: n * O(1) = O(n)
3. Space Complexity: O(n)
- Maximum stack depth is n
- Each frame uses O(1) space
- Total: n * O(1) = O(n)
4. Recursion Tree:
recursive_sum([1,2,3,4], 4)
├── 4 + recursive_sum([1,2,3,4], 3)
├── 3 + recursive_sum([1,2,3,4], 2)
├── 2 + recursive_sum([1,2,3,4], 1)
├── 1 + recursive_sum([1,2,3,4], 0)
└── 0 (base case)

"""

def binary_search(arr, target, left, right):
    """
    Search for target in sorted array arr[left:right+1].
    Return index if found, -1 otherwise.
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


test_arr = [1, 2, 3, 4, 5, 10, 20]
print(f"Binary Search (target 10): {binary_search(test_arr, 10, 0, len(test_arr)-1)}") 
print(f"Binary Search (target 7): {binary_search(test_arr, 7, 0, len(test_arr)-1)}")   

def edit_distance(s1, s2):
    """
    Find minimum edit distance between s1 and s2 using memoization.
    """
    memo = {}

    def solve(i, j):
        
        if i == 0: return j
        if j == 0: return i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        
        if s1[i-1] == s2[j-1]:
            res = solve(i-1, j-1)
        else:
            
            res = 1 + min(
                solve(i, j-1),    
                solve(i-1, j),    
                solve(i-1, j-1)   
            )
        
        memo[(i, j)] = res
        return res

    return solve(len(s1), len(s2))


print(f"Edit Distance ('cat', 'cut'): {edit_distance('cat', 'cut')}")           
print(f"Edit Distance ('sunday', 'saturday'): {edit_distance('sunday', 'saturday')}") 

if __name__ == "__main__":
    
    arr_sum = [1, 2, 3, 4]
    def recursive_sum(arr, n):
        if n <= 0: return 0
        return arr[n-1] + recursive_sum(arr, n-1)
    print(f"Recursive Sum: {recursive_sum(arr_sum, 4)}") 

    
    arr_bin = [10, 20, 30, 40, 50]
    print(f"Binary Search (30): {binary_search(arr_bin, 30, 0, 4)}") 

    
    print(f"Edit Distance: {edit_distance('kitten', 'sitting')}") 

print("QUESTION 2")

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result


random_list = [random.randint(1, 1000000) for _ in range(1000000)]


print("Starting merge sort on 1,000,000 integers...")
start_time = time.time()
sorted_list = merge_sort(random_list)
end_time = time.time()

print(f"Sort completed in {end_time - start_time:.2f} seconds.")
    
"""
Merge Sort is highly efficient because it uses a Divide and Conquer strategy that breaks a large, 
unsorted list into single-element sub-lists that are sorted by default. 
It then merges these sub-lists back together in a specific order, 
which is computationally much cheaper than repeatedly searching through the entire unsorted mass. 
This results in a time complexity of O(nlogn), where n represents the number of elements being merged 
and logn represents the number of times the list is split in half. 
Unlike simpler algorithms that slow down drastically as data grows, 
Merge Sort's consistent performance makes it ideal for handling massive datasets
"""


