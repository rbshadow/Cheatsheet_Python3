import datetime
import time


def dateTime():

    for i in range(10):
        time.sleep(1)
        t = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        print('{}'.format(t))


if __name__ == '__main__':
    dateTime()
