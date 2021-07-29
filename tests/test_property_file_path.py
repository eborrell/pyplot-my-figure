from figures.myfigure import MyFigure

import os
from pathlib import Path
import pytest

SOURCE_PATH = Path(os.path.dirname(__file__))
PROJECT_PATH = SOURCE_PATH.parent
DATA_PATH = os.path.join(PROJECT_PATH, 'data')

class TestPropertyFilePath:
    '''
    '''

    #@pytest.mark.skip(reason='')
    def test_property_file_path(self):

        # initialize custom figure
        dir_path = os.path.join(DATA_PATH, 'tests')
        file_name = 'figure_1'
        file_type = 'png'
        fig = MyFigure(dir_path, file_name, file_type)
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
