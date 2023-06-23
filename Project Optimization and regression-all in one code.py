#Ruba Alsulami - 2110618 , Arjwan Alharbi 2110826

# Greedy Knapsack Algorithm which returns the maximum value and which items are selected in terms of a binary list
def knapsack_greedy(weights, values, capacity):
    # Creating a list of tuples with items, their values, and weights
    items = list(zip(values, weights))
    # Sorting the items based on the value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0  # The Total value of items picked
    total_weight = 0  # The Total weight of items picked
    picked_items = []  # The List to store the items picked

    for value, weight in items:
        if total_weight + weight <= capacity:
            # If the current item can be picked without exceeding the capacity,
            # pick it
            picked_items.append(1)  # Add 1 to indicate the item was picked
            total_value += value
            total_weight += weight
        else:
            picked_items.append(0)  # Add 0 to indicate the item was not picked

    return total_value, total_weight, picked_items


def exhaustive_search_knapsack(C, W, V):
    N = len(W) # Get the number of items
    P = [0] * N # Initialize a list of 0s with length equal to the number of items
    maxValue = 0 # Initialize the maximum value and weight to 0
    maxWeight = 0
    # Iterate over all possible subsets of items
    for i in range(1 << N):
        weight = 0 # Initialize the weight and value of the current subset to 0
        value = 0
        # Iterate over all items in the subset and calculate their total weight and value
        for j in range(N):
            if (i & (1 << j)) != 0:
                weight += W[j]
                value += V[j]
        # If the total weight of the subset is less than or equal to the capacity of the knapsack
        # and its value is greater than the maximum value seen so far, update the maximum value,
        # maximum weight, and the list of picked items
        if weight <= C and value > maxValue:
            maxValue = value
            maxWeight = weight
            for j in range(N):
                P[j] = 1 if (i & (1 << j)) != 0 else 0
    # Return a list containing the maximum value, maximum weight, and the list of picked items
    return [maxValue , maxWeight] + P

# Prompting the user to enter the capacity, weights,number of items, and values
capacity = float(input("\nEnter the capacity of the knapsack:- "))
print("\n")
n = int(input("Enter the total number of items:- "))
print("\n ENTER WEIGHT")
weights = [float(input("Enter the weight of item %d:- " % (i + 1))) for i in range(n)]
print("\n ENTER VALUE")
values = [float(input("Enter the value of item %d:- " % (i + 1))) for i in range(n)]

# Calling the function and printing the results
result = exhaustive_search_knapsack(capacity, weights, values)
print("\nItems picked in Exhaustive:", result[2:])
print("Total value:", result[0])
print("Total weight:", result[1])
print("\n")

# Calling the function and printing the results
result2 = knapsack_greedy(weights, values, capacity)
print("\nItems picked in Greedy:", result2[2:])
print("Total value:", result2[0])
print("Total weight:", result2[1])
print("\n")

# Calculate the percentage error
percentageError = abs(result2[0] - result[0]) / result[0] * 100
print("Percentage Error:", percentageError, "%")

# Calculate the percentage correct
percentageCorrect = (result2[0] * 100) / result[0]
print("Percentage Correct:", percentageCorrect, "%")
