from setuptools import setup, find_packages

setup(
    name="Algorithms_and_structures",
    version="1.0.5",
    packages=find_packages(),
    author="Sergey O",
    package_dir={'Algorithms_and_structures': 'Algorithms_and_structures'},
    include_package_data=True,
    package_data={
        'Algorithms_and_structures.Structures': ['*.py'],
        'Algorithms_and_structures.Algorithms': ['*.py'],
    },
    description="Data structures and algorithms implementations for learning purposes",
    long_description="This repository was created primarily for training in creating own libraries. Consider this as an experiment.",
    python_requires=">=3.6",
)
