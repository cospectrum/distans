def test_readme():
    from distans import lp

    a = [1, -2, 3]
    b = [3, 4, -5]

    p = 2
    norm = lp(a, p=p)
    dist = lp(a, b, p=p)

    from distans import jaro_sim, jaro_winkler_sim

    jaro_sim("hello", "helo")
    jaro_winkler_sim("hi", "hey")
