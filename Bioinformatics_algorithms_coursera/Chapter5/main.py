def GreedyChange(money):
	coins  = [100, 50, 25, 5, 1]
	change = []

	while money > 0:
		coins =  filter(lambda c: c <= money, coins)
		money -= coins[0]
		print money
		change.append(coins[0])
	return change

#print GreedyChange(78)

def RecursiveChange(money, coins):
	print "Received value: %s" % str(money)
	if money == 0:
		return 0
	MinNumCoins = 99999999999
	for i in range(0, len(coins)):
		print "Money value %s, coin value %s, i %s" % (str(money), str(coins[i]), str(i))
		if money>=coins[i]:
			print "Added coin!, now money is %s" % (money-coins[i])
			NumCoins = RecursiveChange(money-coins[i], coins)
			if NumCoins+1 < MinNumCoins:
				MinNumCoins = NumCoins + 1
			print MinNumCoins
	return MinNumCoins
	

def DPChange(money, coins):
	# Using  a dictionary would make this memory-efficience
	MinNumCoins = [0 for i in range(0, money+1)]
	MinNumCoins[0] = 0
	for m in range(1,money+1):
		MinNumCoins[m] = 99999999999999
		for i in range(0,len(coins)):
			coin = coins[i]
			if m>= coin:
				if MinNumCoins[m-coin]+1 < MinNumCoins[m]:
					MinNumCoins[m] = MinNumCoins[m-coin] +1
	return MinNumCoins

money = int(raw_input().strip())
coin_line = raw_input().strip()
coins = [int(x) for x in coin_line.split(",")]
change =  DPChange(money, coins)
print change[-1]
"""
# Test input for DPChange
coins = [5, 4, 1]
change =  DPChange(76, coins)
counter = 0
for i in change:
	print "%s: %s" % (counter, i)
	counter += 1
"""
