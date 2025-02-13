import heapq
class Stack:
    """A stack data structure for storing search history."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def get_all(self):
        return self.items[:]

class MaxHeap:
    """Max-heap for tracking top influencers based on scores."""
    def __init__(self):
        self.heap = []

    def add_influencer(self, influencer):
        heapq.heappush(self.heap, (-influencer.calculate_score(), influencer))

    def get_top_influencer(self):
        return self.heap[0][1] if self.heap else None

    def update_influencer(self, influencer):
        self.remove_influencer(influencer)
        self.add_influencer(influencer)

    def remove_influencer(self, influencer):
        self.heap = [item for item in self.heap if item[1] != influencer]
        heapq.heapify(self.heap)

class SplayTree:
    """A splay tree to manage influencers."""
    
    class Node:
        def __init__(self, influencer):
            self.influencer = influencer
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def _splay(self, root, influencer):
        """Splay operation to bring influencer to the root based on score."""
        if not root or root.influencer == influencer:
            return root

        # Left subtree case
        if influencer.calculate_score() < root.influencer.calculate_score():
            if root.left is None:
                return root

            # Zig-Zig (Left Left)
            if influencer.calculate_score() < root.left.influencer.calculate_score():
                root.left.left = self._splay(root.left.left, influencer)
                root = self._rotate_right(root)
            # Zig-Zag (Left Right)
            elif influencer.calculate_score() > root.left.influencer.calculate_score():
                root.left.right = self._splay(root.left.right, influencer)
                if root.left.right:
                    root.left = self._rotate_left(root.left)

            return self._rotate_right(root) if root.left else root

        # Right subtree case
        else:
            if root.right is None:
                return root

            # Zag-Zig (Right Left)
            if influencer.calculate_score() < root.right.influencer.calculate_score():
                root.right.left = self._splay(root.right.left, influencer)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            # Zag-Zag (Right Right)
            elif influencer.calculate_score() > root.right.influencer.calculate_score():
                root.right.right = self._splay(root.right.right, influencer)
                root = self._rotate_left(root)

            return self._rotate_left(root) if root.right else root

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def insert(self, influencer):
        if not self.root:
            self.root = self.Node(influencer)
        else:
            self.root = self._splay(self.root, influencer)
            new_node = self.Node(influencer)
            if influencer.calculate_score() < self.root.influencer.calculate_score():
                new_node.right = self.root
                new_node.left = self.root.left
                self.root.left = None
            else:
                new_node.left = self.root
                new_node.right = self.root.right
                self.root.right = None
            self.root = new_node

    def remove_root(self):
        if not self.root:
            return None
        removed_influencer = self.root.influencer
        if not self.root.left:
            self.root = self.root.right
        else:
            new_root = self._splay(self.root.left, removed_influencer)
            new_root.right = self.root.right
            self.root = new_root
        return removed_influencer