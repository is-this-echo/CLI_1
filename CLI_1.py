
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Process two floating point numbers')
    
    parser.add_argument('--x', type=float, default=1.0,
                       help='The first number')
    parser.add_argument('--y', type=float, default=1.0,
                       help='The second number')
    parser.add_argument('--operation', type=str, default='mult',
                       help='What operation? Can choose add, minus, mult, div')
    
    args = parser.parse_args()
    
    #calling func
    sys.stdout.write(str(calc(args)))



def calc(args):
    
    
#     operation = args.operation
#     x = x.args
#     y  = y.args
    
    if args.operation =='add':
        return args.x+args.y
    
    elif args.operation =='minus':
        return args.x-args.y
    
    elif args.operation =='mult':
        return args.x*args.y
    
    elif args.operation =='div':
        return args.x/args.y
    
    
if __name__ == '__main__':
    main()


# result = calc(8,3,'mult')
# print(result)