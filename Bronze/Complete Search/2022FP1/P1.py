from testcaseManager.runner.testRunner import TestRunner
def thing(inp):
    t = int(inp[0])
    out = []
    for i in range(t):
        n = int(inp[i + 1])
        a = [int(l) for l in inp[i + 2].split()]
        