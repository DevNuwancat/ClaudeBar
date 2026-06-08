from setuptools import setup

APP = ['app.py']

DATA_FILES = [
    ('assets', ['assets/claudecapicon.png', 'assets/icon.icns'])
]

OPTIONS = {
    'argv_emulation': False,
    'packages': [
        'curl_cffi',
        'rumps',
        'keyring',
    ],
    'iconfile': 'assets/icon.icns',
    'plist': {
        'CFBundleName':               'ClaudeCap',
        'CFBundleDisplayName':        'Claude Cap',
        'CFBundleIdentifier':         'com.nuwancat.claudecap',
        'CFBundleVersion':            '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement':                True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)