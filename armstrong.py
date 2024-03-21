def is_armstrong(number,original,power):
    if number==0:
        return original==0
    else:
        digit=number%10
        return(digit**power)+is_armstrong(number//10,original,power)
def main():
    num=int(input())
    power=len(str(num))
    if is_armstrong(num,num,power)==num:
        print("armstrong number")
    else:
        print("not armstrong number")
if __name__ =="__main__":
    main()
