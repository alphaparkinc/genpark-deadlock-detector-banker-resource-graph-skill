"""Banker's Algorithm for Deadlock Avoidance
100% Python Standard Library.
"""

class BankersAlgorithm:
    """Safe state evaluator and deadlock avoidance engine."""
    def __init__(self, available, max_matrix, allocation):
        self.available = list(available)
        self.max = max_matrix
        self.allocation = allocation
        self.num_p = len(max_matrix)
        self.num_r = len(available)
        self.need = [
            [self.max[i][j] - self.allocation[i][j] for j in range(self.num_r)]
            for i in range(self.num_p)
        ]

    def is_safe_state(self):
        work = list(self.available)
        finish = [False] * self.num_p
        safe_sequence = []

        while len(safe_sequence) < self.num_p:
            found = False
            for p in range(self.num_p):
                if not finish[p]:
                    if all(self.need[p][r] <= work[r] for r in range(self.num_r)):
                        for r in range(self.num_r):
                            work[r] += self.allocation[p][r]
                        finish[p] = True
                        safe_sequence.append(p)
                        found = True
                        break
            if not found:
                return {"is_safe": False, "safe_sequence": []}

        return {"is_safe": True, "safe_sequence": safe_sequence}
