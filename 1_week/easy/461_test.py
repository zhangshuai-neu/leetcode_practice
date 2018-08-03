x = 2
y = 4

count = 0
test_mask = 1
for i in range(31):
	if x&test_mask != y&test_mask:
		count = count + 1
	test_mask = test_mask << 1

print(count)
