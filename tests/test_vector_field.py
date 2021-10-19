from figures.myfigure import MyFigure
from figures.utils import get_data_dir
import matplotlib.pyplot as plt

import numpy as np
import os
import pytest

class TestVectorField:
    '''
    '''
    @pytest.fixture
    def dir_path(self):
        ''' returns dir path for the test plots
        '''
        dir_path = os.path.join(get_data_dir(), 'vector_field')
        return dir_path

    @pytest.fixture
    # https://matplotlib.org/stable/gallery/images_contours_and_fields/
    # quiver_simple_demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-simple-demo-py
    def setting_1(self):
        ''' returns tuple (X, Y)
        '''
        x = y = np.arange(0, 2 * np.pi, .2)
        X, Y = np.meshgrid(x, y, indexing='ij')
        U = np.cos(X)
        V = np.sin(Y)
        return X, Y, U, V

    #@pytest.mark.skip(reason='')
    def test_quiver(self, dir_path, setting_1):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='quiver',
        )
        X, Y, U, V = setting_1
        fig.vector_field(X, Y, U, V)

    def test_quiver_limits(self, dir_path, setting_1):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='quiver_limits',
        )
        X, Y, U, V = setting_1
        fig.set_xlim(0, 3)
        fig.set_ylim(0, 3)
        fig.vector_field(X, Y, U, V)

    def test_quiver_scale(self, dir_path, setting_1):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='quiver_scale',
        )
        X, Y, U, V = setting_1

        # a smaller scale parameter makes the arrow longer
        fig.vector_field(X, Y, U, V, scale=10)

    def test_quiver_width(self, dir_path, setting_1):
        '''
        '''
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name='quiver_width',
        )
        X, Y, U, V = setting_1

        # a smaller scale parameter makes the arrow longer
        fig.vector_field(X, Y, U, V, width=0.01)
