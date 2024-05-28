'''
This code was found on Github
So that is not my solution and did another one. But this works fine too
Author :    https://github.com/shil252255/test_for_ooo_status/blob/master/good.py
'''

from collections import defaultdict


class TreeStore:
    _items_dict: dict[int: dict]
    _items_by_parents: dict[int: dict]
    _items_list: list[dict]

    def __init__(self, items: list[dict]):
        self._items_dict = {}
        self._items_list = []
        self._items_by_parents = defaultdict(list)
        for item in items:
            new_item = item.copy()
            self._items_by_parents[item['parent']].append(new_item)
            self._items_dict[item['id']] = new_item
            self._items_list.append(new_item)

    def getAll(self) -> list[dict]:
        return self._items_list

    def getItem(self, item_id: int) -> dict:
        return self._items_dict[item_id]

    def getChildren(self, item_id: int) -> list[dict]:
        return self._items_by_parents[item_id]

    def _getParent(self, item: dict) -> dict:
        while item['parent'] != 'root':
            yield (item := self._items_dict[item['parent']])

    def getAllParents(self, item_id: int) -> list[dict]:
        return list(self._getParent(self._items_dict[item_id]))


'''
P.S*
Also may work solutions based on classes like
class TreeNode(object):
    "Node of a Tree"
    def __init__(self, name='root', children=None,parent=None):
        self.name = name
        self.parent=parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

class Tree:
    """
    Tree implemenation as a collection of TreeNode objects
    """
    def __init__(self):
       self.root=None
       self.height=0
       self.nodes=[]

'''