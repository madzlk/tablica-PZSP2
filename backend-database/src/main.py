from orchestrator import Orchestrator
import logging
import time

# Nothing to test here, just using other already made methods/functions.

# This just wraps the python logging function into a dependency injection for the Orchestrator
class Logger:
    def __init__(self):
        pass

    def log(self, message):
        logging.warning(message)

# Calling the Orchestrator to update the data every minute, and printing any errors that appear.
def main():
    orch = Orchestrator(Logger())
    while True:
        start = time.time()
        orch.data_collection_cycle()
        # This value was derived via testing; using this value the data if updated roughly once every minute.
        time.sleep(36.5)
        print(f'time: {time.time() - start}')

if __name__ == '__main__':
    main()