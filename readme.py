# Collect readme files in workshop
# Generate readme of the project

import os

# The working dir
WD = os.path.dirname(__file__)

# The content of the readme file
CONTENTS = []
CONTENTS.append(open(os.path.join(WD, 'README_head.md')).read())

# The folder of work shop
workshop_folder = os.path.join(WD, 'workShop')

# For each work in work shop
for folder in os.listdir(workshop_folder):
    # Ignore the folders do not contain 'README.md'
    if 'README.md' not in os.listdir(os.path.join(workshop_folder, folder)):
        continue

    # Prompt the folder name
    print(folder)

    CONTENTS.append(
        open(os.path.join(workshop_folder, folder, 'README.md')).read())


content = '\n'.join(CONTENTS)
print(content)

with open(os.path.join(WD, 'README.md'), 'w') as f:
    f.write(content)

print('All Done.')
