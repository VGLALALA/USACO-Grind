from testcaseManager.runner.testRunner import TestRunner
def thing(inp):
    inp = inp[0].strip()
    start = [-1 for _ in range(26)]
    end = [-1 for _ in range(26)]
    for v, c in enumerate(inp):
        c_id = ord(c) - ord("A")
        if start[c_id] == -1:
            start[c_id] = v
        else:
            end[c_id] = v

    crossing_pairs = 0
    for i in range(26):
        for j in range(26):
            crossing_pairs += start[i] < start[j] and start[j] < end[i] and end[i] < end[j]

    return crossing_pairs
runner = TestRunner()
runner.runTests(thing,"int")
    