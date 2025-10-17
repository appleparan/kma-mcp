"""Tests for weather code conversion utilities."""

from kma_mcp.utils.weather_codes import (
    deg_to_direction,
    deg_to_direction_kr,
    direction_to_kr,
    enhance_weather_data,
    format_weather_summary,
    precipitation_type_to_kr,
    sky_condition_to_kr,
    weather_phenomenon_to_kr,
)


class TestWindDirection:
    """Test wind direction conversion functions."""

    def test_deg_to_direction_cardinal(self):
        """Test conversion of cardinal directions."""
        assert deg_to_direction(0) == 'N'
        assert deg_to_direction(90) == 'E'
        assert deg_to_direction(180) == 'S'
        assert deg_to_direction(270) == 'W'
        assert deg_to_direction(360) == 'N'

    def test_deg_to_direction_intercardinal(self):
        """Test conversion of intercardinal directions."""
        assert deg_to_direction(45) == 'NE'
        assert deg_to_direction(135) == 'SE'
        assert deg_to_direction(225) == 'SW'
        assert deg_to_direction(315) == 'NW'

    def test_deg_to_direction_intermediate(self):
        """Test conversion of intermediate directions."""
        assert deg_to_direction(22.5) == 'NNE'
        assert deg_to_direction(67.5) == 'ENE'
        assert deg_to_direction(112.5) == 'ESE'
        assert deg_to_direction(157.5) == 'SSE'

    def test_deg_to_direction_kr_cardinal(self):
        """Test Korean conversion of cardinal directions."""
        assert deg_to_direction_kr(0) == '북'
        assert deg_to_direction_kr(90) == '동'
        assert deg_to_direction_kr(180) == '남'
        assert deg_to_direction_kr(270) == '서'

    def test_deg_to_direction_kr_intercardinal(self):
        """Test Korean conversion of intercardinal directions."""
        assert deg_to_direction_kr(45) == '북동'
        assert deg_to_direction_kr(135) == '남동'
        assert deg_to_direction_kr(225) == '남서'
        assert deg_to_direction_kr(315) == '북서'

    def test_direction_to_kr(self):
        """Test English to Korean direction conversion."""
        assert direction_to_kr('N') == '북'
        assert direction_to_kr('NE') == '북동'
        assert direction_to_kr('E') == '동'
        assert direction_to_kr('SE') == '남동'
        assert direction_to_kr('S') == '남'
        assert direction_to_kr('SW') == '남서'
        assert direction_to_kr('W') == '서'
        assert direction_to_kr('NW') == '북서'

    def test_direction_to_kr_case_insensitive(self):
        """Test that direction conversion is case insensitive."""
        assert direction_to_kr('n') == '북'
        assert direction_to_kr('ne') == '북동'


class TestPrecipitationType:
    """Test precipitation type conversion."""

    def test_precipitation_type_to_kr(self):
        """Test precipitation type code conversion."""
        assert precipitation_type_to_kr(0) == '강수 없음'
        assert precipitation_type_to_kr(1) == '비'
        assert precipitation_type_to_kr(2) == '비/눈'
        assert precipitation_type_to_kr(3) == '눈'
        assert precipitation_type_to_kr(4) == '소나기'
        assert precipitation_type_to_kr(5) == '빗방울'
        assert precipitation_type_to_kr(6) == '진눈깨비'
        assert precipitation_type_to_kr(7) == '눈날림'

    def test_precipitation_type_unknown(self):
        """Test unknown precipitation type code."""
        assert '알 수 없음' in precipitation_type_to_kr(99)


class TestSkyCondition:
    """Test sky condition conversion."""

    def test_sky_condition_to_kr(self):
        """Test sky condition code conversion."""
        assert sky_condition_to_kr(1) == '맑음'
        assert sky_condition_to_kr(3) == '구름많음'
        assert sky_condition_to_kr(4) == '흐림'

    def test_sky_condition_unknown(self):
        """Test unknown sky condition code."""
        assert '알 수 없음' in sky_condition_to_kr(99)


