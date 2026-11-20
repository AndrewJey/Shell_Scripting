import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent


class ShellScriptingTest(unittest.TestCase):
    def run_script(self, name, stdin_text=''):
        return subprocess.run(
            [sys.executable, str(ROOT / name)],
            input=stdin_text,
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True,
            timeout=15,
        )

    def test_hello_and_environ_and_read_file(self):
        r1 = self.run_script('01_hello_world.py')
        self.assertEqual(r1.stdout.strip(), 'hello, world!')

        r2 = self.run_script('02_environ.py')
        lines = r2.stdout.splitlines()
        self.assertEqual(lines[1], '1234567890')
        self.assertEqual(lines[2], 'Not Set')

        r3 = self.run_script('03_read_file.py')
        self.assertIn('Monday', r3.stdout)

    def test_read_stdin_and_count_auth_failures(self):
        r4 = self.run_script('04_read_stdin.py', 'uno\ndos\n')
        self.assertIn('uno', r4.stdout)

        logs = (
            'Nov 19 sshd: authentication failure; logname= uid=0 user=root\n'
            'Nov 19 sshd: accepted password for alice\n'
            'Nov 19 sshd: authentication failure; logname= uid=0 user=root\n'
            'Nov 19 sshd: authentication failure; rhost=1.2.3.4 user=bob\n'
        )
        r5 = self.run_script('05_cout_users.py', logs)
        self.assertEqual(r5.stdout.splitlines(), ['root: 2', 'bob: 1'])


if __name__ == '__main__':
    unittest.main()
