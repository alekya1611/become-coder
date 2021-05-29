num=int(input())
while True:
    r=num%10
    num=num//10
    print(r,num)
    if num==0:
        break
