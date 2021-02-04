import json
import time
import multiprocessing
import requests


def multiprocessing_func(x):

    serverIp = "http://SERVER_IP:"
    serverPort = "SERVER_PORT"
    endPoint = "/END_POINT_API/"
    passed = 0
    failed = 0
    avg_time = 0
    numberOfRequestPerSecond = 1000

    try:
        for i in range(0,numberOfRequestPerSecond):
            startTime = time.time()
            requests.post(
                serverIp + serverPort + endPoint,
                data=json.dumps({
                }), headers={
                    "Content-Type": "application/json",
                }).json()

            passed = passed + 1
            endTime = time.time()

            avg_time = avg_time + (endTime - startTime)

    except Exception as e:
        print("ERROR IN Func() method")
        print(e)
        failed = failed + 1


    print("TOTAL PASSED IN PROCESS (", x , ")" ,passed)
    print("TOTAL FAILED IN PROCESS (", x, ")", failed)
    print("AVERAGE TIME: ", (avg_time/numberOfRequestPerSecond*1000), " MS")



if __name__ == '__main__':
    startTime = time.time()
    processes = []
    numberOfClients = 100

    for i in range(0, numberOfClients):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    print('Process class took {} seconds'.format(time.time() - startTime))

