from pathlib import Path

from setuptools import find_packages, setup

ROOT_PROJ_DIR = Path(__file__).parent.parent

setup(
    name="networky",
    version="0.1.0a1",
    url="https://github.com/bustawin/fetcher",
    project_urls={
        "Documentation": "https://github.com/bustawin/fetcher",
        "Code": "https://github.com/bustawin/fetcher",
        "Issue tracker": "https://github.com/bustawin/fetcher/issues",
    },
    license="Affero",
    author="Xavier Bustamante Talavera",
    author_email="xavier@bustawin.com",
    description="Executes speedtest-cli and saves it in a SQL db.",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7.3",
    long_description=(ROOT_PROJ_DIR / "README.rst").read_text("utf8"),
    install_requires=[
        "speedtest-cli",
        "sqlalchemy",
        "typer",
    ],
    extras_require={"postgres": ["psycopg2-binary"]},
    entry_points={"console_scripts": ["networky = networky:app"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
)
