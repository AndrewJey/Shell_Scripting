#!/usr/bin/env python3
from pathlib import Path

days_file = Path(__file__).resolve().parent / 'days.txt'
with days_file.open(encoding='utf-8') as file:
    for line in file:
        print(line.strip())
