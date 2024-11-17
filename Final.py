import pexpect
import subprocess
import re

def main(user_input):
    compile_command = ["gcc", "Allen.c", "-o", "./a.out"]
    subprocess.run(compile_command, check=True)

    command = './a.out'
    proc = pexpect.spawn(command)

    proc.sendline(user_input)

    output = proc.read()

    out = output.decode().splitlines()
    print("Output:", out[1])

    if out[1] == outputs:
        print("Success.")
    else:
        print("Fail.")
        print("Required Ouput:", outputs)


def extract(filename):    
    with open(filename, 'r') as f:
        text = f.read()

        pattern = r'(input\n(?!\n)(.*?)(?=output|$))|(output\n(?!\n)(.*?)(?=input|$))'

        matches = re.findall(pattern, text, re.DOTALL)
        groups = []

        for match in matches:
            if match[0]:
                inputs = " ".join([line for line in match[1].splitlines() if line])
                groups.append([inputs, []])
            else:
                outputs = " ".join([line for line in match[3].splitlines() if line])
                groups[-1][1] = outputs
              
        return groups

if __name__ == "__main__":
    groups = extract("testcase.txt")
    for i, (inputs, outputs) in enumerate(groups):
        main(inputs)
