## [0.3.0] - 2025-10-22

### Bug Fixes

- Correct AWS getMinutelyData parameter order in API validation ([3ba64a7](https://github.com/appleparan/kma-mcp/commit/3ba64a76c904eb9ac85f0e1da694a54a82c31833))
- Correct AWS API parameter name in server validation ([eb07768](https://github.com/appleparan/kma-mcp/commit/eb07768e08b90f9be75ab238c4afc104b7e9c631))
- Update AsyncSnowClient test to use correct method ([b6284bf](https://github.com/appleparan/kma-mcp/commit/b6284bf3aee207774ecfd9b82f008d1a34588cf4))
- Update surface client tests to match refactored APIs ([b18f665](https://github.com/appleparan/kma-mcp/commit/b18f665399475b66cf70f2493f8cf16a76b5c4e2))
- Update MCP server tools to use documented API methods ([9a5d246](https://github.com/appleparan/kma-mcp/commit/9a5d2468e4ddc4320a0b0ab0167bc6545e1fdb06))
- Correct forecast tool method calls to match ForecastClient API ([ce3a595](https://github.com/appleparan/kma-mcp/commit/ce3a595356a5def1603701594910bd80f84eb20e))

### Documentation

- Add MCP server run commands to Quick Start ([b7ec48c](https://github.com/appleparan/kma-mcp/commit/b7ec48c9a209d695e3171a7dd5baacccb7c5672f))
- Update README to specify how to run MCP server ([32ffa7b](https://github.com/appleparan/kma-mcp/commit/32ffa7b402c8354e679d7a38225cdd824c5f48cb))
- Add implementation plan for KST timezone support ([176938e](https://github.com/appleparan/kma-mcp/commit/176938e9b42dcd4ca7e5ab32cce66bf1eda8d80b))
- Add comprehensive API coverage and validation analysis ([468101d](https://github.com/appleparan/kma-mcp/commit/468101d80b6f24a764560cb94f019c4695c4f4b1))
- Add comprehensive API endpoint and timezone documentation ([2a7397c](https://github.com/appleparan/kma-mcp/commit/2a7397c90b59f7605408c5af65e6f3478d4c6b00))
- Add comprehensive KMA API endpoint documentation ([ade4235](https://github.com/appleparan/kma-mcp/commit/ade4235ec723940026086952dd8d07f1a33741d9))
- Update Surface API documentation with implemented methods ([b47d253](https://github.com/appleparan/kma-mcp/commit/b47d253424ebb0f0e6ffd6f36c3b985011ca3aaa))
- Add comprehensive Korean API documentation ([2847574](https://github.com/appleparan/kma-mcp/commit/2847574dd2c583d0cf204b91bae6a7b5e6ab8498))
- Update Forecast API documentation with implemented methods ([6bdbe10](https://github.com/appleparan/kma-mcp/commit/6bdbe107bf81f2edd4f9d5e6ab51957827d8ecf4))
- Add Method entries for all Forecast API endpoints ([df16884](https://github.com/appleparan/kma-mcp/commit/df168846c12ee2de84ecfff8893267a30839e9aa))

### Features

- Add weatherrun CLI command ([0de8661](https://github.com/appleparan/kma-mcp/commit/0de86618833a7f4bad669e81b65a99a30b7bc72b))
- Unify CLI command to weatherrun for both Python and TypeScript ([addc432](https://github.com/appleparan/kma-mcp/commit/addc4326358ffc7a4be162989f6d4b99f0ca89e1))
- Add API key validation on server startup ([bdfa16d](https://github.com/appleparan/kma-mcp/commit/bdfa16d1b26b54c05875601ce7e540c40ffcc9e2))
- Add .env file support for API key configuration ([ebec61f](https://github.com/appleparan/kma-mcp/commit/ebec61ff15b0925195d347fe809d479865aff0b6))
- Complete async MCP server with all features from sync version ([bfc245d](https://github.com/appleparan/kma-mcp/commit/bfc245d172fa00c21fa5051e12795947f5902606))
- Add Pydantic validation for API parameters ([3a3fea3](https://github.com/appleparan/kma-mcp/commit/3a3fea3007c8f74b55a0c70ff2b6034b1bd62615))
- Migrate Snow and ASOS clients to documented API endpoints ([7246f21](https://github.com/appleparan/kma-mcp/commit/7246f21100141ee8d3163b119057b880aef66cb7))
- Migrate AWS clients to documented CGI API endpoints ([5112d75](https://github.com/appleparan/kma-mcp/commit/5112d7527003a35c69522f8f8c5409a955c4fb91))
- Add NotImplementedError stubs for unimplemented Surface API endpoints ([2f0b57a](https://github.com/appleparan/kma-mcp/commit/2f0b57a1b7ea1f75c683dfbac090f7c6ec7f1f16))
- Update UV client to use documented API endpoint ([4e2505b](https://github.com/appleparan/kma-mcp/commit/4e2505bc68d08af7819427f364edec3b6e02de62))
- Sync TypeScript surface API with Python and fix linting issues ([365c390](https://github.com/appleparan/kma-mcp/commit/365c3901a26c7cd99317169865793cac24545703))
- Implement Category 1 Short-term Forecast API endpoints ([fcbe260](https://github.com/appleparan/kma-mcp/commit/fcbe2607bc85db90db0909032d067bb8bf39bb58))
- Implement Category 2 Village Forecast Grid Data API endpoints ([dfcac87](https://github.com/appleparan/kma-mcp/commit/dfcac87167d044fd10066642e3ffdf6f5383584a))
- Implement Category 3 Village Forecast Message API endpoints ([269f9ac](https://github.com/appleparan/kma-mcp/commit/269f9ac9197f1f76f3143a9a695a15b249da2ab0))
- Implement Category 4 Village Forecast API endpoints ([ee32101](https://github.com/appleparan/kma-mcp/commit/ee32101f034144b636a0352323bc2ba006f632d3))
- Implement remaining forecast API categories (5-10) ([562d676](https://github.com/appleparan/kma-mcp/commit/562d676a6072747618f1a7c3c18d0d37a451e58b))
- Implement comprehensive AsyncForecastClient with 40+ methods ([19b45ec](https://github.com/appleparan/kma-mcp/commit/19b45ecc9b6344a14c7c64a415a2d861d19310f1))
- Add Categories 5-10 to TypeScript ForecastClient ([4eb664b](https://github.com/appleparan/kma-mcp/commit/4eb664b368ff8df17f907265d50a8e321ba1a3e2))
- Create modular tools structure for MCP server ([a3b618e](https://github.com/appleparan/kma-mcp/commit/a3b618ee308c4f23c434b9194e47b4870929e77d))
- Add forecast_tools module with 6 forecast/warning tools ([05f7111](https://github.com/appleparan/kma-mcp/commit/05f7111e2b6071b55245828332ff877452cd2503))

### Miscellaneous Tasks

- Add Python 3.14 to test matrix ([4d07f4e](https://github.com/appleparan/kma-mcp/commit/4d07f4e42beb25c2f2f01bda961a1c175ad3bcad))
- Remove Windows from test matrix due to Python 3.14 compatibility ([89dc515](https://github.com/appleparan/kma-mcp/commit/89dc5159f345407dd9ca47c0785a796a4c78da05))

### Refactor

- Remove legacy/undocumented API methods from all clients ([6d5427b](https://github.com/appleparan/kma-mcp/commit/6d5427bf11d50e9ec2fe9c7a56b3158c40d4eff1))
- Remove unused API tool registrations from MCP servers ([8681c38](https://github.com/appleparan/kma-mcp/commit/8681c380dbac7a077acf3517232e3fecd4e65a8e))
- Convert MCP servers to use modular tools pattern ([7a3a6cf](https://github.com/appleparan/kma-mcp/commit/7a3a6cffa720646953533c1ba1b9902aa06c9fdd))

### Styling

- Apply ruff formatting and linting ([a105c72](https://github.com/appleparan/kma-mcp/commit/a105c728d83a1a733c389389d2adf39da502b2de))
- Apply ruff linting and formatting to test files ([ec672bc](https://github.com/appleparan/kma-mcp/commit/ec672bc7c2ca9bac580f4b566a82e2a8538124a6))

### Testing

- Add comprehensive pytest tests for all async clients ([fbf8f34](https://github.com/appleparan/kma-mcp/commit/fbf8f348ea1504c22ad130736834c052f3237a11))
- Update async client tests for new API signatures ([723d671](https://github.com/appleparan/kma-mcp/commit/723d671ec0fe9dcd65e35c285fe7da3cdffe3f55))
- Update TypeScript AWS client tests for new API signature ([22a5fae](https://github.com/appleparan/kma-mcp/commit/22a5faec0bf51425762d50e2101bfb4e595ccfea))
- Add comprehensive tests for forecast API categories 5-10 ([3f50891](https://github.com/appleparan/kma-mcp/commit/3f5089185bca15e4bf552ee069854a987b885a93))
- Add Categories 5-10 tests for TypeScript ForecastClient ([97e3bfc](https://github.com/appleparan/kma-mcp/commit/97e3bfce7563a99bae074019c203d86758cda77c))

<!-- generated by git-cliff -->
