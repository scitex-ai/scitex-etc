"""Smoke: render CLI happy paths (fast, subprocess, every PR)."""

import subprocess
import sys

import pytest

pytestmark = pytest.mark.smoke


def test_render_help_exits_zero():
    # Arrange
    cmd = [sys.executable, "-m", "scitex_etc.media.render", "--help"]
    # Act
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    # Assert
    assert proc.returncode == 0


def test_render_classify_help_exits_zero():
    # Arrange
    cmd = [sys.executable, "-m", "scitex_etc.media.render", "classify", "--help"]
    # Act
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    # Assert
    assert proc.returncode == 0
