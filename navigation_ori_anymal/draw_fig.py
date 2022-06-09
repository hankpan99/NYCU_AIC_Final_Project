import pickle
import matplotlib.pyplot as plt

folder_name = "2022-06-09-16-23-58"
num_iteration = 6000

with open(f"../../../../data/rt_anymal/{folder_name}/avg_reward_{num_iteration}", "rb") as fp:   # Unpickling
    avg_reward = pickle.load(fp)

plt.figure(figsize=(15, 10), linewidth = 5)
plt.plot(range(num_iteration), avg_reward)
plt.title('Avg Reward per Iteration (Rotatoin = +-45 degrees)', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Iteration', fontsize=20)
plt.ylabel('Avg Reward', fontsize=20)
plt.savefig(f'./dst.png')
# plt.show()