import pytest

from psrpoppysuper import dosurvey, evolve, populate


def test_populate_wS_requires_surveys():
    with pytest.raises(ValueError):
        populate._validate_output_targets(
            write_global=None,
            write_surveyed='surveyed.txt',
            survey_list=None,
        )


def test_evolve_wG_allows_no_surveys():
    populate._validate_output_targets(
        write_global='global.txt',
        write_surveyed=None,
        survey_list=None,
    )


def test_dosurvey_rejects_wG():
    with pytest.raises(ValueError):
        dosurvey._validate_output_targets(
            write_global='global.txt',
            write_surveyed=None,
        )
