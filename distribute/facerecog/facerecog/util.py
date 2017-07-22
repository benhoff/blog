from os import path as _path


def get_haarcascade_filepath(type='face'):
    """
    Returns the filepath for the haarcascade xml file that comes bundled with
    this package
    """
    directory = _path.dirname(__file__)
    if type == 'face':
        haar_filepath = _path.join(directory,
                                   'haarcascade_frontalface_alt2.xml')
    else:
        haar_filepath = _path.join(directory,
                                   'haarcascade_eye_tree_eyeglasses.xml')
                                    

    return _path.abspath(haar_filepath)
