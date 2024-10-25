import math

# for i in range(1, 256):
#     print(int("ff" * i, 16))

# for power in range(1, 3):
#     for i in range(int(math.pow(256, power))):
#         print(i.to_bytes(power, "big"))
print(int("256E", 16).to_bytes(2, "big"))