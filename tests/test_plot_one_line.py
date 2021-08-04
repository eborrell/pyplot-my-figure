from figures.myfigure import MyFigure

import numpy as np
from pathlib import Path
import os
import pytest

SOURCE_PATH = Path(os.path.dirname(__file__))
PROJECT_PATH = SOURCE_PATH.parent
DATA_PATH = os.path.join(PROJECT_PATH, 'data')

class TestPlotOneLine:
    '''
    '''

    #@pytest.mark.skip(reason='')
    def test_plot_one_line(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'one_line')

        # plot y = x ** 2
        x = np.arange(100)
        y = x**2
        fig.plot_one_line(x, y)

    def test_plot_one_line_legend(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'one_line_legend')

        # plot y = x ** 2
        x = np.arange(100)
        y = x**2
        fig.set_legend_location('lower right')
        fig.plot_one_line(x, y, label='$f(x) = x^2$')

    def test_plot_one_line_linestyle(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'one_line_linestyle')

        # plot y = x ** 2
        x = np.arange(100)
        y = x**2
        fig.plot_one_line(x, y, linestyle='--')

    def test_plot_one_line_scales(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        fig = MyFigure(dir_path, 'one_line_scales')

        # plot y = x ** 2
        x = np.arange(1, 100)
        y = x**2
        fig.set_plot_type('loglog')
        fig.plot_one_line(x, y)
