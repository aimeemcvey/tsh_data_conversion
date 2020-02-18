# test_tsh_test.py
import tsh_test


def test_tsh_test_hyper():
    from tsh_test import diagnose_tsh
    answer = diagnose_tsh([0.1, 0.5, 3.0, 1.6, 2.1])
    expected = "hyperthyroidism"
    assert answer == expected
