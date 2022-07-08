# speed_test_python_lookups
Implements a simple Python3 lookup in various ways to see which is fastest.

Results on a 2021 MBP M1 Pro:
```
Verify the algorithms are correct:
check_dict('ta')=> True
check_dict('foo')=> False
check_local('ta')=> True
check_local('foo')=> False
check_global('ta')=> True
check_global('foo')=> False
check_local_additional('ta', 'bar')=> True
check_local_additional('foo', 'bar')=> False
check_for('ta')=> True
check_for('foo')=> False

Time the various algorithms:
timeit dict:  1.613118625
timeit local:  3.325213208
timeit global:  3.3642712500000007
timeit local additional:  4.587791874999999
timeit for:  5.8532428329999995
```
