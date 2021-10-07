import time


def start_timer():
    return time.time()


def stop_timer(start_time, display=True):
    """Simple timer with optional print statement(Default is True) | returns time in seconds."""
    final_time = time.time()
    calculated_total = final_time - start_time
    total_time = time.strftime("%Hh:%Mm:%Ss", time.gmtime(calculated_total))
    if display:
        print("Total time taken: ", total_time)
    return calculated_total
