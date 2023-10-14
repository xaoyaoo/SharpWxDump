from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "2.0.1"
setup(
    name="pywxdump",
    author="xaoyaoo",
    version=version,
    author_email="xaoyaoo@gmail.com",
    description="微信信息获取工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xaoyaoo/PyWxDump",
    license='MIT',

    packages=find_packages(),
    package_data={
        'app': ['version_list.json'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <4',
    install_requires=[
        "psutil",
        "pycryptodomex",
        "pywin32",
        "pymem",
    ],
    entry_points={
        'console_scripts': [
            'wxdump = app.command:console_run',
        ],
    },
)