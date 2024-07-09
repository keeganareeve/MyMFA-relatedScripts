'''
Script generates a random seed that can be used in another script in conjunction with the random.seed() function.

---------------------------------------------------------------------

Prompt to GPT-3:
give me a random sequence of letters and numbers and possibly special characters

'''

import random
import string

# Generate a random seed consisting of letters, numbers, and special characters
random_seed = ''.join(random.choices(
    string.ascii_letters + string.digits + string.punctuation, k=20))

# Set the random seed
random.seed(random_seed)

# Example usage to demonstrate the effect of the seed
print(f"Random seed chosen: {random_seed}")
print(f"Random number generated with this seed: {random.random()}")
