import sys
# import resource
import os
import psutil

def read_file(filepath: str):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                yield line
    except:
        raise IOError("File not found")

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Enter path to the file")
        exit(1)

    generator = read_file(sys.argv[1])
    for line in generator:
        pass

    p = psutil.Process()
    memory = p.memory_info().peak_wset / (1024 ** 3)
    print("Peak Memory Usage = %.3f GB" % memory)
    time = psutil.cpu_times().user + psutil.cpu_times().system
    print("User Mode Time + System Mode Time = %.2fs" % time)

    # memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    # print(f"Peak Memory Usage = {memory}")
    # user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    # system_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime
    # print(f"User Mode Time + System Mode Time = {user_time + system_time}s")