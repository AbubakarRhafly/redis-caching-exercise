import time
from weather_api import get_weather


start = time.time()
result1 = get_weather("Jakarta")
time1 = time.time() - start

print("Result 1:", result1)
print(f"First call: {time1:.2f}s")


start = time.time()
result2 = get_weather("Jakarta")
time2 = time.time() - start

print("Result 2:", result2)
print(f"Second call (cached): {time2:.2f}s")