class TestWeatherPhenomenon:
    """Test weather phenomenon conversion."""

    def test_weather_phenomenon_to_kr(self):
        """Test weather phenomenon code conversion."""
        assert weather_phenomenon_to_kr(0) == '없음'
        assert weather_phenomenon_to_kr(1) == '비'
        assert weather_phenomenon_to_kr(2) == '비/눈'
        assert weather_phenomenon_to_kr(3) == '눈'
        assert weather_phenomenon_to_kr(4) == '소나기'

    def test_weather_phenomenon_unknown(self):
        """Test unknown weather phenomenon code."""
        assert '알 수 없음' in weather_phenomenon_to_kr(99)


class TestEnhanceWeatherData:
    """Test weather data enhancement."""

    def test_enhance_wind_direction_degree(self):
        """Test enhancement of wind direction from degrees."""
        data = {'wdDeg': 45.0}
        enhanced = enhance_weather_data(data)
        assert enhanced['wdDeg_kr'] == '북동'

    def test_enhance_wind_direction_code(self):
        """Test enhancement of wind direction from code."""
        data = {'wd': 'NE'}
        enhanced = enhance_weather_data(data)
        assert enhanced['wd_kr'] == '북동'

    def test_enhance_precipitation_type(self):
        """Test enhancement of precipitation type."""
        data = {'pty': 1}
        enhanced = enhance_weather_data(data)
        assert enhanced['pty_kr'] == '비'

    def test_enhance_sky_condition(self):
        """Test enhancement of sky condition."""
        data = {'sky': 3}
        enhanced = enhance_weather_data(data)
        assert enhanced['sky_kr'] == '구름많음'

    def test_enhance_weather_phenomenon(self):
        """Test enhancement of weather phenomenon."""
        data = {'wf': 1}
        enhanced = enhance_weather_data(data)
        assert enhanced['wf_kr'] == '비'

    def test_enhance_complete_data(self):
        """Test enhancement of complete weather data."""
        data = {'wdDeg': 90.0, 'pty': 0, 'sky': 1, 'wf': 0}
        enhanced = enhance_weather_data(data)
        assert enhanced['wdDeg_kr'] == '동'
        assert enhanced['pty_kr'] == '강수 없음'
        assert enhanced['sky_kr'] == '맑음'
        assert enhanced['wf_kr'] == '없음'

    def test_enhance_preserves_original(self):
        """Test that enhancement preserves original data."""
        data = {'wdDeg': 45.0, 'ta': 15.5}
        enhanced = enhance_weather_data(data)
        assert enhanced['wdDeg'] == 45.0
        assert enhanced['ta'] == 15.5

    def test_enhance_handles_none_values(self):
        """Test that enhancement handles None values gracefully."""
        data = {'wdDeg': None, 'pty': None, 'sky': None}
        enhanced = enhance_weather_data(data)
        assert 'wdDeg_kr' not in enhanced
        assert 'pty_kr' not in enhanced
        assert 'sky_kr' not in enhanced


class TestFormatWeatherSummary:
    """Test weather summary formatting."""

    def test_format_complete_summary(self):
        """Test formatting of complete weather data."""
        data = {
            'stnNm': '서울',
            'ta': 15.5,
            'hm': 65,
            'wdDeg': 45.0,
            'ws': 3.2,
            'pty': 0,
            'sky': 1,
        }
        summary = format_weather_summary(data)
        assert '서울' in summary
        assert '15.5°C' in summary
        assert '65%' in summary
        assert '북동' in summary
        assert '3.2m/s' in summary
        assert '강수 없음' in summary
        assert '맑음' in summary

    def test_format_partial_summary(self):
        """Test formatting of partial weather data."""
        data = {'stnNm': '부산', 'ta': 20.0, 'sky': 3}
        summary = format_weather_summary(data)
        assert '부산' in summary
        assert '20.0°C' in summary
        assert '구름많음' in summary

    def test_format_with_precipitation(self):
        """Test formatting with precipitation amount."""
        data = {'stnNm': '제주', 'ta': 18.0, 'pty': 1, 'rn': 5.5}
        summary = format_weather_summary(data)
        assert '제주' in summary
        assert '18.0°C' in summary
        assert '비' in summary
        assert '5.5mm' in summary

    def test_format_empty_data(self):
        """Test formatting of empty data."""
        data = {}
        summary = format_weather_summary(data)
        assert summary == ''
