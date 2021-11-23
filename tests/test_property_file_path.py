from figures.myfigure import MyFigure
from figures.utils import get_data_dir

import matplotlib.pyplot as plt
import os
import pytest

class TestPropertyFilePath:
    '''
    '''

    #@pytest.mark.skip(reason='')
    def test_property_file_path(self):

        # initialize custom figure
        dir_path = os.path.join(get_data_dir(), 'foo')
        file_name = 'figure_1'
        file_type = 'png'
        fig = plt.figure(
            FigureClass=MyFigure,
            dir_path=dir_path,
            file_name=file_name,
            file_type=file_type,
        )

        assert fig.file_path is not None
        assert fig.file_path == os.path.join(dir_path, file_name + '.' + file_type)

        # change file name and file type
        file_path = fig.file_path
        new_file_name = 'figure_2'
        fig.file_name = new_file_name
        new_file_path = fig.file_path
        assert new_file_path is not None
        assert new_file_path == os.path.join(dir_path, new_file_name + '.' + file_type)
        assert file_path != new_file_path
