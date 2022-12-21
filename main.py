from mpi4py import MPI
import math
from random import random
from time import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("Process #", rank, "started")

N = 1000000


def generate_arrays(number, m):

    arr = []
    res = []

    for j in range(number):
        arr.append((random(), random()))

    for j in range(m):
        res.append(arr[:math.floor(len(arr) / m * (j + 1))])

    return res


def monte_carlo(arr):

    counter = 0

    for coordinates in arr:
        if coordinates[0] ** 2 + coordinates[1] ** 2 <= 1:
            counter += 1

    return 4 * counter / len(arr)


if __name__ == '__main__':

    if rank == 0:

        x1 = time()

        size = comm.Get_size()
        arrays = generate_arrays(N, size - 1)

        for i in range(size - 1):
            comm.send(arrays[i], dest=i + 1)

        result = []

        for i in range(1, size):
            response = comm.recv(source=i)
            result.append((i, response))

        for i in range(size - 1):
            print("Result of process", result[i][0], ":", result[i][1])

        x2 = time()
        print("Execution time:", x2 - x1)

    else:

        array = comm.recv(source=0)
        comm.send(monte_carlo(array), dest=0)
