# case10_prod_data_test.py
from pathlib import Path
from tempfile import TemporaryDirectory

DATA_LOCATION = '/var/tmp'


def generate_report(file: Path):
    file.write_text('content')


def test_generate_report():
    file = Path(DATA_LOCATION, 'report.txt')

    generate_report(file)  # DANGER! Overwrite file in data directory

    assert file.exists()
    file.unlink()  # DANGER! Delete from data directory


def test_generate_report_with_temp_location():
    with TemporaryDirectory() as tmp_dir:
        file = Path(tmp_dir, 'report.txt')

        generate_report(file)

        assert file.exists()
        assert file.read_text() == 'content'
