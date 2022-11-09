# @Time: 2022/11/8 23:04
# @Author: 李树斌
# @File : 纸牌.py
# @Software :PyCharm
import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])#typename：元组名称 field_names: 元组中元素的名称

class FrenchDeck:
    # 2-10, J, Q, K, A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 黑桃, 红桃, 梅花, 方块
    suits = 'spades diamonds clubs hearts'.split()


    # 初始化
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    # 获取元素个数
    def __len__(self):
        return len(self._cards)

    # 通过索引获取元素
    def __getitem__(self, position):
        return self._cards[position]

# spades > hearts > diamonds > clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
# print(deck[:3])
# print(deck[12::13])
for i in sorted(deck, key=spades_high):
    print(i)
