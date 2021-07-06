from math import *

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import show

# 10^2 = 100 -> 2 -> base 10
# print(log(100,10))

# logaritmo natural
# print(log(10))

# euler
# print(e)

era = []
reward = []
blocks = []
rewardPerBlock = []
intervalChangeEraBlock = 210000
totalEra = 32

sumBlocks = 0
for i in range(0, totalEra):
    era.append(i)
    y = (intervalChangeEraBlock*((50*(10**8))/(2**i)))/(10**8)
    reward.append(y)
    rewardPerBlock.append(y/intervalChangeEraBlock)
    sumBlocks = sumBlocks + intervalChangeEraBlock
    blocks.append(sumBlocks)

sumReward = 0
for i in reward:
    sumReward = sumReward + i

print('reward ->')
print(reward)
print('blocks ->')
print(blocks)
print('rewardPerBlock ->')
print(rewardPerBlock)
print('sum Reward ->')
print(sumReward)
print('sum Blocks ->')
print(sumBlocks)

plt.plot(era, reward, color='green', label='reward era')
plt.ticklabel_format(style = 'plain')
plt.xlabel("time era")
plt.legend()

show()

plt.plot(era, rewardPerBlock, color='red', label='reward block era')
plt.ticklabel_format(style = 'plain')
plt.xlabel("time era")
plt.legend()

show()

plt.plot(era, blocks, color='blue', label='blocks mined')
plt.ticklabel_format(style = 'plain')
plt.xlabel("time era")
plt.legend()

show()









# end
