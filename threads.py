import threading

threads = []

def start_thread(function, amount):
    
    for i in range(amount):

        thread = threading.Thread(target=function)

        thread.start()

        threads.append(thread)

    end_threads(threads)

    #threading.Lock()

def end_threads(threads):
    for t in threads:
        t.join()