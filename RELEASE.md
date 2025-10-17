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
