from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 19:
        return 6 * (g(n - 7) - 36)
    return f(n - 4) + 3580


@lru_cache()
def g(n):
    if n < 248045:
        return g(n + 9) - 4
    return n / 20 + 28
for n in range(248046)[::-1]:
    g(n)

print(f(673))