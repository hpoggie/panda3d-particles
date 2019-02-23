import setuptools


setuptools.setup(
    name="panda3d-particles",
    use_scm_version=True,
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama==0.4.1',
        'panda3d==1.10.1',
    ],
    setup_requires=[
        'setuptools_scm'
    ],
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
