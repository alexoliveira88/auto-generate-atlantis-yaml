
"""
Author: Alex Oliveira
 
This script fetches all folders with excess to the workspace folder and generates the atlantis.yaml file.
"""

import os

def creating_atlantis_yaml():
    with open('atlantis.yaml', 'w') as atlantis_yaml:
        atlantis_yaml.write('version: 3\n'
                            'automerge: true\n'
                            'projects:\n'
                            )
    get_dir()

def get_dir():
    for root, dirs, files in os.walk("teste", topdown=True): 
        for name in dirs:
            with open('atlantis.yaml', 'a') as atlantis:
                if name != 'workspaces':
                    dir = os.path.join(root, name)
                    if os.path.exists(os.path.join(dir, 'workspaces')) and os.path.exists(os.path.join(dir, 'custom-atlantis.yaml')):
                        with open(os.path.join(dir, 'custom-atlantis.yaml')) as custom_atlantis:
                            atlantis.write(custom_atlantis.read())
                            atlantis.write('\n')
                    elif os.path.exists(os.path.join(dir, 'workspaces')):
                        workspace = os.path.join(dir, 'workspaces')
                        for file in os.listdir(workspace):
                             atlantis_template(dir, file)

def atlantis_template(dir, file):
    with open('atlantis.yaml', 'a') as atlantis:
        atlantis.write(f'- name: {dir}-{file.split(".tfvars")[0]}\n'
                       f'  dir: {dir}\n'
                       f'  workspace: {file.split(".tfvars")[0]}\n'
                       f'  autoplan:\n'
                       f'    when_modified: ["*.tf", "workspaces/{file}"]\n'
                       f'    enabled: true\n')

        
if __name__ == "__main__":
    try:
        creating_atlantis_yaml()
    except:
        print('Erro to generate atlantis.yaml.')






