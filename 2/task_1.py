from time import sleep

n = int(input())
max_value = n

bin_n = bin(n)[2::]

for i in range(len(bin_n)):
	bin_n = bin_n[1::] + bin_n[0]
	dec_current = int(bin_n, 2)
	if dec_current > max_value:
		max_value = dec_current

print(max_value)
