Q = int(input())

MOD = int(1e9 + 7)
maxN = 0
queries = []
for _ in range(Q):
    N, K, X = [int(x) for x in input().split(' ')]
    queries.append((N, K, X))
    maxN = max(maxN, N)

def prepare_inv_modulo(maxN):
    # prepare the inv module array
    inv = [1] * (maxN + 1)
    for i in range(2, len(inv)):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
    for i in range(2, len(inv)):
        inv[i] = (inv[i - 1] * inv[i]) % MOD
    return inv

def prepare_factorial_modulo(maxN):
    factorials = [1] * (maxN + 1)
    for i in range(1, maxN + 1):
        factorials[i] = factorials[i - 1] * i % MOD
    return factorials


def coef(n, m, factorials, inv):
    '''
    coef = n!/ (m! * (n - m)!)
    '''
    if m < 0 or m > n:
        return 0
    if m > n / 2:
        m = n - m

    result = factorials[n]
    result = (result * inv[m]) % MOD
    result = (result * inv[n - m]) % MOD
    return result

arr = [1,2,1,2,1]
msgs = []
inv = prepare_inv_modulo(maxN)
factorials = prepare_factorial_modulo(maxN)

for N, K, X in queries:
    N, K = N - 1, K - 1
    sum = 0
    for i in range(5):
        sum = (sum + arr[i] * coef(N, N - 2 - K + i, factorials, inv)) % MOD

    if sum == X:
        print('Correct')
    else:
        print('Incorrect')

