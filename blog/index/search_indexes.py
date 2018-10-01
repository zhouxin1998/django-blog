# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from haystack import indexes
from .models import BowenInfo


class BowenInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self):
        return BowenInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

