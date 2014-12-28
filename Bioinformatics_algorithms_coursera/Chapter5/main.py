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

   MANHATTANTOURIST(n, m, Down, Right)
        s0, 0 ← 0
        for i ← 1 to n
            si, 0 ← si-1, 0 + downi, 0
        for j ← 1 to m
            s0, j ← s0, j−1 + right0, j
        for i ← 1 to n
            for j ← 1 to m
                si, j ← max{si - 1, j + downi, j, si, j - 1 + righti, j}
        return sn, m

# m Cols, n Rows
def ManhatanTourist (n, m, down_m, right_m):
	s = [ [0 for i in range(m)] for i in range(n) ]
	for i in (1, range(n+1)):
		s[i][0] = s[i-1][0] + down_m[i][0]
	for j in (1, range(n+1)):
		s[0][j] = s[0][j-1] + right_m[0][j]
	for i in range(1, i+1):
		for j in range(1,j+1):
			s[i][j] = max(s[i-1][j]+down_m[i][j], s[i][j-1]+right_m[i][j])
	return s


# Manhatan Tourist input
line1  = raw_input().strip().split()
n = int(line1[0])
m = int(line1[1])
down = []
for i in range(n):
	line = raw_input.strip().split()
	down.append([int(i) for i in line])
raw_input() # Waiting for "-"	
right  = []
for i in range(n+1):
	line = raw_input.strip().split()
	right.append([int(i) for i in line])
ManhatanTourist(n, m, down, right)

"""
# Test input for DPChange
coins = [5, 4, 1]
change =  DPChange(76, coins)
counter = 0
for i in change:
	print "%s: %s" % (counter, i)
	counter += 1
# Input for DPChange
money = int(raw_input().strip())
coin_line = raw_input().strip()
coins = [int(x) for x in coin_line.split(",")]
change =  DPChange(money, coins)
print change[-1]
"""
