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

## [0.2.3] - 2025-10-17

### Documentation

- Update llms.txt with TypeScript implementation and Apache 2.0 license ([c9fe105](https://github.com/appleparan/kma-mcp/commit/c9fe105e28037b790bec4e72a15c14e05f35887c))

### Miscellaneous Tasks

- Exclude Windows from TypeScript CI jobs ([3875c46](https://github.com/appleparan/kma-mcp/commit/3875c46e3caf40d5120a87b71979fdaafd629a27))
- Bump version to 0.2.3 ([000e2e1](https://github.com/appleparan/kma-mcp/commit/000e2e1bf513b348cd3071d5bea3574b75a6cfd7))

### Testing

- Remove obsolete test_version.py ([9a5408d](https://github.com/appleparan/kma-mcp/commit/9a5408d6d344a566eab8d1e2bf835e15220df682))

## [0.2.2] - 2025-10-17

### Documentation

- Update documentation to reflect Python and TypeScript implementations ([d786293](https://github.com/appleparan/kma-mcp/commit/d78629397afc144071ffe09c7af74bac8149ddfb))
- Enhance TypeScript documentation with comprehensive examples ([77950e7](https://github.com/appleparan/kma-mcp/commit/77950e7b151ab7e38442522d315f0324b3a26dad))

### Miscellaneous Tasks

- Update TypeScript configuration and dependencies ([2567601](https://github.com/appleparan/kma-mcp/commit/2567601f9aa7931b135e5b8170754e93dc700ce3))
- Bump version to 0.2.2 ([46c9fb7](https://github.com/appleparan/kma-mcp/commit/46c9fb70c0339bd654cfb00e45d1fcbdcbf81e3d))

### Styling

- Format base.test.ts with Prettier ([a6a53f6](https://github.com/appleparan/kma-mcp/commit/a6a53f67929ba49803b9e64a9ae4fbe6b2f6d659))

## [0.2.1] - 2025-10-17

### Documentation

- Add TypeScript documentation with TypeDoc ([46d0caa](https://github.com/appleparan/kma-mcp/commit/46d0caa62b709a3719b952389a6803fec5dec84e))
- Add KMA API Hub attribution and links ([ebe0d62](https://github.com/appleparan/kma-mcp/commit/ebe0d622aa208408308cb5c2d53e3191f4e22190))

### Miscellaneous Tasks

- Bump version to 0.2.1 ([f4f0891](https://github.com/appleparan/kma-mcp/commit/f4f0891f94ba42057d4f236538d6a22dff1f35af))

## [0.2.0] - 2025-10-17

### Bug Fixes

- Remove all ESLint warnings ([ccdbfc4](https://github.com/appleparan/kma-mcp/commit/ccdbfc4f1e4914a24ac4bd031a567b65a2a77888))

### Documentation

- Change bullet points from hyphen to asterisk in index.md ([22c893c](https://github.com/appleparan/kma-mcp/commit/22c893c93f0a346d229d7335f3e19ab3d0676adc))

### Features

- Add TypeScript MCP server implementation ([88d8de8](https://github.com/appleparan/kma-mcp/commit/88d8de84d9b4abe36c9c23296ff1d105afd0091a))
- Add AWS (Automated Weather Station) client ([a31fc14](https://github.com/appleparan/kma-mcp/commit/a31fc145956f9b7fc2ab6955474ac6be89ed93b6))
- Add AWS OA, Dust, UV, and Snow clients ([bd80202](https://github.com/appleparan/kma-mcp/commit/bd802020965d6438aeb7f08bb9b17348e3ea2d86))
- Complete Surface category clients ([0992579](https://github.com/appleparan/kma-mcp/commit/09925792bf80b0bc6576210c33d716008c37ab09))
- Add AMOS, Earthquake, and Typhoon clients ([31afcba](https://github.com/appleparan/kma-mcp/commit/31afcba56f0c691dce18943f15462a94d343a5d3))
- Add Integrated and Satellite clients ([1c26645](https://github.com/appleparan/kma-mcp/commit/1c26645069b6cf1724ec0de889e2f5f1a3dfb3c8))
- Complete all remaining API clients ([e0376d5](https://github.com/appleparan/kma-mcp/commit/e0376d5f0a6445890db58cd571e6e6b65ffa2648))
- Add ESLint and Prettier configuration ([2b7f9c9](https://github.com/appleparan/kma-mcp/commit/2b7f9c90427f31537c015394b370c7a2c807dd67))

### Miscellaneous Tasks

- Add TypeScript CI workflow ([31616a5](https://github.com/appleparan/kma-mcp/commit/31616a50f3a6ef87ab82cefd29acc7fa885f3940))
- Bump version to 0.2.0 ([d76825d](https://github.com/appleparan/kma-mcp/commit/d76825d83b398a574a6e9215caa9b03d62b638c4))

### Refactor

- Reorganize project structure to separate Python and TypeScript ([a49cf9e](https://github.com/appleparan/kma-mcp/commit/a49cf9e4d9a48d76800cffaeb4f0f191cb2335f2))

### Testing

- Add comprehensive tests for TypeScript clients ([82ea3f1](https://github.com/appleparan/kma-mcp/commit/82ea3f1d7df81a08b5100eb426146d7d34818a69))

## [0.1.2] - 2025-10-17

### Bug Fixes

- Correct mkdocstrings configuration for Read the Docs ([dded9e8](https://github.com/appleparan/kma-mcp/commit/dded9e8a01fb472e543ca8403edee6546718961e))

### Miscellaneous Tasks

- Bump version to 0.1.2 ([d7c3026](https://github.com/appleparan/kma-mcp/commit/d7c3026a9ce7a920af41bce0bfb8ce3e9ad1a2bf))

## [0.1.1] - 2025-10-17

### Bug Fixes

- Suppress unrecognized links warning in mkdocs build ([eb38f5b](https://github.com/appleparan/kma-mcp/commit/eb38f5b848f088c8afb397a55a553c0f87c50063))

### Documentation

- Update MkDocs documentation with current implementation ([73b12dd](https://github.com/appleparan/kma-mcp/commit/73b12ddebd72bd6a541535bdc9b525ce87350469))

### Miscellaneous Tasks

- Bump version to 0.1.1 ([dddc8aa](https://github.com/appleparan/kma-mcp/commit/dddc8aabe745eac22fc3025e5e89be8c3db08463))

## [0.1.0] - 2025-10-17

### Bug Fixes

- Resolve all critical linting warnings ([e4cf6ee](https://github.com/appleparan/kma-mcp/commit/e4cf6ee4395d07302469764fc9b34cf37ff5189c))

### Documentation

- Add comprehensive API implementation status document ([495ba5c](https://github.com/appleparan/kma-mcp/commit/495ba5c09077b9e6d2bb70b891c0f11621a9ba66))
- Fix API_STATUS.md to properly reflect 100% surface observation completion ([4ef3089](https://github.com/appleparan/kma-mcp/commit/4ef3089f23657cd3ebc759259a2674bb66f32a91))
- Update API_STATUS.md with Marine, Upper-Air, Earthquake APIs and async support ([ddc862b](https://github.com/appleparan/kma-mcp/commit/ddc862bce364d446743254352a6098d9892323ff))
- Add llms.txt for LLM-friendly project documentation ([3dfe022](https://github.com/appleparan/kma-mcp/commit/3dfe0226af3a346eb03df9f970aeb4316a0aae5f))
- Update API_STATUS.md with Global Meteorology GTS implementation ([dac6e09](https://github.com/appleparan/kma-mcp/commit/dac6e09f15afe850b0ede8caa6f90112ed0fc9c3))
- Update API_STATUS.md with Aviation and Integrated Meteorology implementations ([d16f59f](https://github.com/appleparan/kma-mcp/commit/d16f59f9ec479fa2fe4be11c1dee6c5b6244c777))
- Update API_STATUS.md with accurate implementation status ([8cb3b52](https://github.com/appleparan/kma-mcp/commit/8cb3b52d21a7cec0021a43183c252ea723cd0ceb))
- Update llms.txt with new API implementations ([ec92aee](https://github.com/appleparan/kma-mcp/commit/ec92aee784f583801e5ee4b2a4ddb4cfb894dc6c))

### Features

- Add python-dotenv support for API key management ([90267f3](https://github.com/appleparan/kma-mcp/commit/90267f312d00b87867b35471c9254b113db59d77))
- Implement AWS (Automated Weather Station) API ([6fee1c4](https://github.com/appleparan/kma-mcp/commit/6fee1c4d6da948cdfa6dfd7c306c9dfb4030da2a))
- Implement Climate Statistics API for climate normals ([4ca1eab](https://github.com/appleparan/kma-mcp/commit/4ca1eab5e21052748a595e359944e481ec051c7d))
- Implement Yellow Dust (PM10) API for air quality monitoring ([69cc8d7](https://github.com/appleparan/kma-mcp/commit/69cc8d7574a37255f6eea249fa001926d2bdae37))
- Implement UV Radiation API for sun safety monitoring ([201ae99](https://github.com/appleparan/kma-mcp/commit/201ae99a042d1676babff3ed36687b1bea97888a))
- Implement Snow Depth API for winter weather monitoring ([dac7180](https://github.com/appleparan/kma-mcp/commit/dac718002ae6ab2349589156520894ff03130821))
- Implement North Korea Meteorological API for regional monitoring ([84f054d](https://github.com/appleparan/kma-mcp/commit/84f054d1b5b06f0089f55d24db54bdbe1f3c8db2))
- Complete all surface observation APIs (100% coverage) ([1f11fc1](https://github.com/appleparan/kma-mcp/commit/1f11fc1bcfe0ca684007002ae558a22808b8ba04))
- Implement Weather Forecast and Warning APIs ([8f86584](https://github.com/appleparan/kma-mcp/commit/8f86584f2993049b9157082409cf0d681adfdc7c))
- Implement Radar and Typhoon APIs for severe weather monitoring ([fd2975f](https://github.com/appleparan/kma-mcp/commit/fd2975f7df231e2cefdc7eec36d78f017e13150c))
- Implement Marine, Upper-Air, and Earthquake monitoring APIs ([8a091a0](https://github.com/appleparan/kma-mcp/commit/8a091a06253d52cfe38f4e866a78698a83153495))
- Add async support for all API clients ([e69a4c8](https://github.com/appleparan/kma-mcp/commit/e69a4c8079c0817246e5024fb219f7eef54c86f8))
- Add Satellite API (GK2A) support ([a7754eb](https://github.com/appleparan/kma-mcp/commit/a7754ebb4b6aab110935980a0c84827560736b52))
- Add Korean weather code conversion utilities ([a6ef9be](https://github.com/appleparan/kma-mcp/commit/a6ef9be8ed1e5147a6e6b5ebaab2024dfca7ece2))
- Add Global Meteorology GTS API support ([9390443](https://github.com/appleparan/kma-mcp/commit/93904438d28ddf9f9e5ccda4d85fae9fd9d4b14b))
- Add Aviation and Integrated Meteorology APIs ([41952b6](https://github.com/appleparan/kma-mcp/commit/41952b68bff4bdae25d0c605767fef771b6f577b))

### Miscellaneous Tasks

- Add uv.lock for dependency version locking ([fc7a3f0](https://github.com/appleparan/kma-mcp/commit/fc7a3f0d01e2990d0debc07f7d62620835a30df0))
- Remove CPU extra dependency from GitHub Actions CI ([4a1b872](https://github.com/appleparan/kma-mcp/commit/4a1b872b1fef6c8664c04cc510543bd521498aaa))
- Bump version to 0.1.0 ([df2ff2b](https://github.com/appleparan/kma-mcp/commit/df2ff2b64b4329139f3fdb96bda8ea046ba16f44))

### Refactor

- Replace FastAPI server with FastMCP for KMA ASOS data ([c32e503](https://github.com/appleparan/kma-mcp/commit/c32e50357f3cfa829b74e3a489cc01e2c0d077dc))
- Organize surface observation code into dedicated package ([9ad37af](https://github.com/appleparan/kma-mcp/commit/9ad37af7e4bf3da31bc083c6ab97e3936847b126))

### Styling

- Run ruff format and auto-fix linting issues ([bbf574a](https://github.com/appleparan/kma-mcp/commit/bbf574a6e8df72e52f2a21e4b9eeab94d89662c8))
- Suppress BLE001 warnings with noqa comments ([3e90403](https://github.com/appleparan/kma-mcp/commit/3e9040353dbf8694023cf8b62484b36f1f704e95))
- Run ruff format and auto-fix linting issues ([0ee08a5](https://github.com/appleparan/kma-mcp/commit/0ee08a5188aa6f8489774803ae5dfbac799a9569))

### Testing

- Add comprehensive tests for ASOS client and MCP server ([3806ae0](https://github.com/appleparan/kma-mcp/commit/3806ae06125ff9d1e3360406560993218fa01196))

<!-- generated by git-cliff -->
