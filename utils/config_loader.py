import json

def load_config(env_name):
    with open('envs/' + env_name + '.env', 'r') as file:
        config = json.load(file)
        print(f"Loaded configuration for environment: {env_name}")
    return config