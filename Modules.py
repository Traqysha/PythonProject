import math
import statistics
from mymodule import x, y
import mymodule

mymodule.shule("eMobilis Mobile Technology")

print("Addition", mymodule.x + mymodule.y)
print("Subtraction", mymodule.x - mymodule.y)
print("Multiplication", mymodule.x * mymodule.y)
print("Division", mymodule.x / mymodule.y)
# This are inbuilt modules

print(math.sqrt(25))
dataset = (6, 2, 14, 78, 4, 7, 10, 45, 67)
x = statistics.mean(dataset)
print("mean is ", x)

x = statistics.mode(dataset)
print("mode is ", x)

x = statistics.median(dataset)
print("median is", x)

x = statistics.median_low(dataset)
print("median_low is", x)

print(x+y)
