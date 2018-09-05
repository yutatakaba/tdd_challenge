import unittest
from di_sample import MyMemory


class TestMyMemory(unittest.TestCase):
    def test_get_favorite(self):
        # 副作用（KVS）から「お気に入り：インコ」の入力があるときに、出力が正しくインコになる
        stub_data = {'favorite': 'インコ'}
        kvs_stub = MockedKVS(initial_data=stub_data)  # これがスタブ
        my_memory = MyMemory(kvs_stub)

        self.assertEqual(my_memory.get_favorite(), 'インコ')

    def test_set_favorite(self):
        # インコを set_favorite したときに、 KVS にそれが登録される
        kvs_spy = MockedKVS()  # これがスパイ
        my_memory = MyMemory(kvs_spy)

        my_memory.set_favorite('ボルダリング')
        self.assertEqual(kvs_spy.data, {'favorite': 'ボルダリング'})


class MockedKVS:
    '''
    SomeKVSUsingDynamoDB クラスと同じインターフェースを持つ偽物です。
    スタブとスパイを兼ねます。
    '''
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = {}
        self.data = initial_data

    def get(self, key):
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value
