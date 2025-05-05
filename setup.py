from setuptools import setup, find_packages

setup(
    name="nikto-html-wrapper",
    version="0.1.0",
    description="Wrapper for Nikto that outputs HTML reports",
    author="Your Name",
    packages=find_packages(),
    install_requires=["jinja2"],
    entry_points={
        "console_scripts": [
            "nikto-html-wrapper=nikto_html_wrapper.cli:main",
        ],
    },
)
