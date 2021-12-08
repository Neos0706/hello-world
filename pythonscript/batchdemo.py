import sys
import os
import argparse
import time
"""
    能够批量执行脚本
"""


def files_parameters(script, files):
    for i in files:
        cmd(script, i)


def dir_parameters(script, dir):
    files = os.listdir(dir)
    print(files)
    for i in files:
        if i != ".DS_Store":
            i = os.path.join(dir, i)
            cmd(script, i)


# 拼接全脚本
def whole_script(script):
    res = ''
    for i in script:
        res = res + " " + i
    res.lstrip(' ')
    return res


def cmd(script, parameters):
    cmd = str(script) + " " + str(parameters)
    os.system(cmd)

def parser_args():
    parser = argparse.ArgumentParser(description=" Batch execution script")
    parser.add_argument('--script', '-s', type=str, dest="script", required=True, nargs="*", help="destination script")
    parser.add_argument('--dir', '-d', type=str, dest="dir", help="destination dir")
    parser.add_argument('--files', '-f', type=str, dest="files", nargs="*", help="destination files")
    args = parser.parse_args()
    # print(args)
    return args


if __name__ == '__main__':
    argc = len(sys.argv)
    args = parser_args()
    script = args.script
    script = whole_script(script)
    print(script)
    print(args)
    if args.dir:
        dir = args.dir
        dir_parameters(script, dir)
    else:
        files = args.files
        files_parameters(script, files)


    # script = sys.argv[1]
    # parameters = sys.argv[2:]
    # print(parameters)
    # for i in range(argc-2):
    #     main(script, parameters[i])

