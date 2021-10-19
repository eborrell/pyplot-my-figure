from pathlib import Path

import os

def get_project_dir():
    ''' returns the absolute path of the repository's directory
    '''
    return Path(__file__).parent.parent.parent

def get_data_dir():
    ''' returns the absolute path of the repository's data directory
    '''
    project_path = get_project_dir()
    return os.path.join(project_path, 'data')
