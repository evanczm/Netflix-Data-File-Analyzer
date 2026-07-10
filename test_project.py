import pandas
from project import clean_title, parseDuration, filterRealViews


def test_clean_title_weird_colons():
    # Unicode colon-like chars get replaced with standard colon
    assert clean_title("Show\u02D0 Title") == "Show: Title"
    assert clean_title("Show\uFF1A Title") == "Show: Title"


def test_clean_title_collapses_spaces():
    assert clean_title("Show    Title") == "Show Title"
    assert clean_title("Show \t  Title") == "Show Title"


def test_clean_title_strips_whitespace():
    assert clean_title("  Show Title  ") == "Show Title"
    assert clean_title("\nShow Title\n") == "Show Title"


def test_clean_title_removes_trailing_colon():
    assert clean_title("Show Title:") == "Show Title"
    assert clean_title("Show Title:  ") == "Show Title"


def test_clean_title_normal_title_unchanged():
    assert clean_title("Stranger Things") == "Stranger Things"
    assert clean_title("Breaking Bad") == "Breaking Bad"


def test_parseDuration_basic():
    assert parseDuration("1:10:49") == 4249
    assert parseDuration("0:41:08") == 2468
    assert parseDuration("2:00:00") == 7200


def test_parseDuration_zeros():
    assert parseDuration("0:00:00") == 0
    assert parseDuration("0:00:01") == 1
    assert parseDuration("0:01:00") == 60


def test_parseDuration_large():
    assert parseDuration("100:00:00") == 360000


def test_filterRealViews_removes_hooks_and_trailers():
    df = pandas.DataFrame({
        "Title": [
            "Stranger Things: S1: E1 (Episode 1)",
            "Breaking Bad Hook",
            "New Trailer Thing",
            "The Office: S3: E1 (Episode 1)",
        ],
        "Supplemental Video Type": [
            "",
            "HOOK",
            "TRAILER",
            "",
        ],
    })
    result = filterRealViews(df)
    assert len(result) == 2
    assert "Stranger Things" in result.iloc[0]["Title"]
    assert "The Office" in result.iloc[1]["Title"]


def test_filterRealViews_keeps_all_when_no_fakes():
    df = pandas.DataFrame({
        "Title": [
            "Inception",
            "The Dark Knight",
            "Interstellar",
        ],
        "Supplemental Video Type": [
            "",
            "",
            "",
        ],
    })
    result = filterRealViews(df)
    assert len(result) == 3


def test_filterRealViews_handles_missing_column():
    df = pandas.DataFrame({
        "Title": [
            "Inception",
            "The Dark Knight",
        ],
    })
    result = filterRealViews(df)
    assert len(result) == 2


def test_filterRealViews_exact_match():
    df = pandas.DataFrame({
        "Title": [
            "Good Show (Episode 1)",
            "HOOK thing",
            "TRAILER thing",
        ],
        "Supplemental Video Type": [
            "",
            "HOOK",
            "TRAILER",
        ],
    })
    result = filterRealViews(df)
    assert len(result) == 1
    assert "Good Show" in result.iloc[0]["Title"]
