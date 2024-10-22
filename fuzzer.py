import subprocess
import sys
import os
import tempfile
import math

MAX = 8

if __name__ == '__main__':
    file = sys.argv[1]
    arg = "hello"
    tmp = tempfile.mktemp()
    res = subprocess.run(f"clang {file} -o out", shell=True, capture_output=True, text=True)
    if res.stderr:
        print(f"Compiler warnings!!\n{res.stderr}")
    print("Fuzzing now (Please wait)!")
    payloadSize = 1
    while True:
        sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
        input = "ff" * payloadSize
        sp.stdin.write(int(input, 16).to_bytes(payloadSize, "big"))
        sp.stdin.flush()
        out, err = sp.communicate()
        if sp.poll() != 0:
            code = sp.poll()
            hexit = sp.poll().to_bytes(1, "big", signed=True)
            print(f"Program crashed with: \nff *{payloadSize}\nExit code: {hexit} {code}")
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

    print("Brute force incoming!")

    byteNum = 1
    while True:
        for i in range(int(math.pow(256, byteNum))):
            sp = subprocess.Popen(['./out'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
            sp.stdin.write(i.to_bytes(byteNum, "big"))
            sp.stdin.flush()
            out, err = sp.communicate()
            if sp.poll() != 0:
                print(f"Program crashed with: \n{hex(input)}")
                if out:
                    print(f"Out: {out}")
                if err:
                    print(f"Error: {err}")
                break
        byteNum += 1

    os.remove("out")

