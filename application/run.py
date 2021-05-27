import time

import log


def hello_log():
    while True:
        log.registry(log.LOGGING_ENUM.INFO, 'Info...')
        log.registry(log.LOGGING_ENUM.WARNING, 'Warning...')
        log.registry(log.LOGGING_ENUM.ERROR, 'Error...')
        time.sleep(5)


if __name__ == '__main__':
    # TODO: treating if not has directory logs
    hello_log()
