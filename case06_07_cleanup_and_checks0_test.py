# case06_07_cleanup_and_checks_test.py
import os
from pathlib import Path
from tempfile import TemporaryDirectory


def generate_report(file: Path):
    file.write_text('content')


def test_generate_report():
    file = Path('report.txt')

    generate_report(file)

    assert file.exists()
    assert file.read_text() == 'content'
