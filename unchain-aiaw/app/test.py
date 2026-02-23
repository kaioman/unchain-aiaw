import os

print(os.environ.get('PROJECT_ROOT', 'root not found'))
print(os.environ.get('CONFIG_FILE_NAME', 'config not found'))
