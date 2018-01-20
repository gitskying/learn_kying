# coding=utf-8
from doubleLinkList import DoubleLinkList


class Stack(object):
    def __init__(self):
        self.items = DoubleLinkList

    def push(self, item):
        """添加一个新的元素"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.items.pop()

    def is_empty(self):
        """判断栈是否为空"""
        return self.items.empty

    def size(self):
        """返回栈的元素个数"""
        return self.items.length