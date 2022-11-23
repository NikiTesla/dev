import time

with open("lyrics.txt") as f:
	lines = f.readlines()

for line in lines:
	time.sleep(1.8)
	print(line)
