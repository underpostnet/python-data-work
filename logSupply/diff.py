#!/usr/bin/env python
import sys


# https://medium.com/@jordan.baczuk/how-bitcoin-network-hashrate-is-estimated-269766a809f5

# Get command line arguments
##########################
# Note this script will calculate based on an average of 1 day's worth of blocks
# if len(sys.argv) < 2:
#     print ("Usage: $ btc_hashrate <blocks-24h> <current-difficulty>")
#     sys.exit()

# actualBlocks = float(sys.argv[1])
# currentDifficulty = float(sys.argv[2])


actualBlocks = 100
currentDifficulty = 100

# 0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff


# Math
##########################
blockTime = 10.0 # minutes
minutesPerDay = 24.0 * 60.0
expectedBlocks = minutesPerDay / 10.0 # 144 (1 days worth of blocks)
secondsPerBlock = 60.0 * 10.0  # 60 seconds * 10 minutes
hashpower = (actualBlocks / expectedBlocks) * (currentDifficulty * 2**32) / secondsPerBlock

print('hashpower ->')
print(hashpower)

# Print it nicely
if hashpower < 1000 * 1e9:
    print (hashpower/1e9, "GH/s (1e9)")
elif hashpower < 1000 * 1e12:
    print (hashpower/1e12, "TH/s (1e12)")
elif hashpower < 1000 * 1e15:
    print (hashpower/1e15, "PH/s (1e15)")
elif hashpower < 1000 * 1e18:
    print (hashpower/1e18, "EH/s (1e18)")
else:
    print (hashpower/1e21, "ZH/s (1e21)")
