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
        dir_path = os.path.join(get_data_dir(), 'plot')
        return dir_path

    @pytest.fixture
    def x(self):
        ''' returns one-dimensional array
        '''
        h = 0.1
        lb = -1
        rb = 1
        x = np.arange(lb, rb + h, h)
        return x

    @pytest.fixture
    def f(self, x):
        ''' returns one-dimensional array
        '''
        return x**2

    @pytest.fixture
    def g(self, x):
        ''' returns one-dimensional array
        '''
        return x**3

    #@pytest.mark.skip(reason='')
    def test_one_line(self, dir_path, x, f):
        ''' plot y = x**2
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line',
        )
        fig.plot(x, f)

    def test_one_line_labels_and_titles(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_labels_and_titles',
        )
        fig.set_title('test title')
        fig.set_xlabel('x')
        fig.plot(x, f, labels='test label')
        #fig.plot(x, f, labels=r'$f(x) = x^2$')

    def test_one_line_linestyle(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_linestyle',
        )
        fig.plot(x, f, linestyles='--')

    def test_one_line_legend(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_legend',
        )
        fig.set_legend_location('lower right')
        fig.plot(x, f, labels=r'$f(x) = x^2$')

    def test_one_line_linestyle(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_linestyle',
        )
        fig.plot(x, f, linestyles='--')

    def test_one_line_scales(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_scales',
        )
        fig.set_plot_scale('loglog')
        fig.plot(x, f)

    def test_one_line_ylim(self, dir_path, x, f):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='one_line_ylim',
        )
        fig.set_xlim(-0.5, 0.5)
        fig.plot(x, f)

    def test_multiple_lines(self, dir_path, x, f, g):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='multiple_lines',
        )
        y = np.vstack((f, g))
        fig.plot(x, y)

    def test_multiple_lines_legend(self, dir_path, x, f, g):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='multiple_lines_legend',
        )

        y = np.vstack((f, g))
        labels = [
            r'$f(x) = x^2$',
            r'$f(x) = x^3$',
        ]
        fig.set_legend_location('upper right')
        fig.plot(x, y, labels=labels)

    def test_multiples_lines_scales(self, dir_path, x, f, g):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='multiple_lines_scales',
        )
        y = np.vstack((f, g))
        fig.set_plot_scale('loglog')
        fig.plot(x, y)
