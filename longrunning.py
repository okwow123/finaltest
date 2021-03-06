import logging
import socket
import sys

lock_socket = None

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_id = "my-username.my-task-name"   # this should be unique. using your username as a prefix is a convention
        lock_socket.bind('\0' + lock_id)
        logging.debug("Acquired lock %r" % (lock_id,))
        return True
    except socket.error:
        logging.info("Failed to acquire lock %r" % (lock_id,))
        return False
 
if not is_lock_free():
    sys.exit()
from my_module import my_long_running_process
my_long_running_process()
