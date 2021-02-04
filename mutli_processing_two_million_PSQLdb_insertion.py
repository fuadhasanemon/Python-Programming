
# 20 Multi Processing Units.
# SSD Storage
# 8 GB RAM
# AMD FX-6300 Processor
# Took 292.8992097377777 seconds to insert 20 Million rows

import time
import multiprocessing
import random
from random import randint

import psycopg2
import uuid

NAMES = ["AAA", "BBB", "CCC", "DDD",
         "EEE", "FFF", "GGG", "HHH",
         "III", "JJJ", "KKK", "LLL"]

ROLES = ["SUPER_ADMIN", "ADMIN", "NORMAL_USER", "GUEST"]


def connect_to_database():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydatabase")

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ALL_USER( "
                       "USER_ID VARCHAR(450) PRIMARY KEY,"
                       "USER_NAME VARCHAR(450) NOT NULL,"
                       "USER_KEY VARCHAR(450) NOT NULL, "
                       "USER_ROLE VARCHAR(450) NOT NULL, "
                       "CREATED_TIME BIGINT NOT NULL)")
        connection.commit()
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def multiprocessing_func(x):
    connection = connect_to_database()
    cursor = connection.cursor()

    for i in range(0, 100000):
        cursor.execute("INSERT INTO ALL_USER "
                       "(USER_ID, USER_NAME, USER_KEY, USER_ROLE, CREATED_TIME) VALUES (%s, %s, %s, %s, %s)",
                       [str(uuid.uuid4()) + str(randint(0, 999999999)), random.choice(NAMES), str(uuid.uuid4()),
                        random.choice(ROLES), int(time.time())])
        connection.commit()
    connection.close()
    cursor.close()


if __name__ == '__main__':
    startTime = time.time()
    processes = []
    for i in range(0, 20):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
    print('Process class took {} seconds'.format(time.time() - startTime))
