import json
from pathlib import Path

def _load():
    return json.loads(REPORT.read_text())

def test_report_exists():
    """Criterion 1: a report.json is written to /app."""
    assert REPORT.exists(), "no report.json found"


def test_total_requests():
    """Criterion 2: total_requests == 6 (non-empty log lines)."""
    assert _load()["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips == 3 (distinct client IPs)."""
    assert _load()["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path == /index.html (most-requested path)."""
    assert _load()["top_path"] == "/index.html"