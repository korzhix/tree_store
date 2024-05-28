from typing import List, Optional
from typing_extensions import TypedDict
from pprint import pprint


# Data validation scheme
class NodeData(TypedDict, total=False):
    id: int
    parent: int | str
    type: Optional[str | None]


class TreeStore:
    def __init__(self, node_items: List[NodeData]):
        self.data = node_items
        self.adj = matrix = [[0 for column in range(len(self.data))]
                             for i in range(len(self.data))]

        for node in self.data:
            try:
                # symmetric adjacency matrix as a data pointer and mapper
                self.adj[node['parent'] - 1][node['id'] - 1] = 1
                self.adj[node['id']-1][node['parent']-1] = 1
            except TypeError:
                pass

    def get_item(self, item_id: int) -> NodeData:
        return self.data[item_id - 1]

    def get_all(self) -> List[NodeData]:
        return self.data

    def get_parents(self, item_id: int) -> List[NodeData]:
        parents = []
        item = self.data[self.adj[item_id].index(1)]
        while item['parent'] != 'root':
            item = self.data[self.adj[item_id].index(1)]
            item_id = self.adj[item_id].index(1)
            parents.append(item)
        return parents

    def get_children(self, item_id: int) -> List[NodeData]:
        children = []
        for col in range(len(self.adj)):
            if self.adj[item_id - 1][col] and item_id - 1 <= col:
                children.append(self.data[col])
        return children

    def print_adj(self):
        pprint(self.adj)
