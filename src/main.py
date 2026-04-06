from HVLCS import HVLCS

def main():
    k = int(input())
    values = {}
    
    for i in range(k):
        line = [n for n in input().strip().split(" ")]
        values[line[0]] = int(line[1])

    A = input().strip()
    B = input().strip()

    max_value, subsequence = HVLCS(values, A, B)
    print(max_value)
    print(subsequence)

if __name__ == "__main__":
    main()