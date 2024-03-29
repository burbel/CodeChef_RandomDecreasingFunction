#! /usr/bin/env python
# Created by Brian Bibeault on 3/18/13.
# Direct port of my C version program

def main():    # Don't leave the code in the global namespace, it runs slower
    sumBelowCache = [[0.0 for x in range(0, 32)] for x in range(0, 100001)]
    for b in range (0, 32):
        sumBelowCache[0][b] = 0.0;
    for a in range (1, 100001):
        sumBelowCache[a][0] = sumBelowCache[a-1][0] + a
        sumBelowCache[a][1] = sumBelowCache[a-1][1] + 0.5*a - 0.5
    for b in range (2, 32):
        for a in range (2, 100000):
            sumBelowCache[a][b] = sumBelowCache[a-1][b] + sumBelowCache[a-1][b-1]/a

    tokenizedInput = map(int, sys.stdin.read().split())    # Read at once, tokenize
    testcases = tokenizedInput[0]
    readAt = 1    # Position to begin reading
    for count in range(0,testcases):
        n,k = tokenizedInput[readAt:readAt+2]    # Read the tokenized input
	if k >= 32:
	    print("0.0")
	elif k == 0:
	    print(n)
	else:
	    output = sumBelowCache[n-1][k-1]/float(n)
	    if output < 0.000001:
		print("0.0")
	    else:
 	        print(output)
        readAt = readAt + 2

import sys
main()
