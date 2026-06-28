import sys;
import getopt;

# print(sys.argv[0]);
# print(sys.argv[1]);
filename = None;
message = None;

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message']);

for opt, arg in opts: 
    if(opt == '-f'): 
        filename = arg;
    if(opt == '-m'):
        message = arg;

with open(filename, 'a+') as f:
    f.write(f"{message}\n");
