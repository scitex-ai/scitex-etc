"""Enforces SciTeX skills quality checklist §1–§4."""

# PS-206b: import-smoke-allowed — generated skill-quality wrapper, assertions live in scitex-dev.

from pathlib import Path

import pytest

# scitex-dev is a [dev] extra, not a runtime dependency — guard per PA-303
# so the test cleanly skips when running in a minimal install.
scitex_dev_skills_quality_pytest = pytest.importorskip(
    "scitex_dev._skills_quality_pytest"
)
make_skill_quality_tests = scitex_dev_skills_quality_pytest.make_skill_quality_tests

test_skills_quality = make_skill_quality_tests(
    package_root=Path(__file__).resolve().parents[2]
)
