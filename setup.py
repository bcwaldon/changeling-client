import setuptools
import changeling_client.metadata


def parse_requirements():
    return open('requirements.txt').readlines()


setuptools.setup(
    name='changeling-client',
    version=changeling_client.metadata.VERSION,
    packages=['changeling_client'],
    install_requires=parse_requirements(),
    entry_points={
        'console_scripts': [
            'changeling = changeling_client.core:main',
        ],
    },
)
