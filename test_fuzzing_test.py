# test_fuzzing_test.py
from fuzzing import fuzzing_test

def test_run():
    result = fuzzing_test.run()
    assert isinstance(result, dict)
    assert sum(result.values()) == 1  # shots=1