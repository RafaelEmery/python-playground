# Playground

## Run locally

Configure Python using `asdf` based on `.tool-versions` file:

```
asdf plugin-add python

asdf install

asdf set python 3.12.2
```

Or you can use `pyenv` based on `.python-version` file:

```
TODO: set pyenv config here
```

## Projects

#### `daily_python_projects`

Based on "Daily Python Projects" newsletter from Substack: [https://dailypythonprojects.substack.com/](https://dailypythonprojects.substack.com/)

Run using `Makefile` command at root:

```
make list-daily-python-projects

make daily-python-project file=file_name.py
```