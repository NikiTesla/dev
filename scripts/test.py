num = input()
num = [ num[::-1][i*3:i*3+3]+"," for i in range(len(num)//3+1)]
if num[-1] == ",": num = num[:-1]
print("".join(num)[-2::-1])
