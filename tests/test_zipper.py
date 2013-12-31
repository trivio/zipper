from nose.tools import *
import zipper

def test_zipper_list_tree():
  tree = [20, [0,1], 4, [5, 6, [7,8]]]

  loc = zipper.list(tree)

  # the current node() is the entire tree
  eq_(loc.node(), tree)

  # .. which happens to be the same as calling root
  eq_(loc.root(), tree)

  # Moving down and calling node
  eq_(loc.down().node(), 20)


  eq_(loc.down().up().node(), tree)


  # calling root anywhere in the tree produces 
  # the entire tree
  eq_(loc.down().root(), tree)


  eq_(loc.down().right().node(), [0,1])

  eq_(loc.down().right().left().node(), 20)


  eq_(loc.down().right().right().node(), 4)
  eq_(loc.down().right().right().right().node(), [5, 6, [7,8]])

  # can't move down in trees
  eq_(loc.down().down(), None)

  eq_(loc.down().right().down().node(), 0)


def test_zipper_dict_tree():
  tree = dict(left=dict(left=1, right=2),right=3)
  loc = zipper.dict(tree)


def test_leftmost_descendant():
  top = zipper.list([ [[1], 2], [3], 4])
  eq_(
    top.leftmost_descendant().node(),
    1
  )

def test_rightmost_descendant():
  top = zipper.list([ [[1], 2], [3], 4])
  eq_(
    top.rightmost_descendant().node(),
    4
  )

  top = zipper.list([ [[1], 2], [3], [4,[5,6]]])
  eq_(
    top.rightmost_descendant().node(),
    6
  )

  eq_(
    top.rightmost_descendant().rightmost_descendant().node(),
    6
  )
  

def test_preorder_iter():
  top = zipper.list([1, [2,3], 4])
  eq_(
    [n.node() for n in top.preorder_iter()],
    [1, [2,3], 2, 3, 4, [1,[2,3],4]]
  )


def test_postorder_iter():
  top = zipper.list([1, [2,3],4])

  eq_(
  [n.node() for n in   top.postorder_iter()],
  [1, 2, 3, [2,3], 4, [1, [2,3], 4]]
  )

def test_leftmost():
  top = zipper.list([1, [2,3], 4])

  # the top of the tree is the left most node at this level
  eq_(
    top.leftmost().node(),
    [1, [2,3], 4]
  )

  eq_(
    top.down().leftmost().node(),
    1
  )

def test_rightmost():
  top = zipper.list([1, [2,3], 4])

  # the top of the tree is the left most node at this level
  eq_(
    top.rightmost().node(),
    [1, [2,3], 4]
  )

  eq_(
    top.down().rightmost().node(),
    4
  )


def test_insert_left():
  top = zipper.list([1, [2,3], 4])
  # can't insert at the top
  assert_raises(IndexError, top.insert_left,0)

  eq_(
    top.down().insert_left(0).root(),
    [0, 1, [2,3], 4]
  )

def test_insert_right():
  top = zipper.list([1, [2,3], 4])
  # can't insert at the top
  assert_raises(IndexError, top.insert_right,5)

  eq_(
    top.down().insert_right(1.5).root(),
    [1, 1.5, [2,3], 4]
  )

  eq_(
    top.down().right().down().insert_left(1.5).root(),
    [1, [1.5,2,3], 4]
  )

def test_replace():
  top = zipper.list([1, [2,3], 4])

  eq_(
    top.replace([9]).root(),
    [9]
  )

  eq_(
    top.down().replace(0).root(),
    [0, [2,3], 4]
  )

def test_insert():
  top = zipper.list([1, [2,3], 4])
  eq_(
    top.insert(0).root(),
    [0, 1, [2,3], 4]
  )

def test_append():
  top = zipper.list([1, [2,3], 4])
  eq_(
    top.append(5).root(),
    [1, [2,3], 4, 5]
  )

def test_remove():
  top = zipper.list([1, [2,3], 4])

  # can't remove top node
  assert_raises(IndexError, top.remove)

  eq_(
    top.down().right().remove().root(),
    [1, 4]
  )  

  eq_(
    top.down().right().down().remove().root(),
    [1, [3], 4]
  )  


  top = zipper.list([[[1.1,1.2],1.3], 2,3, 4])


  eq_(
    top.down().down().right().node(),
    1.3
  )  

  eq_(
    top.down().down().right().remove().node(),
    1.2
  )

def test_edit():
  top = zipper.list([1, [2,3], 4])

  eq_(
    top.down().edit(lambda node, k: node+k, 1).root(),
    [2, [2,3], 4]
  )

def test_move_to():
  top = zipper.list([1, [2,3, [4,[5,6]]], [7,8]])

  n = top.down().right().down().right().right().down()
  eq_(
    n.node(),
    4
  )

  right_most = n.top().rightmost_descendant()
  eq_(
    right_most.node(),
    8
  )

  eq_(
    right_most.move_to(n).node(),
    4
  )

def test_ancestor():
  top = zipper.list([1, [2,3, [4,[5,6]]], [7,8]])

  n = top.down().right().down().right().right().down().right().down()
  eq_(
    n.node(),
    5
  )

  # This is the equivalent of up
  eq_( 
    n.ancestor(lambda l: True).node(),
    [5,6]
  )

  # this filter returns ancestor with 2 elements
  f = lambda l: len(l.node()) % 2 == 0

  loc = n.ancestor(f)

  eq_(
    loc.node(),
    [5,6]
  )

  loc = loc.ancestor(f) 
  eq_(
    loc.node(),
    [4,[5,6]]
  )

  loc = loc.ancestor(f) 
  eq_(
    loc,
    None
  )




