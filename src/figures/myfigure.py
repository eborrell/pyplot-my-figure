import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import os

class MyFigure(Figure):
    ''' Figure with one axes.
    '''

    def __init__(self, dir_path, file_name='foo', file_type='png', *args, **kwargs):
        super().__init__(*args, **kwargs)

        # file path attributes
        self.file_name = file_name
        self.file_type = file_type
        self.dir_path = dir_path

        # add set of subplots
        _ = self.subplots()

    @property
    def file_path(self):
        return os.path.join(self.dir_path, self.file_name + '.' + self.file_type)
