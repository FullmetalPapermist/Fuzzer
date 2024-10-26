import math
import sys
import subprocess
# for i in range(1, 256):
#     print(int("ff" * i, 16))

# for power in range(1, 3):
#     for i in range(int(math.pow(256, power))):
#         print(i.to_bytes(power, "big"))

file = sys.argv[1]
res = subprocess.run(f"clang {file} -fstack-protector-all -o out", shell=True, capture_output=True, text=True)
if res.stderr:
    print(f"Compiler warnings!!\n{res.stderr}")
print("Format string payload incoming")
for payloadSize in range(1, 10):

    sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    userIn = "256E" * payloadSize
    sp.stdin.write(int(userIn, 16).to_bytes(payloadSize * 2, "big"))
    sp.stdin.flush()
    print(int(userIn, 16).to_bytes(payloadSize * 2, "big"))
    out, err = sp.communicate()
    if sp.poll() != 0:
        code = sp.poll()
        hexit = sp.poll().to_bytes(1, "big", signed=True)
        print(f"Program crashed with: \n%n * {payloadSize}\nExit code: {hexit} {code}")
        if out:
            print(f"Out: {out}")
        else:
            print("No out")
        if err:
            print(f"Error: {err}")
        else:
            print("No err")

# print(int("256E", 16).to_bytes(2, "big"))