import random

from distans import jaro_sim, jaro_winkler_sim


rand_char = lambda: random.randint(0, 100)


def random_permutation(seq: list) -> None:
    l = random.randint(0, len(seq) - 1)
    r = random.randint(0, len(seq) - 1)
    seq[l], seq[r] = seq[r], seq[l]


def random_replace(seq: list) -> None:
    i = random.randint(0, len(seq) - 1)
    seq[i] = rand_char()


def test_sim() -> None:
    a_len = random.randint(2, 60)
    a = [rand_char() for _ in range(a_len)]
    b = [x for x in a]
    b += [rand_char() for _ in range(random.randint(0, 10))]

    for _ in range(random.randint(0, 9)):
        random_permutation(b)

    for _ in range(random.randint(0, 7)):
        random_replace(b)

    fns = [jaro_sim, jaro_winkler_sim]
    for fn in fns:
        sim = fn(a, b)  # type: ignore
        assert 0.0 <= sim <= 1.0
