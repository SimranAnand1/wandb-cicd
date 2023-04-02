import wandb
print(f'The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.14.0', f'Expected version 2.1.01, but got {wandb.__version__}'
