from figures.myfigure import MyFigure
from figures.utils import get_data_dir

import matplotlib.pyplot as plt
import numpy as np
import os
import pytest

class TestPlot:
    '''
    '''
    @pytest.fixture
    def dir_path(self):
        ''' returns dir path for the test plots
        '''
        dir_path = os.path.join(get_data_dir(), 'pyplot')
        return dir_path

    #@pytest.mark.skip(reason='')
    def test_scatter(self, dir_path):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='scatter',
        )
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N)) ** 2

        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.savefig(fig.file_path)
