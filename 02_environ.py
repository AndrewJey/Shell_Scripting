#!/usr/bin/env python3
import os

home_dir = os.environ.get('HOME') or os.environ.get('USERPROFILE') or ''
print(home_dir)

# Value for the current process session only
os.environ['APP_TOKEN'] = '1234567890'
print(os.environ.get('APP_TOKEN'))

# Use .get() with default for robustness
print(os.environ.get('APP_SECRET', 'Not Set'))
