import os


print('Hello word')


def shell(self, command: str, output: bool = False):
    try:
        if not output:
            os.subprocess.call([command], shell=True)
        else:
            return os.subprocess.check_output([command], shell=True).decode().strip()
    except os.subprocess.CalledProcessError as e:
        raise ValueError('Error') from e

v = shell()
print(v)
