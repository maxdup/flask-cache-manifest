from setuptools import setup


setup(
    name="Flask-Cache-Manifest",
    version="0.1.0",
    author="Maxime Dupuis",
    author_email="mdupuis@hotmail.ca",
    url="https://github.com/maxdup/flask-cache-manifest",
    description="Flask extension to serve md5 hashed assets.",
    license="MIT",
    package_data={"Flask-Static-Digest": ["VERSION"]},
    packages=["flask_cache_manifest"],
    platforms="any",
    python_requires=">=3.6",
    install_requires=[
        "Flask>=2.0"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Compression"
    ]
)
