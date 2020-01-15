import os, shutil, random
import atexit
import signal
import sys
from glob import glob


is_cleaned = False
original_sigint_handler = signal.getsignal(signal.SIGINT)
def do_cleaning(*args, **kwargs):
    global is_cleaned, original_sigint_handler
    if is_cleaned:
        return

    new_dir = './app/static'
    for d in glob(os.path.join(new_dir, "[0-9]*")):
        os.remove(os.path.join(d, 'suspicious_file.txt'))
        os.rmdir(d)
    is_cleaned = True
    # signal.signal(signal.SIGINT, original_sigint_handler)
    # os.kill(os.getpid(), signal.SIGINT)

atexit.register(do_cleaning)
# signal.signal(signal.SIGINT, do_cleaning)


def randomFlag():
    folder = random.randint(1, 155)
    new_dir = './app/static/{}'.format(folder)
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
        shutil.copyfile('/tmp/suspicious_file.txt', os.path.join(new_dir, 'suspicious_file.txt'))
