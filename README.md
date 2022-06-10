# NYCU_AIC_Final_Project

## Introduction
We use Raisim to train ANYmal to achieve two tasks, "walk stably" and "navigation".

## Installation
Please first check out the [installation guide](https://raisim.com/sections/Installation.html) on RaiSim website to install Raisim.

### Environment 
Clone this repo and place these three folders in ```PATH_TO_raisimLib/raisimGymTorch/raisimGymTorch/env/envs```.

### Trained Model
```
cd PATH_TO_raisimLib/raisimGymTorch
mkdir data
cd data
```

The trained model can be found in this [link](https://drive.google.com/drive/folders/19x172cEwG4Exwcyls97_pFTc6T0a8CHw?usp=sharing), please download the folder and place it in the directory `data`.

## Usage
In the following please run commands in the directory ```PATH_TO_raisimLib/raisimGymTorch```.

### Run
1. Compile raisimgym: ```python setup.py develop```
2. Run runner.py of the task (for rsg_anymal example): ```python raisimGymTorch/env/envs/rsg_anymal/runner.py```

### Test policy
1. Compile raisimgym: ```python setup.py develop```
2. Run tester.py of the task with policy (for rsg_anymal example): ```python raisimGymTorch/env/envs/rsg_anymal/tester.py --weight data/rsg_anymal/FOLDER_NAME/full_XXX.pt```

### Retrain policy
1. Compile raisimgym: ```python setup.py develop```
2. Run runner.py of the task with policy (for rsg_anymal example): ```python raisimGymTorch/env/envs/rsg_anymal/runner.py --mode retrain --weight data/rsg_anymal/FOLDER_NAME/full_XXX.pt```

Please check out this [link](https://raisim.com/sections/RaisimGymTorch.html) for more details about RaisimGymTorch.

