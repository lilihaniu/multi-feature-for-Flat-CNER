import argparse

parser=argparse.ArgumentParser()
parser.add_argument('parm1',type=str,help='输入姓名',default='True')
parser.add_argument('parm2',type=str,help='输入姓名',default='True')
arg=parser.parse_args()
print(arg.parm1+arg.parm2)


