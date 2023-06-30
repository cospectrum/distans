import random
import math

from distans import cos_sim

from distans.stuff import angular_dist, angular_sim, jaccard_sim


def random_vec(dim: int = 3) -> list[float]:
    return [random.random() for _ in range(dim)]


def eq(a: float, b: float) -> bool:
    return math.isclose(a, b)


dim = random.randint(1, 100)
a = random_vec(dim)
b = random_vec(dim)


def test_jaccard() -> None:
    assert eq(jaccard_sim(set(a), a), 1)
    assert eq(jaccard_sim(set(a), []), 0)

    assert 0 <= jaccard_sim(set(a), b) <= 1


def test_cos_sim() -> None:
    assert eq(cos_sim(a, a), 1)
    a_neg = [-x for x in a]
    assert eq(cos_sim(a, a_neg), -1)
    assert -1 <= cos_sim(a, b) <= 1


def test_angular() -> None:
    assert eq(angular_sim(a, a), 1)
    assert eq(angular_dist(a, a), 0)

    sim = angular_sim(a, b)
    assert 0 <= sim <= 1
    assert eq(angular_dist(a, b), 1 - sim)
