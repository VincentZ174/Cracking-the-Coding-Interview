#!/usr/bin/python

hash_table = [[] for _ in range(10)]


def hashing_func(key):
	return key % len(hash_table)


def insert(hash_table, key, value):
	hash_key = hashing_func(key)
	hash_table[hash_key].append(value)


print(hash_table)

insert(hash_table, 23427088, 'Vincent')
insert(hash_table, 23124291, 'Jessica')
insert(hash_table, 11233209, 'Jones')

print(hash_table)


