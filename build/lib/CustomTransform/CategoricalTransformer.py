from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder

class CategoricalTransformer(BaseEstimator, TransformerMixin):    
    # Class constructor method
    def __init__(self, features):
        self.features = features

    # Return self
    def fit(self, X, y = None):
        return self

    # Transfomer method
    def transform(self, X, y=None):

        lb_make = LabelEncoder()
        df_new = X.copy()

        for col in self.features:
            df_new[col] = lb_make.fit_transform(X[col])
        
        return X.values