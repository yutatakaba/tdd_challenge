class Sample:
    def calc_speed(self, distance, elapsed_time):
        '''
        移動距離とかかった時間から平均の速さを計算します。

        :param float distance: 移動距離（単位: km）
        :param float elapsed_time: 時間（単位: h）
        :rtype: float
        :return: 速度（単位: km/h）
        '''
        if distance < 0 or elapsed_time <= 0:
            raise ValueError()
        return distance / elapsed_time
