import sys
import bisect

def solve():
    data = sys.stdin.read().strip().split()

    N = int(data[0])
    a = list(map(int, data[1:1+N]))
    b = list(map(int, data[1+N:1+2*N]))

    T1 = 0
    for i in range(N):
        if a[i] == b[i]:
            left_count = i*(i+1)//2
            right_count = (N - i - 1)*(N - i)//2
            T1 += left_count + right_count

    A_by_species = [[] for _ in range(N+1)]
    B_by_species = [[] for _ in range(N+1)]
    for j in range(N):
        A_by_species[a[j]].append(j+1)
    for i in range(N):
        B_by_species[b[i]].append(i+1)

    T2 = 0

    def prefix_sums(arr):
        ps = [0]*(len(arr)+1)
        s = 0
        for i, val in enumerate(arr):
            s += val
            ps[i+1] = s
        return ps

    for s in range(1, N+1):
        A_list = A_by_species[s]
        B_list = B_by_species[s]
        if not A_list or not B_list:
            continue

        A_list.sort()
        B_list.sort()

        psA = prefix_sums(A_list)

        def sum_A(L, R):
            if R < L:
                return 0
            return psA[R+1] - psA[L]

        species_sum = 0
        nA = len(A_list)

        Alist = A_list

        for i_pos in B_list:
            u = bisect.bisect_right(Alist, N - i_pos) - 1

            if u >= 0:
                t_prime = bisect.bisect_left(Alist, i_pos) - 1
                if t_prime > u:
                    t_prime = u
                if t_prime < 0:
                    count_ = (u - 0 + 1)
                    sum1 = i_pos * count_
                else:
                    sum_p = sum_A(0, t_prime)
                    count2 = (u - (t_prime+1) + 1)
                    sum1 = sum_p + i_pos*count2
                species_sum += sum1

            L = u+1
            if L < nA:
                count_ = (nA - L)
                sum_max = 0
                t_dblprime = bisect.bisect_left(Alist, i_pos) - 1
                if t_dblprime < L:
                    sum_max = sum_A(L, nA-1)
                else:
                    if t_dblprime >= nA-1:
                        cnt_temp = (nA - L)
                        sum_max = i_pos * cnt_temp
                    else:
                        cnt1 = (t_dblprime - L + 1)
                        part1 = i_pos * cnt1
                        part2 = sum_A(t_dblprime+1, nA-1)
                        sum_max = part1 + part2
                sum2 = count_*(N+1) - sum_max
                species_sum += sum2

        T2 += species_sum

    print(T1 + T2)
solve()