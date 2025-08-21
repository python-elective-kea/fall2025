# procedual style
# Import the module
import counter_module as cm1

# Increment and get the count
print(cm1.increment())  # Output: 1
print(cm1.increment())  # Output: 2

# Simulate another "instance" of the counter
# This is not possible directly, but let's pretend we want a separate counter
import counter_module as cm2
print(cm2.increment())  # Output: 3, but we wanted a separate counter starting from 0


#########################
# OOP style
# Import the class
from counter_class import Counter

# Create two separate counter instances
counter1 = Counter()
counter2 = Counter()

# Increment and get the count for counter1
print(f'Counter1: {counter1.increment()}')  # Output: 1
print(f'Counter1: {counter1.increment()}')  # Output: 2

# Increment and get the count for counter2
print(f'Counter2: {counter2.increment()}')  # Output: 1, as expected for a separate counter

