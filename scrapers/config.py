import yaml

with open('./config.yaml') as file:
        CONFIG = yaml.load(file, Loader=yaml.FullLoader)

