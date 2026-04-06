import time
import matplotlib.pyplot as plt
from pathlib import Path

from HVLCS import HVLCS

def read_input_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        char, value = lines[i].split()
        values[char] = int(value)

    A = lines[k + 1]
    B = lines[k + 2]
    return values, A, B


def scalability(input_dir="../inputs"):
    base_path = Path(__file__).resolve().parent
    inputs_path = (base_path / input_dir).resolve()
    
    x = []
    times = []

    for file_path in sorted(inputs_path.glob("*.txt")):
        values, A, B = read_input_file(file_path)

        start = time.perf_counter()
        max_value, subsequence = HVLCS(values, A, B)
        end = time.perf_counter()

        elapsed = end - start
        times.append(elapsed)
        x.append(len(A) * len(B))
        
    plt.scatter(x, times)
    plt.xlabel("Product of Input Lengths (|A| * |B|)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Product of Input Lengths")
    plt.savefig("question1.png")
    plt.clf()


if __name__ == "__main__":
    scalability()