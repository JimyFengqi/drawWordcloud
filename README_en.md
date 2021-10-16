
# WordCloud Generator
English | [简体中文](./README_cn.md)

## 简介

> This is a wordcloud generator,which has a UI
>
> it's easy to use: just select a file and a picture, then a wordcloud will be genrate.
>
> Image viewer: you can select a image directory to view pictures

## Environment：
- Python 3.8
- jieba 0.42.1
- wordcloud 1.8.0
- numpy1.19
- pillow 8.1
- wxPython 4.0
- numpy 1.19.0

## Setup
1. Download the porject

```bash
git clone https://github.com/JimyFengqi
cd my-project
```
or
```bash
git clone https://gitee.com/jimmyfengqi
cd my-project
```
2. Install dependencies
```bash
source install.sh
```
Or install by PIP
```bash
pip install -r requirements.txt
```
3.Quick Start
```sh
python src/daw_gui
```
or（if you install dependencies by poetry）
```
test-package
```
## Project Config
### Use peotry
#### Project Entry
Notice the format for this config

"test-package" is the name for start project(named by you)

```
[tool.poetry.scripts]
  test-package = "src.test:GUI"
```
#### Add Source
In order to install dependencies smoothly, add the source mirror.
```
[[tool.poetry.source]]
    name = "tsinghua"
    url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
    default = true
```
### Linting and formatting

The code structure needs follow [Flake8](https://pypi.org/project/flake8/) and [Black](https://pypi.org/project/black/) and is enforced via a pre commit hook.


To keep the imports clean and consistent we use [isort](https://pypi.org/project/isort/) which is also enforced using a pre-commit hook.

#### Black

[Black](https://pypi.org/project/black/) is a (very popular) code formatter with very little configuration.

It will transform your code stylewise such that it follows the official [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).

 You may not necessarily agree with all of the choices made by black,

 but in return it makes everyone's code consistent and allows you to focus on coding rather than the number of spaces between your functions.

 Black can be configured using [pyproject.toml](./pyproject.toml).

Max line length is configured to 120 characters.
```
[tool.black]
    line-length = 120
```
####Flake8

[Flake8](https://pypi.org/project/flake8/) is a linter which essentially wraps an error checker ([Pyflakes](https://pypi.org/project/pyflakes/)),

 a PEP 8 style checker ([Pycodestyle](https://pypi.org/project/pycodestyle/)) and a code complexity checker([Mccabe](https://pypi.org/project/mccabe/)).

 If used by your editor, you will get instant warnings about issues in your code.

 Flake8 can be configured using [.flake8](./.flake8).

#### Isort

[Isort](https://pypi.org/project/isort/) groups imports by type and then sorts them alphabetically.

By default it disagrees slightly with Black, but that can be configured in [pyproject.toml](./pyproject.toml).

#### pre-commit
In order to check the style and format for the code,

we install the tool [pre-commit](https://pypi.org/project/pre-commit)

with the config file [.pre-commit-config.yaml] to do the code check

if you want to skip these hooks check, then you can run
```
git commit --no-verify
git push --no-verify
```
