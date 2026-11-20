#!/usr/bin/env python3
from collections import Counter
import re
import sys

USER_PATTERN = re.compile(r'\buser=([^\s;]+)|\bfor\s+(?:invalid\s+user\s+)?([^\s;]+)', re.IGNORECASE)


def count_auth_failures(lines):
    """Count authentication failure occurrences per user from log lines."""
    counts = Counter()
    for raw in lines:
        line = raw.strip()
        if 'authentication failure' not in line.lower():
            continue
        match = USER_PATTERN.search(line)
        user = (match.group(1) or match.group(2)) if match else 'unknown'
        counts[user] += 1
    return dict(counts)


def main():
    counts = count_auth_failures(sys.stdin)
    for user, total in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f'{user}: {total}')


if __name__ == '__main__':
    main()
