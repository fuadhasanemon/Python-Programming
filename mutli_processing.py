import time
import multiprocessing


def multiprocessing_func(x):
    outputFile = open("data" + str(x) + ".txt", "w")
    for i in range(0, 10000000):
        outputFile.write(str(i) + '\n')
    outputFile.close()


if __name__ == '__main__':

    startTime = time.time()
    processes = []
    for i in range(0, 5):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    print('Process class took {} seconds'.format(time.time() - startTime))

    startTime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(20, 25))
    pool.close()
    print('Pool class took {} seconds'.format(time.time() - startTime))

    startTime = time.time()
    for i in range(40, 45):
        multiprocessing_func(i)
    print('Normal System took {} seconds'.format(time.time() - startTime))
