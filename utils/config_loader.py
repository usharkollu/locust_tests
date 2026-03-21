import json
import os

def load_config(env_name):
    # Local path: envs/prod.env
    # Azure path: prod.env (flat structure)
    local_path = f'envs/{env_name}.env'
    azure_path = f'{env_name}.env' # Azure engines flatten the folder structure

    # Check which path exists
    if os.path.exists(azure_path):
        target_path = azure_path
    elif os.path.exists(local_path):
        target_path = local_path
    else:
        raise FileNotFoundError(f"Config file not found: {env_name}.env")

    with open(target_path, 'r') as file:
        config = json.load(file)
        print(f"Loaded configuration for environment: {env_name}")
    return config