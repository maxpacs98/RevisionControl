import subprocess
import sys


def shell(command: str, output: bool = False):
    try:
        if not output:
            subprocess.call([command], shell=True)
        else:
            return subprocess.check_output([command], shell=True).decode().strip()
    except subprocess.CalledProcessError as e:
        raise ValueError('Error') from e


# v = shell('git describe --tags --long --dirty --always')
try:
    v = sys.argv[1]
except IndexError:
    v = shell('git describe --tags --long --dirty --always')
print(v)
