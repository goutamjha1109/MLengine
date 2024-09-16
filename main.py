import yaml


with open('conf/conf.yml') as file:
    conf = yaml.safe_load(file)

print("pass")