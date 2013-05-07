Homer
=====

Sandbox for applications.

Usage
-----

Create an environment:

```
$ homer env
$ cd env
$ ls
bin  include  lib  local
```

Activate the environment:

```
$ cd env
$ source bin/activate
```

Install your application

```
$ cd some-application-that-i-can-compile
$ ./configure --prefix=$HOMER_PATH
$ make
$ make install
```

Installation
------------

Some dependencies:

1) python

Clone from the repository

```
$ git clone git://github.com/jpanganiban/homer.git
```

Install it

```
$ cd homer
$ sudo python setup.py install
```

or with a virtualenv

```
# Activate your environment the way you do...
$ python setup.py install
```

Why Another Sandbox
-------------------

Sandboxes are good. It keeps things tidy. Besides that,
it allows you to:

1) Install multiple versions of applications/libraries/etc without
  having to install something on top of another.

2) Keep track of which environment being used at a specific moment.

3) Easily switch environments.

4) Install without sudo. Badassssss!

Exposed Environment Variables
-----------------------------

Exposed environment variables

```
$HOMER_PATH  # Path to the environment
$HOMER_ENV  # Just a name you entered when you created your environment
```

More exposed environments

```
$_HOMER_OLD_PATH  # The old $PATH for backup
```
