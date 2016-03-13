import random

t, f, w = 0, 0, 0
while w < 50000:
    x = random.randint(0, 10000)
    if x < 5000 :
        t = t + 1
	print ('<')
    elif x > 5000 :
	f = f + 1
	print ('>')
    w = w + 1
print ('Finished: < ', t, ' > ', f)
