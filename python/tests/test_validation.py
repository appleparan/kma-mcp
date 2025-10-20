"""Tests for input validation."""

import pytest
from pydantic import ValidationError

from kma_mcp.validation import (
    DateParam,
    DateTimeParam,
    InvalidCoordinateError,
    InvalidDateError,
    InvalidStationError,
    InvalidTimeError,
    LatitudeParam,
    LongitudeParam,
    StationParam,
    YearParam,
)


class TestDateParam:
    """Tests for DateParam validator."""

    def test_valid_date(self):
        """Test valid date formats."""
        date = DateParam(value='20250101')
        assert date.value == '20250101'
        assert str(date) == '20250101'

    def test_leap_year(self):
        """Test leap year date."""
        date = DateParam(value='20240229')
        assert date.value == '20240229'

    def test_invalid_format(self):
        """Test invalid date format."""
        with pytest.raises((ValidationError, InvalidDateError)):
            DateParam(value='2025-01-01')

    def test_invalid_date(self):
        """Test invalid date value."""
        with pytest.raises((ValidationError, InvalidDateError)):
            DateParam(value='20250230')  # February 30th

    def test_invalid_length(self):
        """Test invalid length."""
        with pytest.raises((ValidationError, InvalidDateError)):
            DateParam(value='2025010')  # Too short


class TestDateTimeParam:
    """Tests for DateTimeParam validator."""

    def test_valid_datetime(self):
        """Test valid datetime formats."""
        dt = DateTimeParam(value='202501011200')
        assert dt.value == '202501011200'
        assert str(dt) == '202501011200'

    def test_midnight(self):
        """Test midnight time."""
        dt = DateTimeParam(value='202501010000')
        assert dt.value == '202501010000'

    def test_end_of_day(self):
        """Test end of day time."""
        dt = DateTimeParam(value='202501012359')
        assert dt.value == '202501012359'

    def test_invalid_format(self):
        """Test invalid datetime format."""
        with pytest.raises((ValidationError, InvalidTimeError)):
            DateTimeParam(value='2025-01-01 12:00')

    def test_invalid_hour(self):
        """Test invalid hour."""
        with pytest.raises((ValidationError, InvalidTimeError)):
            DateTimeParam(value='202501012560')  # Hour 25

    def test_invalid_minute(self):
        """Test invalid minute."""
        with pytest.raises((ValidationError, InvalidTimeError)):
            DateTimeParam(value='202501011299')  # Minute 99


class TestYearParam:
    """Tests for YearParam validator."""

    def test_valid_year(self):
        """Test valid year."""
        year = YearParam(value=2025)
        assert year.value == 2025
        assert str(year) == '2025'

    def test_minimum_year(self):
        """Test minimum valid year."""
        year = YearParam(value=1900)
        assert year.value == 1900

    def test_maximum_year(self):
        """Test maximum valid year."""
        year = YearParam(value=2100)
        assert year.value == 2100

    def test_year_too_low(self):
        """Test year below minimum."""
        with pytest.raises(ValidationError):
            YearParam(value=1899)

    def test_year_too_high(self):
        """Test year above maximum."""
        with pytest.raises(ValidationError):
            YearParam(value=2101)


class TestStationParam:
    """Tests for StationParam validator."""

    def test_all_stations(self):
        """Test all stations (0)."""
        stn = StationParam(value=0)
        assert stn.value == 0
        assert str(stn) == '0'

    def test_seoul_station(self):
        """Test Seoul station."""
        stn = StationParam(value=108)
        assert stn.value == 108

    def test_wmo_station(self):
        """Test WMO station code."""
        stn = StationParam(value=47122)  # Seoul upper-air
        assert stn.value == 47122

    def test_negative_station(self):
        """Test negative station ID."""
        with pytest.raises((ValidationError, InvalidStationError)):
            StationParam(value=-1)

    def test_station_too_large(self):
        """Test station ID too large."""
        with pytest.raises((ValidationError, InvalidStationError)):
            StationParam(value=100000)


class TestLatitudeParam:
    """Tests for LatitudeParam validator."""

    def test_seoul_latitude(self):
        """Test Seoul latitude."""
        lat = LatitudeParam(value=37.5)
        assert lat.value == 37.5
        assert str(lat) == '37.5'

    def test_southern_limit(self):
        """Test southern limit of Korea."""
        lat = LatitudeParam(value=33.0)
        assert lat.value == 33.0

    def test_northern_limit(self):
        """Test northern limit of Korea."""
        lat = LatitudeParam(value=43.0)
        assert lat.value == 43.0

    def test_latitude_too_south(self):
        """Test latitude too far south."""
        with pytest.raises((ValidationError, InvalidCoordinateError)):
            LatitudeParam(value=32.0)

    def test_latitude_too_north(self):
        """Test latitude too far north."""
        with pytest.raises((ValidationError, InvalidCoordinateError)):
            LatitudeParam(value=44.0)


class TestLongitudeParam:
    """Tests for LongitudeParam validator."""

    def test_seoul_longitude(self):
        """Test Seoul longitude."""
        lon = LongitudeParam(value=127.0)
        assert lon.value == 127.0
        assert str(lon) == '127.0'

    def test_western_limit(self):
        """Test western limit of Korea."""
        lon = LongitudeParam(value=124.0)
        assert lon.value == 124.0

    def test_eastern_limit(self):
        """Test eastern limit of Korea."""
        lon = LongitudeParam(value=132.0)
        assert lon.value == 132.0

    def test_longitude_too_west(self):
        """Test longitude too far west."""
        with pytest.raises((ValidationError, InvalidCoordinateError)):
            LongitudeParam(value=123.0)

    def test_longitude_too_east(self):
        """Test longitude too far east."""
        with pytest.raises((ValidationError, InvalidCoordinateError)):
            LongitudeParam(value=133.0)
