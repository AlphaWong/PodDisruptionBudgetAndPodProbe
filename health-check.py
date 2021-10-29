import time, urllib.request, random, sys, logging
from threading import Event

# configure logging
logs_format = '[%(asctime)s] %(levelname)s - %(message)s'
logger = logging.getLogger()
# this is needed in order to see the logs through K8s logs
# '/proc/1/fd/1' file is functioning as the Pod's STDOUT.
handler = logging.FileHandler('/proc/1/fd/1', mode='w')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(logs_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

# sleep_window = random.randrange(10, 60)
# logger.info("sleep_window: %s", sleep_window)
# time.sleep(sleep_window)
# Event().wait(sleep_window)

urllib.request.urlopen('http://slow-server.default.svc.cluster.local/ping',
                       timeout=10)
resp = urllib.request.urlopen('http://nginx2.default.svc.cluster.local',
                              timeout=10)
status_code = resp.getcode()
logger.info("status_code: %s", status_code)
if status_code != 200:
    sys.exit(1)
