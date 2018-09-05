class MyMemory:
    '''
    Dependency Injection のサンプルです。

    私の情報を覚えていてくれるかわいいクラス。
    記憶は AWS の DynamoDB とかの KVS (Key Value Store) に保存されるらしいよ。
    '''
    def __init__(self, kvs):
        '''
        コンストラクタです。

        :param kvs: KVS を操作するためのクラスです。
            kvs は get(key) と set(key, value) を実装している必要があります。
        '''
        # このクラスは kvs に dependency がある
        self._kvs = kvs

    def get_favorite(self):
        '''
        お気に入りを返します。

        :rtype: str
        :return: おきいに入りの名前
        '''
        return self._kvs.get('favorite')

    def set_favorite(self, favorite):
        '''
        お気に入りを設定します。

        :param str favorite: お気に入りの名前
        '''
        self._kvs.set('favorite', favorite)


class SomeKVSUsingDynamoDB:
    def get(self, key):
        # 本当は DynamoDB 叩いて値を取ってくる
        pass

    def set(self, key, value):
        # 本当は DynamoDB 叩いて値を設定する
        pass


if __name__ == '__main__':
    # 本番はこんな感じで使うことを想定
    kvs = SomeKVSUsingDynamoDB()
    my_memory = MyMemory(kvs)
    my_memory.set_favorite('ボルダリング')
    print(my_memory.get_favorite())
