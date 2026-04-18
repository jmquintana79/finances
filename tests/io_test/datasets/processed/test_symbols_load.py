# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-04-18 22:51:50
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-18 23:23:58

from unittest.mock import patch

import pandas as pd
import pytest

# ── fixtures ──────────────────────────────────────────────

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "symbol": ["AAPL", "GOOG", "^GSPC"],
        "price":  [100,    200,    300   ]
    })


# ── tests originales ──────────────────────────────────────

def test_load_returns_sorted_deduped_df(sample_df):
    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv", "f2.csv"]), \
         patch("pandas.read_csv", return_value=sample_df) as mock_csv:

        from finances.io.datasets.processed.symbols import load

        result = load()

        assert result["symbol"].is_monotonic_increasing
        assert result["symbol"].duplicated().sum() == 0
        assert mock_csv.call_count == 2


def test_load_raises_if_folder_empty():
    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=[]):

        from finances.io.datasets.processed.symbols import load

        with pytest.raises(ValueError, match="No files found"):
            load()


def test_load_raises_if_all_files_are_empty():
    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv"]), \
         patch("pandas.read_csv", return_value=pd.DataFrame()):

        from finances.io.datasets.processed.symbols import load

        with pytest.raises(ValueError, match="empty"):
            load()


# ── tests nueva funcionalidad: with_only_favorites ────────

def test_load_with_favorites_filters_correctly(sample_df):
    """Solo devuelve los símbolos que están en la lista favorites."""
    fake_favorites = ["AAPL", "^GSPC"]

    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv"]), \
         patch("pandas.read_csv", return_value=sample_df), \
         patch("finances.configs.symbols.favorites", fake_favorites):

        from finances.io.datasets.processed.symbols import load

        result = load(with_only_favorites=True)

        assert set(result["symbol"]) == {"AAPL", "^GSPC"}
        assert "GOOG" not in result["symbol"].values


def test_load_with_favorites_resets_index(sample_df):
    """El índice del resultado debe ser 0-based y continuo."""
    fake_favorites = ["AAPL", "^GSPC"]

    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv"]), \
         patch("pandas.read_csv", return_value=sample_df), \
         patch("finances.configs.symbols.favorites", fake_favorites):

        from finances.io.datasets.processed.symbols import load

        result = load(with_only_favorites=True)

        assert list(result.index) == list(range(len(result)))


def test_load_with_favorites_filters_correctly(sample_df):
    fake_favorites = ["AAPL", "^GSPC"]

    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv"]), \
         patch("pandas.read_csv", return_value=sample_df), \
         patch("finances.io.datasets.processed.symbols.favorites", fake_favorites):  # ✅

        from finances.io.datasets.processed.symbols import load

        result = load(with_only_favorites=True)

        assert set(result["symbol"]) == {"AAPL", "^GSPC"}
        assert "GOOG" not in result["symbol"].values


def test_load_with_favorites_raises_if_no_match(sample_df):
    fake_favorites = ["TSLA", "MSFT"]

    with patch("finances.configs.io.folder_processed", "/fake"), \
         patch("os.listdir", return_value=["f1.csv"]), \
         patch("pandas.read_csv", return_value=sample_df), \
         patch("finances.io.datasets.processed.symbols.favorites", fake_favorites):  # ✅

        from finances.io.datasets.processed.symbols import load

        with pytest.raises(ValueError, match="filtered dataframe is empty"):
            load(with_only_favorites=True)