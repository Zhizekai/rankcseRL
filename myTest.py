from collections import namedtuple
import torch
import numpy as np

# Transition = namedtuple('Transition',('state', 'action', 'next_state', 'reward'))
# #生成一个列表，列表中是元组
# a = [(1,2,3,4),
#     (11,12,13,14),
#     (21,22,23,24),
#     (31,32,33,34)]
# b = zip(*a)

# b = list(b) # [(1, 11, 21, 31), (2, 12, 22, 32), (3, 13, 23, 33), (4, 14, 24, 34)]
# print(b)
# c = Transition(*zip(*a))
# print(c) #Transition(state=(1, 11, 21, 31), action=(2, 12, 22, 32), next_state=(3, 13, 23, 33), reward=(4, 14, 24, 34))
# c = list(c)

# 保存中间变量的函数
# a = {'state_batch':batch.state, 'next_state_batch':batch.next_state}
# torch.save(a, "./myDict.pth")

# 这玩意第一层是个元组 ，第二层是list ，最里面才是包着的tensor
# state_batch,next_state_batch = torch.load("./myDict.pth").values()

# next_state_batch = [ torch.cat((i[0],i[1]),0) for i  in zip(*next_state_batch)]
# print(next_state_batch)

# tensor1 = torch.randn(1, 10)  # 形状: [2, 3, 4]
# tensor2 = torch.randn(1, 10)  # 形状: [1, 3, 1]

# # 广播 tensor2 到 [2, 3, 4]
# tensor2_broadcasted = tensor2.expand(tensor1.shape)
# print(tensor2_broadcasted)

# # 现在两个张量的形状都是 [2, 3, 4]，可以进行元素级操作
# result = tensor1 + tensor2_broadcasted
# print(result)
a = torch.load("./myDict.pth")
ddpg_x3, ddpg_w3, ppo_x3, ppo_w3 = a.values()
x_ddpg = torch.matmul(ddpg_x3, ddpg_w3)
x_ppo = torch.matmul(ppo_x3, ppo_w3)
print(x_ddpg)
print(x_ppo)
