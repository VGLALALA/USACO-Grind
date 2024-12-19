from testcaseManager.runner.testRunner import TestRunner
def thing(inp):
    GENOME_ID = {"A": 0, "T": 1, "C": 2, "G": 3}

    cow_num, genome_len = [int(i) for i in inp[0].split()]

    spotted = []
    for i in range(cow_num):
        genome_str = inp[i + 1]
        genome = []
        for g in range(genome_len):
            # A -> 0, C -> 1, T -> 2, G -> 3
            genome.append(GENOME_ID[genome_str[g]])
        spotted.append(genome)

    plain = []
    for i in range(cow_num):
        genome_str = inp[cow_num + i + 1]
        genome = []
        for g in range(genome_len):
            genome.append(GENOME_ID[genome_str[g]])
        plain.append(genome)

    valid_sets = 0
    for a in range(genome_len):
        for b in range(a + 1, genome_len):
            for c in range(b + 1, genome_len):
                spotted_ids = [False for _ in range(64)]
                for sc in range(cow_num):
                    total = spotted[sc][a] * 16 + spotted[sc][b] * 4 + spotted[sc][c] * 1
                    spotted_ids[total] = True

                for pc in range(cow_num):
                    total = plain[pc][a] * 16 + plain[pc][b] * 4 + plain[pc][c] * 1
                    if spotted_ids[total]:
                        break
                else:
                    valid_sets += 1
    return valid_sets

runner = TestRunner()
runner.runTests(thing,"int")