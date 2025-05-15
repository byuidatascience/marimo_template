# marimo Data Science Notebooks

## Installation

```bash
pip install "marimo[recommended]"
```

## Developing notebooks

In general, we recommend creating notebooks in the `reports` folder. Upload your data used within your notebooks into the `reports/public` folder.

## Including data or assets

To include data or assets in your notebooks, add them to the `public/` directory.

## Terminal and marimo

In your terminal run `marimo edit` or `marimimo edit [path_to_py_file]` and marimo will start running.

## VS code and marimo

[vscode marimo](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo) can be installed as an extension in VS Code. This extension includes an experimental feature to run marimo in VSCode's native notebook interface. This feature lets you use VSCode editors and extensions for writing code while the outputs and visualizations are rendered in a view-only marimo editor. This marimo editor displays outputs, console logs, and UI elements to interact with.

You can start the viewer (as edit) to use the app.

[](marimo_vscode_gui.png)

We recommend popping the in vs code browser into your computer's web browser. The marimo team recommends Chrome for the best use.

You can now work within the marimo space in your browser.  Saving your file will update the `.py` file in VS code.

## Docker and marimo

This repository also provides a `Dockerfile` and `docker-compose.yaml` file. Through these files you can run `docker compose up` to build your marimo environment and develop using [http://localhost:8080](http://localhost:8080). The `docker-compose.yaml` will sync any saves in your marimo environment to this repository.

## Github Pages `WebAssembly + GitHub Pages Template` and marimo

[WebAssembly](https://webassembly.org) is designed as a web client portable compilation of programming languages like Python and R. In our case Python just works in the static web page using the client's resources without the client needed a full local install of Python. Now marimo gives us access to this WebAssembly protocal through [WebAssembly Notebooks](https://docs.marimo.io/guides/wasm/).

WASM notebooks come with many packages pre-installed, including NumPy, SciPy, scikit-learn, pandas, and matplotlib; see [Pyodide's documentation](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) for a full list. If you attempt to import a package that is not installed, marimo will attempt to automatically install it for you. To manually install packages, use micropip. All packages with pure Python wheels on PyPI are supported, as well as additional packages like NumPy, SciPy, scikit-learn, duckdb, polars, and more. For a full list of supported packages, see [Pyodide's documentation on supported packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html).

As of April 2025, [Lets-Plot](https://lets-plot.org) is not part of Pyodide's supported packages and will not work with WebAssembly marimo notebooks.

### 🚀 Usage

1. Fork this repository
2. Add your marimo files to the `notebooks/` or `apps/` directory
   1. `notebooks/` notebooks are exported with `--mode edit`
   2. `reports/` notebooks are exported with `--mode run`
3. Push to main branch
4. Go to repository **Settings > Pages** and change the "Source" dropdown to "GitHub Actions"
5. GitHub Actions will automatically build and deploy to Pages


### 🧪 Local Environment Testing using `build.py`

To test the export process, run `scripts/build.py` from the root directory.

```bash
python scripts/build.py
```

This will export all notebooks in a folder called `_site/` in the root directory. Then to serve the site, run:

```bash
python -m http.server -d _site
```

This will serve the site at `http://localhost:8000`.
