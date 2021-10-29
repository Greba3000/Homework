# Implement the [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

from threading import Thread, Lock
from time import sleep


class Fork:
    def __init__(self, number: int):
        self.number = number
        self.lock = Lock()

    def take(self):
        self.lock.acquire()

    def put(self):
        self.lock.release()

    def is_free(self):
        return not self.lock.locked()


class Philosopher(Thread):
    def __init__(self, number: int, left_fork: Fork, right_fork: Fork):
        super(Philosopher, self).__init__()
        self.number = number
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self) -> None:
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f'Philosopher {self.number} is thinking!\t')
        sleep(1)
        print(f'Philosopher {self.number} is ready to eat!\t')

    def eat(self):
        left_fork, right_fork = self.left_fork, self.right_fork

        if left_fork.is_free():
            # take left_fork
            left_fork.take()
            print(f'Philosopher {self.number} took fork {left_fork.number}!\t')

            if right_fork.is_free():
                # take right_fork
                right_fork.take()
                print(f'Philosopher {self.number} took fork {right_fork.number}!\t')

                print(f'Philosopher {self.number} started eating!\t')
                sleep(1)
                print(f'Philosopher {self.number} finished eating!\t')

                left_fork.put()
                print(f'Philosopher {self.number} put fork {left_fork.number}!\t')

                right_fork.put()
                print(f'Philosopher {self.number} put fork {right_fork.number}!\t')

            else:
                # if right fork is taken, put left fork and go think
                left_fork.put()
                print(f"Philosopher {self.number} can't eat and put fork {left_fork.number}!\t")
        # if left fork is taken, go think


if __name__ == '__main__':
    NUM_PHIL_FORK = 5

    forks = [Fork(num) for num in range(NUM_PHIL_FORK)]
    philosophers = [Philosopher(num, forks[num % NUM_PHIL_FORK], forks[(num + 1) % NUM_PHIL_FORK]) for num in
                    range(NUM_PHIL_FORK)]

    for philosopher in philosophers:
        philosopher.start()

