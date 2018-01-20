class Node(object):
    def __init__(self, item):
        self.item = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.__root = None

    def add(self, item):
        node = Node(item)
        if self.__root is None:
            self.__root = node
        else:
            # 以队列的方式变量树
            queue = []
            queue.append(self.__root)

            while queue:
                cur = queue.pop(0)

                if cur.lChild is None:
                    cur.lChild = node
                    return
                if cur.rChild is None:
                    cur.rChild = node
                    return
                queue.append(cur.lChild)
                queue.append(cur.rChild)

    # 广度优先遍历，层次遍历
    def breath_travel(self):
        if self.__root is None:
            return

        queue = []
        queue.append(self.__root)

        while queue:
            cur = queue.pop(0)
            print(cur.item)

            if cur.lChild is not None:
                queue.append(cur.lChild)
            if cur.rChild is not None:
                queue.append(cur.rChild)

    # 深度优先遍历
    def depth_travel(self):
        self.post_order(self.__root)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.lChild)
        self.post_order(node.rChild)
        print(node.item, end=" ")

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.lChild)
        print(node.item, end=" ")
        self.in_order(node.rChild)

    def pre_order(self, node):
        if node is None:
            return
        print(node.item, end=" ")
        self.pre_order(node.lChild)
        self.pre_order(node.rChild)