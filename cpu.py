import numpy as np

num1 = np.array(range(100), dtype=np.int32)
num2 = np.array(range(100), dtype=np.int32)
out = np.empty(num1.shape, dtype=np.int32)
count = 0

#while count < 100:
for i in num1:
	out[i] = (num1[i]*num1[i]+ num2[i]*num2[i])
#	count+=1

print "Number1:", num1
print "Number2:", num2
print "Output :", out