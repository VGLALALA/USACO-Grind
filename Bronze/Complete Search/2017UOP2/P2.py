from testcaseManager.runner.testRunner import TestRunner

def thing(inp):
    from collections import Counter
    n, m = map(int, inp[0].split())
    spotPattern = [[] for i in range(m)]
    plainPattern = [[] for i in range(m)]
    for i in range(n):
        # print(inp[i + 1])
        for index,letter in enumerate(inp[i + 1]):
            if letter not in spotPattern[index]:
                spotPattern[index].append(letter)
    for i in range(n):
        # print(inp[n + i + 1])
        for index, letter in enumerate(inp[n + i + 1]):
            if letter not in plainPattern[index]:
                plainPattern[index].append(letter)
    # print(spotPattern)
    # print(plainPattern)
    counter = 0
    for i in range(m):
        if not any(letter in spotPattern[i] for letter in plainPattern[i]):
            counter += 1
    return counter
        
            

runner = TestRunner()
runner.runTests(thing)