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
    import lets_plot as lp
    return lp, pl, px


@app.cell
def _(pl):
    dat = pl.DataFrame({
        'year':[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        'UT':[4000, 3760, 4211, 4000, 3760, 4211, 4000, 3760, 4211, 4000]
    })
    return (dat,)


@app.cell
def _(dat, lp):
    lp.ggplot(dat, lp.aes(x='year', y='UT')) + \
        lp.geom_line() + \
        lp.ggtb() + \
        lp.scale_x_continuous(format='4d') + \
        lp.ggsize(width=1000, height=500)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
