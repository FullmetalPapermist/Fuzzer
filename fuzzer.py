import subprocess
import sys
import os
import tempfile
import math

def formatPayload():
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
            break
        payloadSize += 1


def fastPayload():
    print("Fast payload incoming!")
    payloadSize = 1
    while True:
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
            break
        payloadSize += 1

def bruteForce():
    print("Brute force incoming!")
    byteNum = 1
    error = False
    while not error:
        for i in range(int(math.pow(256, byteNum))):
            sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
            sp.stdin.write(i.to_bytes(byteNum, "big"))
            sp.stdin.flush()
            out, err = sp.communicate()
            if sp.poll() != 0:
                print(f"Program crashed with: \n{hex(input)}\nPayload size: {byteNum} bytes")
                if out:
                    print(f"Out: {out}")
                if err:
                    print(f"Error: {err}")
                error = True
                break
        byteNum += 1

def test(bytes, byteNum):
    sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
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
    tmp = tempfile.mktemp()
    res = subprocess.run(f"clang {file} -o out", shell=True, capture_output=True, text=True)
    if res.stderr:
        print(f"Compiler warnings!!\n{res.stderr}")
    ans = input("Fast (f), Slow (s) Format Strings (%n) or Expert (x)?\n")
    if ans == "f":
        print("Fuzzing now (Please wait)!")
        fastPayload()
    elif ans == "s":
        print("Fuzzing now (Please wait)!")
        bruteForce()
    elif ans == "x":
        userIn = input("Enter input:\n")
        buffer = input("Enter size:\n")
        hex = int(userIn, 16).to_bytes(buffer, "big")
    elif ans == "n":
        print("Fuzzing now (Please wait)!")
        formatPayload()


    os.remove("out")
    print("Done!")
