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


# Join CONTENTS to generate content
content = '\n'.join(CONTENTS)

# Generate Table of Contents
split = [e.strip() for e in content.split('\n') if e.strip()]
toc = []
repeat = []
ignore = False

for seg in split:
    if seg.startswith('```'):
        ignore = not ignore

    if ignore:
        continue

    if not seg.startswith('#'):
        continue

    count = -1
    while seg.startswith('#'):
        count += 1
        seg = seg[1:]
    seg = seg.strip()

    c = '  ' * count + '- '
    a = seg
    b = seg.replace(' ', '-').lower()
    bb = b

    if b in repeat:
        j = 0
        while bb in repeat:
            j += 1
            bb = f'{b}-{j}'

    repeat.append(bb)

    toc.append(f'{c}[{a}](#{bb})')

toc.append('')
toc.append('')

# Write content
with open(os.path.join(WD, 'README.md'), 'w') as f:
    f.write('\n'.join(toc))
    f.write(content)

print('All Done.')
