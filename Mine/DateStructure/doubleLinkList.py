# coding=utf-8
class Node(object):    # 节点
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):
        self.__head = None

    def empty(self):
        # if self.__head is None:
        #     return True
        # else:
        #     return False
        return self.__head is None

    def length(self):
        cursor = self.__head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        cursor = self.__head
        while cursor is not None:
            print(cursor.item, end="  ")
            cursor = cursor.next

    def add(self, item):    # 头插
        node = Node(item)
        if self.__head is not None:
            self.__head.pre = node
            node.next = self.__head
        self.__head = node

    def append(self, item):    # 尾插
        if self.__head is None:
            self.add(item)
        else:
            node = Node(item)
            cursor = self.__head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node
            node.pre = cursor

    def insert(self, position, item):    # 指定位置
        try:
            position = int(position)
        except Exception as e:
            print(e)
        if position <= 0:
            self.add(item)
        elif position > self.length():
            self.append(item)
        else:
            index = 0
            node = Node(item)
            cursor = self.__head
            while index < position-1:
                cursor = cursor.next
                index+=1
            node.next = cursor.next    # 应该先把插入节点和后面接起来，再接前面
            cursor.next.pre = node
            cursor.next = node
            node.pre = cursor

    def remove(self, item):
        cursor = self.__head
        while cursor is not None:
            if cursor.item == item:
                if cursor.pre is None:
                    cursor.__head = cursor.next
                else:
                    cursor.pre.next = cursor.next
                    cursor.next.pre = cursor.pre
                break
            cursor = cursor.next

    def pop(self):
        cursor = self.__head
        while cursor.next is not None:
            cursor = cursor.next
        cursor.pre.next = None
        return cursor.item


    def search(self, item):
        cursor = self.__head
        while cursor is not None:
            if cursor.item == item:
                return True
            cursor = cursor.next
        else:
            return False


