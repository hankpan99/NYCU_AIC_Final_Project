import pickle
import matplotlib.pyplot as plt

folder_name = "noT_2022-06-07-23-59-36"
num_iteration = 5000

with open(f"../../../../data/rsg_anymal/{folder_name}/avg_reward_{num_iteration}", "rb") as fp:   # Unpickling
    avg_reward = pickle.load(fp)

plt.figure(figsize=(15, 10), linewidth = 5)
plt.plot(range(num_iteration), avg_reward)
plt.title('Avg Reward per Iteration (Original Form)', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Iteration', fontsize=20)
plt.ylabel('Avg Reward', fontsize=20)
plt.savefig(f'./{folder_name}/noT.png')
# plt.show()