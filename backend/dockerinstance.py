import os
import yaml


# prefix all environment variables like so:
# after prefix a valid cookiecutter-zope-instance key is needed
PREFIX = "INSTANCE_"

# load base instance.yaml
with open("instance.yaml", "r") as fio:
    instance = yaml.safe_load(fio)
cfg = instance["default_context"]

# set values from enviroment
for envkey, value in os.environ.items():
    if not envkey.startswith(PREFIX):
        continue
    key = envkey[len(PREFIX) :].lower()
    print(f"Set from env {envkey}: {key}={value}")
    cfg[key] = value


# write file
with open("dockerinstance.yaml", "w") as fio:
    yaml.dump(instance, fio)
