Zipper [![Build Status](https://travis-ci.org/trivio/zipper.png)](https://travis-ci.org/trivio/zipper)
======

A datastructure, first described by Huet, is used to traverse and 
manipulate immutable trees. This library is a port of the zipper
implementation found in Clojure.

Usage
-----

The zipper module provides several functions for creating a Loc object which
represents the current focal point in the tree.



```
>>> import zipper
>>> top = zipper.list([1, [2, 3], 4])

>>> print top.down().right().node()
[2,3]

>>> print top.down().right().down().node()
2

>>> print top.down().right().down().replace(0).root()
[1, [0, 3], 4]

```



