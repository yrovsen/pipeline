from sklearn.base import BaseEstimator, TransformerMixin

class DateModification(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, data, y=None):
        return self

    def transform(self, data, y=None):
        return data