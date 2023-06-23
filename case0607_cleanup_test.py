# case5_cleanup_test.py
import os
from pathlib import Path
from tempfile import TemporaryDirectory


def generate_report(file: Path):
    file.write_text('content')


def test_report_generator():
    file = Path('report.txt')

    generate_report(file)

    assert file.exists()
    # report.unlink()


def test_report_generator_with_cleanup():
    with TemporaryDirectory() as tmp_dir:
        file = Path(tmp_dir, 'report.txt')
        assert not file.exists()  # pre-check

        generate_report(file)

        assert file.exists()
    assert not file.exists()  # post-check
