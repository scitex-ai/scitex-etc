"""Runtime cross-package import gate.

This test imports every cross-package module that 'scitex-etc' references
in its source tree. Two outcomes:

- Module installed AND import succeeds → test PASSES.
- Module installed BUT import fails (e.g. an internal rename) →
  test FAILS loudly.
- Module NOT installed (peer standalone absent in the CI env) →
  test is SKIPPED via `pytest.importorskip`. The umbrella's CI
  (which installs every peer) catches cross-package renames.

scitex-etc references ``scitex_dev`` only from
``scitex_etc.media.render.mcp_server`` (a ``[dev]`` extra used to locate the
optional ``fastmcp`` dependency); the import is guarded, so a minimal runtime
install without scitex_dev still imports the module cleanly.
``scitex_logging`` is a runtime dependency, used for all stdout/stderr output.
"""

import importlib

import pytest

# ===== AUTO-GENERATED: cross-package imports =====
CROSS_PACKAGE_IMPORTS = [
    "scitex_dev",
    "scitex_logging",
]
# ===== END AUTO-GENERATED =====


@pytest.mark.parametrize("module_name", CROSS_PACKAGE_IMPORTS)
def test_cross_package_import(module_name):
    """Importing scitex-etc's declared cross-package dependency must succeed."""
    # Arrange: skip only when the peer's ROOT package is absent
    pytest.importorskip(module_name.split(".")[0])
    # Act: hard-import the FULL path so a renamed submodule fails loudly
    module = importlib.import_module(module_name)
    # Assert
    assert getattr(module, "__name__", None) == module_name
