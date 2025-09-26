import sys
import getopt

print(sys.argv) #系统参数输入解析

opts, args = getopt.getopt(sys.argv[1:],"f:m:",['filename','message']) #解析参数和opts
print(opts)
print(args)

for opt,arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

print(f"filename:{filename},\nmessage:{message}")