from figures.myfigure import MyFigure

import numpy as np
from pathlib import Path
import os
import pytest

SOURCE_PATH = Path(os.path.dirname(__file__))
PROJECT_PATH = SOURCE_PATH.parent
DATA_PATH = os.path.join(PROJECT_PATH, 'data')

class TestPlotMultiplesLines:
    '''
    '''

    #@pytest.mark.skip(reason='')
    def test_plot_multiple_lines(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'multiple_lines')

        # plot
        x = np.arange(0, 10, 0.1)
        y = np.vstack((x ** 2, x ** 3))
        fig.plot_multiple_lines(x, y)

    def test_plot_multiple_lines_legend(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'multiple_lines_legend')

        # plot
        x = np.arange(0, 10, 0.1)
        y = np.vstack((x ** 2, x ** 3))
        labels = [
            '$f(x) = x^2$',
            '$f(x) = x^3$',
        ]
        fig.set_legend_location('upper right')
        fig.plot_multiple_lines(x, y, labels=labels)

    def test_plot_multiples_lines_scales(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'multiple_lines_scales')

        # plot y = x ** 2
        x = np.arange(0, 10, 0.1)
        y = np.vstack((x ** 2, x ** 3))
        fig.set_plot_type('loglog')
        fig.plot_multiple_lines(x, y)
