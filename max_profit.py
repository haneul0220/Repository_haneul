import sys

def max_(prices):
	max_p = -sys.maximum
 	for i, price in enumerate(prices):
		for j in range(i, len(prices)):
			max_p = max(prices[i] - price, max_p)

	return max_p

