#!/usr/bin/env python3
#
# This implements a simple Python3 lookup in various ways to see which is fastest.
# I reordered the algorithms in the speed order I found on my MBP M1 Pro machine.
#
# I could have used timeit with number=loops instead of my own 'for in
# range' loops, but I think that the for loops have lower overhead.
#
# This code grew as I added more tests and I know it could be
# reorganized in a less repetitive form.
#

import timeit
import time

rrtypes  = ('any-dnssec',  'ds', 'rrsig',  'nsec', 'dnskey',  'nsec3',
            'nsec3param',  'dlv',  'cds',  'cdnskey',  'ta',  'type43',
            'type46', 'type47', 'type48', 'type50', 'type51', 'type59',
            'type60', 'type32768', 'type32769')

rrtypes_dict = {'any-dnssec': 1, 'ds': 1, 'rrsig': 1, 'nsec': 1,
                'dnskey': 1, 'nsec3': 1, 'nsec3param': 1, 'dlv': 1,
                'cds': 1, 'cdnskey': 1, 'ta': 1, 'type43': 1,
                'type46': 1, 'type47': 1, 'type48': 1, 'type50': 1,
                'type51': 1, 'type59': 1, 'type60': 1, 'type32768': 1,
                'type32769': 1}

def check_dict(rr):
    if rrtypes_dict.get(rr, None):
        return True
    else:
        return False

def check_local(rr):
    """ This is what the original code I was looking at did """

    if rr in ('any-dnssec', 'ds', 'rrsig', 'nsec', 'dnskey', 'nsec3', 'nsec3param',
              'dlv', 'cds', 'cdnskey', 'ta', 'type43', 'type46',
              'type47', 'type48', 'type50', 'type51', 'type59',
              'type60', 'type32768', 'type32769'):
        return True
    else:
        return False

def check_global(rr):
    if rr in rrtypes:
        return True
    else:
        return False

def check_local_additional(rr, additional):
    """ Test if adding a new value disables load-time optimization """

    if rr in ('any-dnssec', 'ds', 'rrsig', 'nsec',
              'dnskey', 'nsec3', 'nsec3param',
              'dlv', 'cds', 'cdnskey', 'ta',
              'type43', 'type46', 'type47',
              'type48', 'type50', 'type51',
              'type59', 'type60', 'type32768', 'type32769',
              additional):
        return True
    else:
        return False

def check_for(rr):
    for r in ['any-dnssec', 'ds', 'rrsig', 'nsec',
              'dnskey', 'nsec3', 'nsec3param',
              'dlv', 'cds', 'cdnskey', 'ta',
              'type43', 'type46', 'type47',
              'type48', 'type50', 'type51',
              'type59', 'type60', 'type32768', 'type32769']:
        if rr == r:
            return True
    return False

loops = 10000000

def loop_local():
    for i in range(loops):
        _ = check_local('ta')
    for i in range(loops):
        _ = check_local('foo')
    
def loop_global():
    for i in range(loops):
        _ = check_global('ta')
    for i in range(loops):
        _ = check_global('foo')
    
def loop_dict():
    for i in range(loops):
        _ = check_dict('ta')
    for i in range(loops):
        _ = check_dict('foo')
    
def loop_local_additional():
    for i in range(loops):
        _ = check_local_additional('ta', 'bar')
    for i in range(loops):
        _ = check_local_additional('foo', 'bar')
    
def loop_for():
    for i in range(loops):
        _ = check_for('ta')
    for i in range(loops):
        _ = check_for('foo')

print("Verify the algorithms are correct:")
    
print("check_dict('ta')=>", check_dict('ta'))
print("check_dict('foo')=>", check_dict('foo'))
print("check_local('ta')=>", check_local('ta'))
print("check_local('foo')=>", check_local('foo'))
print("check_global('ta')=>", check_global('ta'))
print("check_global('foo')=>", check_global('foo'))
print("check_local_additional('ta', 'bar')=>", check_local_additional('ta', 'bar'))
print("check_local_additional('foo', 'bar')=>", check_local_additional('foo', 'bar'))
print("check_for('ta')=>", check_for('ta'))
print("check_for('foo')=>", check_for('foo'))

print("")
print("Time the various algorithms:")
print("timeit dict: ",timeit.Timer(loop_dict).timeit(number=1))
print("timeit local: ", timeit.Timer(loop_local).timeit(number=1))
print("timeit global: ",timeit.Timer(loop_global).timeit(number=1))
print("timeit local additional: ", timeit.Timer(loop_local_additional).timeit(number=1))
print("timeit for: ", timeit.Timer(loop_for).timeit(number=1))
