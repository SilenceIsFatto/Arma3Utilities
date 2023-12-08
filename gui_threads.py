from threading import Thread
from threading import Lock

def start_threads(threads):
    for x in threads:
        x.start()

    for x in threads:
        x.join()

    # print("All Threads Finished")
    return True