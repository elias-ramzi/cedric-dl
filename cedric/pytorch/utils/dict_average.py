from collections import defaultdict

from cedric_dl.pytorch.utils.average_meter import AverageMeter


class DictAverage(defaultdict):

    def __init__(self,):
        super().__init__(AverageMeter)

    def update(self, dict_values, n=1):
        for key, item in dict_values.items():
            self[key].update(item, n)

    @property
    def avg(self,):
        return {key: item.avg for key, item in self.items()}

    @property
    def sum(self,):
        return {key: item.sum for key, item in self.items()}
