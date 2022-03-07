# 동적 프로그래밍(Dynamic Programming)

## 동적 프로그래밍이란?
- 동적 프로그래밍은 재귀적으로 문제를 해결하는 방식을 최적화하여 문제를 해결하는 알고리즘이다.
- 동적 프로그래밍은 재귀적으로 문제를 해결할 때, 같은 입력에 대한 출력이 지속적으로 반복된다면 해당 값을 저장하여 사용하는 것을 통해서 지속적으로 같은 연산이 일어나지 않게 한다.
- 일반적으로 재귀 코드의 시간 복잡도는 지수적이다. 하지만 다이나믹 프로그래밍을 적용하게 된다면 시간 복잡도를 산술적으로 바꿀 수 있다.
- 동적 프로그래밍으로 문제를 해결하기 위해서는 `Overlapping Subproblems`와 `Optimal Substructure`2가지의 성질을 가지고 있어야 한다.
- **Overlapping Subproblem**의 경우, 동적 프로그래밍으로 해결하고 싶은 문제가 반복되는 작은 문제들로 이루어져 있어야 한다는 것이다. 즉, 저장한 값들이 지속적으로 재사용이 이루어져야 의미가 있다는 뜻이다.
- **Optimal Substructure**의 경우, 문제의 최적이 문제를 나눈 작은 문제들의 최적으로 구할 수 있어야 한다는 것이다. 즉, 해결하고자 하는 문제를 작은 문제로 나누었을 때, 작은 문제의 최적들로 구한 답과 해결하고자 하는 문제의 최적이 다르다면 동적 프로그래밍을 활용할 수 없다.
- 아래의 코드는 피보나치 수열을 재귀적으로 구하는 코드와 동적 프로그래밍을 적용하여 구하는 코드이다.
```python
# Recursion solution
def fibo_recursion(n):
    if n <= 1:
        return n
    return fibo_recursion(n-1) + fibo_recursion(n-2)

# 결과 : fibo_recursion(40) : 31.6초

def fibo_dynamic(n):
    cache = [0, 1]
    for i in range(2, n):
        cache[i].append(cache[i-1] + cache[i-2])
    return cache[-1]

# 결과: fibo_dynamic(40): 1.67e-05초
```

## 동적 프로그래밍 수행 절차
1. 메모리에 저장할 상태를 정의한다.
1. 상태 간의 관계를 정의한다.
1. 반복되는 값을 저장하며, 원하는 값을 찾는다.

## 반복되는 값을 어떻게 저장할 것인가 ( Tabulation vs Memoization )

### Tabulation ( 상향식 )
- 반복되는 답들을 작은 단위부터 큰 단위로 저장하면서 해당 답들을 재사용하는 방식이다.
- 문제에서 필요한 정답이 `dp[n]`인 경우, `dp[0]`에서 시작하여 `dp[n]`으로 값을 찾아가는 방식으로 답을 찾는 방식이다.
- Tabulation 방식을 사용하여 팩토리얼을 구현하면 다음과 같다.
```python
MAXN = 1000
def factorial(n):
    dp = [0]*MAXN
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i-1]*i
    return dp[n]
```
- 위의 방식은 `dp`라는 배열을 표처럼 사용하여 재사용되는 값들을 저장하는 형식이다. `재사용하는 값을 저장하는 방식이 표를 이용하여 저장하기 때문에` **tabulatoin method**라고 부른다.

### Memoization ( 하향식 )
- 반복되는 답들을 큰 단위부터 작은 단위로 나누면서 저장이 되어 있는 값들은 재사용하고 그렇지 않은 경우는 저장하는 방식이다.
- 문제에서 필요한 정답이 `dp[n]`인 경우, `dp[n]`에서 시작해서 이 값을 이루고 있는 작은 단위로 나누어서 `dp[0]`으로 가면서 값을 저장하고 재사용하며 `dp[n]`을 찾는 방식이다.
- Memoization 방식을 사용하여 팩토리얼을 구현하면 다음과 같다.
```python
MAXN = 1000
dp = [-1]*MAXN

def factorial(n):
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = n*factorial(n-1)
    return dp[n]
```

### Tabulation vs Memoization
- Tabulation의 경우는 이전 상태를 그대로 사용하므로, 상대적으로 빠르지만, Memoization의 경우 여러 조건문과 재귀를 호출하므로 상대적으로 느리다.
- Tabulation의 경우는 모든 하위 문제들을 적어도 한 번이상은 계산을 하게 되지만, Memoization의 경우는 필요한 값만을 계산하게된다. 따라서 계산 횟수는 모든 경우를 계산하는 Tabulation보다 Memoization인 경우가 더 빠르다.


## 참고 문헌
[GeeksForGeeks](https://www.geeksforgeeks.org/dynamic-programming/)
