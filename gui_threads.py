from threading import Thread

def start_threads(threads):
    for x in threads:
        x.start()

    for x in threads:
        x.join()