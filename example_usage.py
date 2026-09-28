from client import BankersAlgorithm

def main():
    avail = [3, 3, 2]
    max_m = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    banker = BankersAlgorithm(avail, max_m, alloc)
    res = banker.is_safe_state()
    print("Banker's Algorithm Verification:")
    print(f"Is Safe: {res['is_safe']}")
    print(f"Safe Execution Sequence: {res['safe_sequence']}")

if __name__ == "__main__":
    main()
