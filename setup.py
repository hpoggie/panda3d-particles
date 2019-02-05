import setuptools
import git

r = git.Repo('.')

setuptools.setup(
    name="particle-editor",
    version=str(r.tags[-1]),  # Most recent tag as version
    packages=setuptools.find_packages(),
    include_package_data=True,
    options={
        'build_apps': {
            'exclude_modules': [
                'GitPython'
            ],
            'include_patterns': [
                '**/*.egg',
                '**/*.png',
                '**/*.ttf',
                '**/*.bam',
                '**/*.glsl',
                'CREDITS.txt'
            ],
            'plugins': [
                'pandagl',
            ],
            'gui_apps': {
                'Particle Editor': 'particle_editor/__main__.py',
            },
            'platforms': [
                'manylinux1_x86_64',
                # 'macosx_10_6_x86_64',
                # 'win32',
                'win_amd64',
            ],
        }
    },
    entry_points={
        'gui_apps': [
            'particle_editor=particle_editor.__main__:main'
        ],
    },
)
