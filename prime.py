


class Prime(object):
	x = 1
	primeList = [1]

	def isPrime(self, n):
		for num in self.primeList:
			if(n % num == 0):
				return True
		return False

	def genPrime(self):
		while (True):
			if (self.isPrime(self.x + 1)):
				self.primeList.append(self.x + 1)
				self.x += 1
				yield self.x
			else:
				self.x += 1
			

p = Prime();
c = p.genPrime()
print c.next()
print c.next()
print c.next()

print c.next()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()






#start with 1
#if next number (x + 1) can be divided by any prime number in the list, it isn't prime => continue
#if it can't be divided by any number in the prime number list, it is prime
	#add it to the primeList

#if x + 1 is prime: 
	#add to primeList
	#return x + 1
#increment x