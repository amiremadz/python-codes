def hello(name="amir"):	
	return name

def other(func):
	print func("ali")

other(hello)		


def gensquares(N):
	for i in xrange(N):
		yield i**2


import random
def rand_num(low, high, n):
	for _ in xrange(n):
		yield random.randint(low, high)

class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = val
		InstanceCounter.count += 1

	@classmethod	
	def get_count(cls):
		return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)

print a.get_count()
print b.get_count()
print InstanceCounter.get_count()


import abc

class GetterSetter(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def set_val(self, value):
		return

	@abc.abstractmethod
	def get_val(self):
		return

class MyClass(GetterSetter):

	def set_val(self, input):
		self.val = input

	def get_val(self):
		return self.val

x = MyClass()
x.set_val(5)
print x.get_val()


class SumList(object):
	def __init__(self, this_list):
		self.mylist = this_list

	def __add__(self, other):
		new_list = [ a+b for a,b in zip(self.mylist, other.mylist)]
		return SumList(new_list)

	def __repr__(self):
		return str(self.mylist)

cc = SumList([1, 2, 3])
dd = SumList([4, 5, 6])

ee = cc + dd
print ee

# __contains__
# __eq__
# __getslice__
# __len__


class MyDict(dict):
	# re-implement a dict method
	def __setitem__(self, key, val):
		print "setting a key and value"
		# self[key] = val  !! Runtime error, max recursion
		dict.__setitem__(self, key, val)

dd = MyDict()
print dd['a'] = 5
print dd.keys()


class MyList(list):
	def __getitem__(self, index):
		if index==0: raise IndexError
		if index > 0: index -= 1
		return list.__getitem__(self, index)

	def __setitem__(self, index, value):	
		if index == 0: raise IndexError
		if index > 0: index -= 1
		list.__setitem__(self, index, value)

x = MyList(['a', 'b', 'c'])
x.append('spam')
print x[1]
print x[4]


class GetSet(object):

	def __init__(self, value):
		self._attrval = value

	@property
	def var(self):
		print 'getting the "var" attribute'
		return self._attrval

	@var.setter
	def var(self, value):
		print 'setting the "var" attribute'
		self._attrval = value

	@var.deleter
	def var(self):
		print 'deleting the "var" attribute'
		self._attrval = None
    
me = GetSet(5)

me.var = 1000
print me.var
del me.var
print me.var			

# __slots__

# __double_leading_underscore : should not be subclassed

class Amir(object):
	__mangled_name = "amir"

amir = Amir()
print amir.__mangled_name
print amir._Amir__mangled_name



with open('fil.txt') as fh:
	for line in fh:
		line = line.rstrip()
		print line

fh = opne('file.txt')
for line in fh:
	print(line)
fh.close()


class MyClass(object):

	def __enter__(self):
		print('we have entered "with"')
		return self

	# Cleanup, Catch exceptions
	def __exit__(self, type, value, traceback):
		print('error type: {0}'.format(type))
		print('error value: {0}'.format(value))	
		print('error traceback: {0}'.format(traceback))

	def sayhi(self):
		print('hi, instance %s' % (id(self)))

# cc = MyClass()
with MyClass() as cc:
	cc.sayhi()
	5/0

print('after the "with" block') 


class MyError(Exception):
    def __init__(self, *args):
        print 'calling init!'
        if args:
            self.message = arge[0]
        else:
            self.message = ''

    def __str__(self):
        print 'calling str'
        if self.message:
            return 'MyError exception message: {0}'.format(self.message)
        else:
            return "MyError message!"

raise MyError
raise MyError('We have a problem!')                      




import re # Regular expressions
re.search(r'^\d\d\d\d-\d\d-\d\d\$', this_date)


import sys

try:
	arg = sys.argv[1]
	num = int(arg)
except(IndexError, ValueError):
	sys.exit("please eneter an integer")



import pickle

mylist = ['a', 'b']

with open('datafile.txt', 'w') as fh:
	pickle.dump(mylist, fh)

with open('datafile.txt') as fh:
	unpickledlist = pickle.load(fh)


x = pickle.dumps(mylist)
var = pickle.loads(x)


class MyClass(object):
	def __init__(self, init_val):
		self.val = init_val

	def increment(self):
		self.val += 1

cc = MyClass(5)
cc.increment()

with open('datafile.txt') as fh:
	pickle.dump(cc, fh)

with open('datafile.txt') as fh:
	unpickled_cc = pickle.load(fh)


import json

with open('backup_config.json') as fh:
	conf = json.load(fh)

print conf

conf['newkey'] = 5000

with open('backup_config') as fh:
	json.dump(conf, fh, indent=4, separators=(',', ': '))


x = json.dumps({'a': [1, 2, 3], 'b': [7, 8]})
var = json.loads(x)	


import yaml

mydict = {'a':1, 'b':2}
mylist = [1, 2, 3]
mytuple = ('x', 'y')

print yaml.dump(mydict, default_flow_style = False)
print yaml.dump(mylist, default_flow_style = False)
print yaml.dump(mytuple, default_flow_style = False)

with open('app.yaml') as fh:
	struct = yaml.load(fh)

print json.dumps(struct, indent=4, separators=(',', ': '))


x = MyClass(5)
x.increment()

with open('obj.yaml') as fh:
	yaml.dump(x, fh)

with open('obj.yaml') as fh:
	inst = yaml.load(fh) # yaml.safe_load(fh)

print inst.val


import logging

# loggind.DEBUG logging.WARNING
logging.basicConfig(level=logging.INFO, filename=='example.log', filemode='w', 
	format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logging.debug('debug')
logging.info('info')
logging.warning('warning')

import timeit
print timeit.timeit(stmt="mydict['c']", setup="mydict = {'a':5, 'b':6, 'c':7}", number=1000000)

pythpn -m timeit -n 1000000 -s "mydict = {'a':5, 'b':6, 'c':7}" "mydict['c']"


def testme(this_dict, key):
	return this_dict[key]

print timeit.timeit("testme(mydict, key)", 
	setup="from __main__ import testme; mydict = {'a':5, 'b':6, 'c':7}; key = 'c'", number=1000000)	