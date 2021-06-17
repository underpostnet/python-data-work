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


reward = []
era = []
blocks = []
rewardPerBlock = []

sumBlocks = 0;

intervalChangeEraBlock = 210000
totalEra = 32

for i in range(0, totalEra):

    era.append(i)

    y = (intervalChangeEraBlock*((50*(10**8))/(2**i)))/(10**8)
    reward.append(y)
    rewardPerBlock.append(y/intervalChangeEraBlock)

    sumBlocks = sumBlocks + intervalChangeEraBlock
    blocks.append(sumBlocks)


# https://en.bitcoin.it/wiki/Controlled_supply

# print('reward ->')
# print(reward)
# print('era ->')
# print(era)

reward_sum = 0
for i in reward:
    reward_sum = reward_sum + i

print('total sum y test ->')
print(reward_sum)


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
