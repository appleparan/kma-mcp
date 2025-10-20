# KST Timezone Support Implementation Plan

## Background
Currently, the MCP server uses UTC timezone throughout, but KMA APIs expect Korean Standard Time (KST, UTC+9) for certain endpoints, particularly ASOS and AWS surface observations.

## Problem
- MCP server uses `datetime.now(UTC)` throughout the codebase
- ASOS and AWS clients expect KST timestamps
- This causes time mismatch issues when querying current data

## Stage 1: Research and Documentation
**Goal**: Identify which APIs use KST vs UTC
**Status**: Not Started

Tasks:
- [ ] Document which KMA APIs expect KST (ASOS, AWS, etc.)
- [ ] Document which KMA APIs expect UTC (Radiosonde, Earthquake, etc.)
- [ ] Review KMA API documentation for timezone specifications
- [ ] Test current behavior with both timezones

**Success Criteria**:
- Clear documentation of timezone requirements per API

## Stage 2: Add KST Timezone Constant
**Goal**: Add KST timezone support infrastructure
**Status**: Not Started

Tasks:
- [ ] Add `from zoneinfo import ZoneInfo` import
- [ ] Define `KST = ZoneInfo('Asia/Seoul')` constant
- [ ] Keep UTC for APIs that need it
- [ ] Update module docstrings to document timezone usage

**Success Criteria**:
- KST constant available in both sync and async servers
- No breaking changes to existing functionality

## Stage 3: Update Surface Observation APIs (ASOS, AWS)
**Goal**: Convert ASOS and AWS endpoints to use KST
**Status**: Not Started

Files to update:
- [ ] `python/src/kma_mcp/mcp_server.py`:
  - `validate_api_key()` - line 75
  - `get_current_weather()` - line 114
  - `get_aws_current_weather()` - line 326
  - `get_dust_current_pm10()` - line 545
  - `get_uv_current_index()` - line 638
  - `get_snow_current_depth()` - line 731
  - `get_nk_current_weather()` - line 824
  - `get_aws_oa_current()` - line 918
  - `get_season_current_year()` - line 983

- [ ] `python/src/kma_mcp/async_mcp_server.py`:
  - Similar functions as above

**Success Criteria**:
- Surface observation APIs use KST
- All tests pass
- API validation works correctly

## Stage 4: Keep UTC for International Standards
**Goal**: Ensure APIs that require UTC continue to use it
**Status**: Not Started

APIs to verify (should remain UTC):
- [ ] Radiosonde (upper air) observations
- [ ] Earthquake monitoring
- [ ] Marine buoy observations (international)
- [ ] Satellite imagery timestamps

**Success Criteria**:
- UTC-based APIs continue working correctly
- Clear comments documenting why each uses UTC vs KST

## Stage 5: Update Tests
**Goal**: Ensure tests reflect timezone changes
**Status**: Not Started

Files to update:
- [ ] `python/tests/surface/test_asos_client.py`
- [ ] `python/tests/surface/test_aws_client.py`
- [ ] `python/tests/surface/test_dust_client.py`
- [ ] `python/tests/surface/test_uv_client.py`
- [ ] `python/tests/surface/test_snow_client.py`
- [ ] `python/tests/surface/test_nk_client.py`
- [ ] `python/tests/surface/test_aws_oa_client.py`

**Success Criteria**:
- All tests pass with KST timestamps
- Tests document expected timezone behavior

## Notes
- Python 3.9+ includes `zoneinfo` in standard library
- `ZoneInfo('Asia/Seoul')` handles DST (though Korea doesn't use DST)
- Consider adding timezone to docstrings for clarity
- May need to update API documentation to specify expected timezone

## Decision Points
- [ ] Confirm which APIs use KST vs UTC (needs user/documentation verification)
- [ ] Decide if we need timezone conversion helpers
- [ ] Decide if we should accept both UTC and KST in user-facing tools
