import unittest
from tree_store import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


class TestTreeStore(unittest.TestCase):
    def setUp(self):
        self.store = TreeStore(items)

    def test_get_all(self):
        self.assertCountEqual(self.store.get_all(),
                              [{"id": 1, "parent": "root"}, {"id": 2, "parent": 1, "type": "test"},
                               {"id": 3, "parent": 1, "type": "test"}, {"id": 4, "parent": 2, "type": "test"},
                               {"id": 5, "parent": 2, "type": "test"}, {"id": 6, "parent": 2, "type": "test"},
                               {"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}])
        self.assertDictEqual(self.store.get_item(7),
                             {"id": 7, "parent": 4, "type": None})
        self.assertCountEqual(self.store.get_children(4),
                              [{"id": 7, "parent": 4, "type": None},
                               {"id": 8, "parent": 4, "type": None}])
        self.assertCountEqual(self.store.get_children(5), [])
        self.assertCountEqual(self.store.get_parents(7),
                              [{"id": 4, "parent": 2, "type": "test"},
                               {"id": 2, "parent": 1, "type": "test"},
                               {"id": 1, "parent": "root"}])


if __name__ == "__main__":
    unittest.main()
