"""E2E: render classify/detect against real subsystem (no network)."""

import pytest

pytestmark = pytest.mark.e2e


def test_classify_png_returns_image_type():
    # Arrange
    from scitex_etc.media import render
    # Act
    ref = render.classify("fig.png")
    # Assert
    assert ref["type"] == "image"


def test_detect_finds_png_under_root():
    # Arrange
    from scitex_etc.media import render
    # Act
    refs = render.detect("Saved /proj/fig.png", root_path="/proj")
    # Assert
    assert len(refs) == 1
