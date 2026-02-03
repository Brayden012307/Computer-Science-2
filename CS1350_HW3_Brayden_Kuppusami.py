import numpy as np

print("===========================================")
print("--- Problem 1 ---")
print("===========================================")
zeros_arr = np.zeros(8) 
ones_matrix = np.ones((3, 4)) 
range_arr = np.arange(10, 51, 5) 
linear_arr = np.linspace(0, 2, 9) 

print(f"zeros_arr:\n{zeros_arr}")
print(f"ones_matrix:\n{ones_matrix}")
print(f"range_arr:\n{range_arr}")
print(f"linear_arr:\n{linear_arr}")


a = np.array([2, 4, 6, 8, 10]) 
b = np.array([1, 2, 3, 4, 5]) 
print(f"a + b: {a + b}") 
print(f"a * b: {a * b}") 
print(f"a^2: {a**2}") 
print(f"a / b: {a / b}") 
print(f"Sum of a: {np.sum(a)}") 
print(f"Mean of b: {np.mean(b)}") 

print("===========================================")
print("--- Problem 2 ---")
print("===========================================")
matrix_20 = np.arange(1, 21).reshape(4, 5) 
print(f"Matrix:\n{matrix_20}") 
print(f"Shape: {matrix_20.shape}") 
print(f"Dimensions: {matrix_20.ndim}") 
print(f"Total elements: {matrix_20.size}") 
print(f"Data type: {matrix_20.dtype}") 
print(f"Total bytes: {matrix_20.nbytes}") 


print(f"Overall Mean: {np.mean(matrix_20)}") 
print(f"Overall Std Dev: {np.std(matrix_20)}") 
print(f"Min: {np.min(matrix_20)}, Max: {np.max(matrix_20)}") 
print(f"Row sums: {np.sum(matrix_20, axis=1)}") 
print(f"Column means: {np.mean(matrix_20, axis=0)}") 
print(f"Index of max (flattened): {np.argmax(matrix_20)}") 

print("===========================================")
print("--- Problem 3 ---")
print("===========================================")
scores = np.array([
    [85, 90, 78, 92], # Alice
    [70, 65, 72, 68], # Bob
    [95, 98, 94, 97], # Carol
    [60, 55, 58, 62], # Dave
    [88, 85, 90, 87], # Eve
    [75, 80, 77, 82]  # Frank
]) 
students = np.array(['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']) 


print(f"Carol Exam2: {scores[2, 1]}") 
print(f"Alice scores: {scores[0, :]}") 
print(f"Exam 3 scores: {scores[:, 2]}") 
print(f"Submatrix (Bob/Carol, Exam 1/2):\n{scores[1:3, 0:2]}") 


mask_90 = scores >= 90 
print(f"Scores >= 90: {scores[mask_90]}") 
print(f"Count >= 90: {np.sum(mask_90)}") 
avg_scores = np.mean(scores, axis=1)
print(f"Students with avg >= 85: {students[avg_scores >= 85]}") 
scores[scores < 60] = 60 
print(f"Modified scores (min 60):\n{scores}")

print("===========================================")
print("--- Problem 4 ---")
print("===========================================")
arr_24 = np.arange(1, 25) 
mat_4x6 = arr_24.reshape(4, 6) 
arr_3d = arr_24.reshape(2, 3, 4) 
flattened = arr_3d.ravel() 

print(f"Original array: {arr_24}")
print(f"Reshaped to 4x6:\n{mat_4x6}")
print(f"Reshaped to 2x3x4:\n{arr_3d}")
print(f"Flattened: {flattened}")


prices = np.array([
    [1.20, 1.50, 1.30, 1.40],
    [0.50, 0.60, 0.55, 0.45],
    [0.80, 0.90, 0.85, 0.75]
])


discounted = prices * 0.9 
with_fee = prices + 0.10 
tax_rates = np.array([0.08, 0.05, 0.07, 0.05]) 
final_prices = prices * (1 + tax_rates) 
normalized = prices - np.mean(prices, axis=1, keepdims=True) 

print(f"Final prices with tax:\n{final_prices}")

print("===========================================")