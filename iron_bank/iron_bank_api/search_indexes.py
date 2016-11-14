import datetime
from haystack import indexes
from iron_bank_api.models import Transaction


class TransactionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Transaction
    
