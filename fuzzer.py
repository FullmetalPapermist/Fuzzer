import subprocess
import sys
import os
import math

def formatPayload(byteLimit):
    print("Format string payload incoming")
    payloadSize = 1
    while True:
        sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        userIn = "256E" * payloadSize
        sp.stdin.write(int(userIn, 16).to_bytes(payloadSize * 2, "big"))
        sp.stdin.flush()
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
        payloadSize += 1


def fastPayload(byteLimit):
    print("Fast payload incoming!")
    payloadSize = 1
    while payloadSize <= byteLimit:
        sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        input = "ff" * payloadSize
        sp.stdin.write(int(input, 16).to_bytes(payloadSize, "big"))
        sp.stdin.flush()
        out, err = sp.communicate()
        if sp.poll() != 0:
            code = sp.poll()
            hexit = sp.poll().to_bytes(1, "big", signed=True)
            print(f"Program crashed with: \nff * {payloadSize}\nExit code: {hexit} {code}")
            if out:
                print(f"Out: {out}")
            else:
                print("No out")
            if err:
                print(f"Error: {err}")
            else:
                print("No err")
        payloadSize += 1

def bruteForce(byteLimit):
    print("Brute force incoming!")
    payloadSize = 1
    while payloadSize <= byteLimit:
        for i in range(int(math.pow(256, payloadSize))):
            sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            payload = i.to_bytes(payloadSize, "big")
            sp.stdin.write(payload)
            sp.stdin.flush()
            out, err = sp.communicate()
            if sp.poll() != 0:
                byte = i.to_bytes(payloadSize, "big")
                print(f"Program crashed with: \nBytes: {hex(i)}\nString: {payload} \nPayload size: {payloadSize} bytes")
                if out:
                    print(f"Out: {out}")
                if err:
                    print(f"Error: {err}")
        payloadSize += 1

def test(bytes, byteNum):
    sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    sp.stdin.write(bytes)
    sp.stdin.flush()
    out, err = sp.communicate()
    if sp.poll() != 0:
        print(f"Program crashed with: \n{hex(bytes)}\nPayload byteNum: {byteNum} bytes")
        if out:
            print(f"Out: {out}")
        if err:
            print(f"Error: {err}")

if __name__ == '__main__':
    file = sys.argv[1]
    res = subprocess.run(f"clang {file} -fstack-protector-all -o out", shell=True, capture_output=True, text=True)
    if res.stderr:
        print(f"Compiler warnings!!\n{res.stderr}")
    byteLimit = int(input("Insert byte limit:\n"))
    ans = input("Fast (f), Slow (s) Format Strings (n) or Expert (x)?\n")
    if ans == "f":
        print("Fuzzing now (Please wait)!")
        fastPayload(byteLimit)
    elif ans == "s":
        print("Fuzzing now (Please wait)!")
        bruteForce(byteLimit)
    elif ans == "x":
        bytes = input("Enter input:\n")
        byteSize = input("Enter size:\n")
        test(bytes, byteSize)
    elif ans == "n":
        print("Fuzzing now (Please wait)!")
        formatPayload(byteLimit)


    os.remove("out")
    print("Done!")
