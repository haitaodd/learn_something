import numpy as np


class SimpleLinearRegression1:
    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0

        for x_i, y_i in zip(x_train, y_train):
            num += (x_i - x_mean) * (y_i - y_mean)
            d += np.square(x_i - x_mean)

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self, x_predict):
        assert x_predict.ndim == 1, \
            "Only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "Must fit before predict."
        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return 'SimpleLinearRegression1(a = {}, b={})'.format(self.a_, self.b_)

# 使用向量化计算
class SimpleLinearRegression2:
    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0


        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train-x_mean).dot(x_train-x_mean)

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self, x_predict):
        assert x_predict.ndim == 1, \
            "Only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "Must fit before predict."
        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return 'SimpleLinearRegression2(a = {}, b={})'.format(self.a_, self.b_)