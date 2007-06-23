from distutils.core import setup
import sys

kwargs = {
    'name': 'ShotFactory',
    'version': '0.4-alpha1',
    'description': 'Screenshot factory for browsershots.org',
    'author': 'Johann C. Rocholl',
    'author_email': 'johann@browsershots.org',
    'url': 'http://v04.browsershots.org/',
    'packages': [
        'shotfactory04',
        'shotfactory04.gui',
        'shotfactory04.gui.darwin',
        'shotfactory04.gui.linux',
        'shotfactory04.gui.windows',
        'shotfactory04.image',
        ],
    'scripts': [
        'shotfactory.py',
        'browsershot.py',
        'ppmoffset.py',
        ],
    }

if 'py2exe' in sys.argv:
    import py2exe
    # modulefinder can't handle runtime changes to __path__,
    # but win32com uses them
    import modulefinder
    import win32com
    for path in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", path)
    __import__("win32com.shell")
    m = sys.modules["win32com.shell"]
    for path in m.__path__[1:]:
        modulefinder.AddPackagePath("win32com.shell", path)
    # py2exe configuration
    kwargs['console'] = [{
        'script': 'shotfactory.py',
        'icon_resources': [(1, 'favicon.ico')],
        }]
    kwargs['options'] = {
        'py2exe': {
            'includes': ','.join([
                'shotfactory04.gui.windows.msie',
                'shotfactory04.gui.windows.firefox',
                'shotfactory04.gui.windows.safari',
                ]),
            'dist_dir': 'bin',
            }
        }

setup(**kwargs)
