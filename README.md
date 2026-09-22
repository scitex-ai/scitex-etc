# scitex-etc

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Interactive keyboard input utilities for the SciTeX ecosystem.</b></p>

<p align="center">
  <a href="https://scitex-etc.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-etc[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-etc/"><img src="https://img.shields.io/pypi/v/scitex-etc?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-etc/"><img src="https://img.shields.io/pypi/pyversions/scitex-etc?label=python" alt="python"></a>
  <a href="https://scitex-etc.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-etc?label=docs" alt="docs"></a>
</p>
<p align="center">
  <a href="https://github.com/ywatanabe1989/scitex-etc/actions/workflows/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-etc/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-etc/actions/workflows/import-smoke-on-ubuntu-py3-12.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-etc/import-smoke-on-ubuntu-py3-12.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-etc"><img src="https://img.shields.io/codecov/c/github/ywatanabe1989/scitex-etc/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Keypress pause** — raw stdin needs OS boilerplate. | **One import** — wait_key handles Linux macOS Windows. |

## Quick Start

```python
import multiprocessing
from scitex_etc import wait_key, count

# count() prints an incrementing counter forever (1 per second).
# Run it in a subprocess and use wait_key() to stop on 'q'.
p = multiprocessing.Process(target=count)
p.start()
wait_key(p)
```

## Demo

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 20, 'rankSpacing': 40, 'curve': 'linear'}, 'themeVariables': {'fontSize': '12px'}}}%%
flowchart LR
    User[User keypress] --> TTY{stdin is TTY?}
    TTY -- yes --> Termios[termios raw mode]
    TTY -- no --> Fallback[readline fallback]
    Termios --> Key[key string]
    Fallback --> Key
```

<p align="center"><sub><b>Figure 1.</b> Keypress handling from stdin check to key string.</sub></p>

## Installation

```bash
uv pip install "scitex-etc[all]"
```

<details>
<summary><b>Per-module extras</b></summary>

<br>

| Extra | Pulls in |
|---|---|
| `dev` | pytest, pytest-cov, ruff, scitex-dev |
| `docs` | Sphinx plus theme and myst-parser |
| `all` | dev plus docs (recommended) |

```bash
uv pip install "scitex-etc[dev]"  # contributors
uv pip install -e ".[dev]"         # editable install
```

</details>

## Architecture

### 1. Input handling

`wait_key` abstracts raw-stdin keypress handling across Linux, macOS, and Windows with TTY fallback.

### 2. Media rendering

`media.render` classifies, detects, and shows media files for terminal, chat, and markdown targets.

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 20, 'rankSpacing': 40, 'curve': 'linear'}, 'themeVariables': {'fontSize': '12px'}}}%%
flowchart LR
    INPUT[wait_key and count] --> CORE[core helpers]
    MEDIA[media render] --> CLASSIFY[classify and detect]
    CORE --> OUT[interactive utilities]
    CLASSIFY --> OUT
```

<p align="center"><sub><b>Figure 2.</b> Module collaboration from input and media to utilities.</sub></p>

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
import multiprocessing
from scitex_etc import wait_key, count

# Run the counter in a subprocess, wait for 'q' to stop it.
p = multiprocessing.Process(target=count)
p.start()
wait_key(p)  # Blocks until 'q' is pressed, then terminates the process
```

</details>

<details>
<summary><strong>Media handling (<code>scitex_etc.media.render</code>)</strong></summary>

<br>

```python
from scitex_etc.media import render

# Classify a file by its extension
render.classify("fig.png")          # {"type": "image", "path": "fig.png", "ext": ".png"}

# Detect media refs in tool output
render.detect("Saved /proj/fig.png", root_path="/proj")
# [{"type": "image", "path": "fig.png", "ext": ".png"}]

# Render to a target: terminal (OSC overlay), chat, or markdown
render.show("fig.png", target="markdown")  # "![fig.png](fig.png)"
```

Also available as a CLI (`python -m scitex_etc.media.render show|classify|detect`)
and as MCP tools (`scitex_etc.media.render.mcp_server`).

</details>

## Part of SciTeX

`scitex-etc` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[etc]` to use as
`scitex.etc` (Python) or `scitex etc ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
