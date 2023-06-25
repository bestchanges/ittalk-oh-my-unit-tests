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
    file.unlink()


def test_generate_report_with_cleanup_and_checks():
    with TemporaryDirectory() as tmp_dir:
        file = Path(tmp_dir, 'report.txt')
        assert not file.exists()  # pre-check

        generate_report(file)

        assert file.exists()
        assert file.read_text() == 'content'

    assert not file.exists()  # post-check
