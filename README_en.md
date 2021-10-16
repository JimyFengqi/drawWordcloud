
# WordCloud Generator
English | [简体中文](./README_cn.md)

## 简介

> Python 实现的、带界面的词云生成器。
>
> 选择文档（中文、英文均可)和背景图片即可生成词云

```bash
source install.sh
```

## Testing

Tests are executed with the testrunner [Pytest](https://docs.pytest.org/en/stable/).

To run the tests, execute the following in the root of the git repository:

```bash
pytest --verbose --cov=fyc_event_transformer --cov-branch --cov-report term-missing
```

Using the flag `--verbose` will give you more detailed test result in the terminal, for example which test function/class has been executed and with which input data.

Using the flag `--cov` will give you coverage of a certain folder when running the tests.

Using the flag `--cov-branch` will include more information in the coverage report, it can be used to view more detailed
coverage information.

Using the flag `--cov-report term-missing` will include information of which code branches have not been covered.

## Sphinx documentation

We are using [Sphinx](https://www.sphinx-doc.org/en/master/) to generate code level documentation in the [ReadTheDocs theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/).
Sphinx expects docstrings in the [reStructuredText format](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) but we are able to use our more readable google-style docstrings using the [napoleon extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html). The documentation is located in the [docs](./docs) folder.

To generate the documentation:

```
cd docs
bash generate_docs.sh
```

If everything went well, the documentation is now available at [docs/\_build/html/index.html](./docs/_build/html/index.html).
