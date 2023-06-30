import random
from distans import l1, l2, l_inf, lp


dim = random.randint(1, 20)
a = [random.randint(-10, 10) for _ in range(dim)]
b = [random.randint(-10, 10) for _ in range(dim)]


def test_l1() -> None:
    assert l1(a) == sum(abs(x) for x in a)
    assert l1(a, b) == sum(abs(x - y) for x, y in zip(a, b))


def test_l2() -> None:
    assert l2(a) == sum(x * x for x in a) ** 0.5
    assert l2(a, b) == sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def test_l_inf() -> None:
    assert l_inf(a) == max(abs(x) for x in a)
    assert l_inf(a, b) == max(abs(x - y) for x, y in zip(a, b))


def test_lp() -> None:
    p = random.uniform(0, 10)
    p_inv = p**-1
    assert lp(a, p=p) == sum(abs(x) ** p for x in a) ** p_inv
    assert lp(a, b, p=p) == sum(abs(x - y) ** p for x, y in zip(a, b)) ** p_inv
