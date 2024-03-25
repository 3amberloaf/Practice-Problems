# In a game called Fruit Crush, you can choose two dissimilar fruits and crush them. Each fruit is represented by an integer in an array. 
# Given an array 'Fruit' of size n, return the minimum number of fruits left after a given operation is performed a number of times. 

# Constraints: 1 <= n <= 10^5

def getMinimumFruits(fruits):
    
    # Count the fruit
    fruit_counts = {} # Initialize an empty dictionary
    for fruit in fruits: # Iterate through dictionary, variable 'fruit' takes on the value of each item as the loop iterates
        if fruit in fruit_counts:
            fruit_counts[fruit] += 1
        else:
            fruit_counts[fruit] = 1
    
    even_count_fruits = sum(1 for count in fruit_counts.values() if count % 2 == 0)
    """ sums the fruit counts who have an even modulo"""
    
    min_fruits_left = max(1, even_count_fruits) if even_count_fruits > 0 else 0
    
    return min_fruits_left

# Example usage
n = 5
fruits = [1, 2, 5, 6, 6, 6, 6]
result = getMinimumFruits(fruits)
print(result)
