from figures.myfigure import MyFigure
from figures.utils import get_data_dir
import matplotlib.pyplot as plt

import numpy as np
import os
import pytest

class TestContour:
    '''
    '''
    @pytest.fixture
    def dir_path(self):
        ''' returns dir path for the test plots
        '''
        dir_path = os.path.join(get_data_dir(), 'contour')
        return dir_path

    @pytest.fixture
    def mesh(self):
        ''' returns tuple (X, Y)
        '''
        h = 0.1
        lb = -10
        rb = 10
        x = y = np.arange(lb, rb + h, h)
        return np.meshgrid(x, y, indexing='ij')

    @pytest.fixture
    def f(self, mesh):
        ''' returns function f(x, y) = 2x evaluated at the grid
        '''
        X, Y = mesh
        return 2 * X

    @pytest.fixture
    def g(self, mesh):
        ''' returns function g(x, y) = x y evaluated at the grid
        '''
        X, Y = mesh
        return X * Y

    #@pytest.mark.skip(reason='')
    def test_contour(self, dir_path, mesh, f):
        ''' plot contour of f(x, y)
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='contour',
        )
        X, Y = mesh
        fig.contour(X, Y, f)

    def test_contour_colormap(self, dir_path, mesh, f):
        ''' plot contour of f(x, y). Set colormap.
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='contour_colormap',
        )
        X, Y = mesh
        #fig.set_colormap('BuPu_r', start=0.15, stop=1.)
        fig.set_colormap('Blues_r', start=0., stop=1.)
        fig.contour(X, Y, f)

    def test_contour_limits(self, dir_path, mesh, f):
        ''' plot contour of f(x, y). Set domain limits.
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='contour_limits',
        )
        X, Y = mesh
        fig.set_xlim(0, 0.5)
        fig.set_ylim(0, 0.5)
        fig.contour(X, Y, f)

    def test_contour_levels(self, dir_path, mesh, g):
        ''' plot contour of g(x, y). Set log levels.
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='contour_levels',
        )
        X, Y = mesh
        fig.set_contour_levels_scale('log')
        fig.contour(X, Y, g)
