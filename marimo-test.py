import marimo

__generated_with = "0.14.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame

    return Series, np


@app.cell
def _(mo):
    mo.md(
        r"""
    # The story so far

    I have been using Jupyter notebooks for many years. But in the last month or two, I've started to use Marimo instead. And I have to say, I love it!
    """
    )
    return


@app.cell
def _(Series, mo, np):
    np.random.seed(0)
    s = Series(np.random.randint(0, 100, 10),
              index=list('abcdefghij'))
    threshold = mo.ui.slider(0, 100, show_value=True)
    threshold
    return s, threshold


@app.cell
def _(mo):
    name = mo.ui.text('Enter your name: ')
    name
    return (name,)


@app.cell
def _(mo):
    color = mo.ui.radio(options={'red':'red',
                               'blue':'blue',
                               'green':'green',
                               'black':'black'},
                       label='Pick a color',
                       value='green')
    color
    return (color,)


@app.cell
def _(color, name, s, threshold):

    (
        s
        .loc[lambda s_: s_ > threshold.value]
        .plot.line(title=f'Plot for {name.value}',
        color=color.value)
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
