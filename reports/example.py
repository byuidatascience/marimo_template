import marimo

__generated_with = "0.12.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    return pl, px


@app.cell
def _():
    import lets_plot
    import importlib

    # Get the __all__ list from lets_plot
    all_symbols = lets_plot.__all__

    # Import each symbol into the current namespace
    for symbol in all_symbols:
        globals()[symbol] = getattr(lets_plot, symbol)
    return all_symbols, importlib, lets_plot, symbol


@app.cell
def _(pl):
    df = pl.DataFrame(
        {
            "A": ["a", "b", "a"],
            "B": [1, 3, 5],
            "C": [10, 11, 12],
            "D": [2, 4, 6],
        }
    )
    df
    return (df,)


@app.cell
def _(aes, df, geom_line, geom_point, ggplot, ggsize, ggtb):
    ggplot(df, aes(x="B", y="C")) + geom_point() + \
        geom_line() + \
        ggtb() + \
        ggsize(width=1000, height=500)
    return


if __name__ == "__main__":
    app.run()
