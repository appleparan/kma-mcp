[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/satellite](../README.md) / SatelliteClient

# Class: SatelliteClient

Defined in: [src/clients/satellite.ts:24](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/satellite.ts#L24)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new SatelliteClient**(`config`): `SatelliteClient`

Defined in: [src/clients/satellite.ts:25](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/satellite.ts#L25)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`SatelliteClient`

#### Overrides

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`constructor`](../../base/classes/BaseKMAClient.md#constructor)

## Properties

### authKey

> `protected` **authKey**: `string`

Defined in: [src/clients/base.ts:43](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L43)

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`authKey`](../../base/classes/BaseKMAClient.md#authkey)

***

### client

> `protected` **client**: `AxiosInstance`

Defined in: [src/clients/base.ts:42](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L42)

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`client`](../../base/classes/BaseKMAClient.md#client)

## Methods

### formatDateTime()

> `protected` **formatDateTime**(`date`, `includeTime`): `string`

Defined in: [src/clients/base.ts:96](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L96)

Format datetime to KMA API format (YYYYMMDDHHmm or YYYYMMDD)

#### Parameters

##### date

`Date`

##### includeTime

`boolean` = `true`

#### Returns

`string`

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`formatDateTime`](../../base/classes/BaseKMAClient.md#formatdatetime)

***

### getSatelliteFileList()

> **getSatelliteFileList**(`sat`, `vars`, `area`, `fmt`, `tm?`): `Promise`\<[`SatelliteFile`](../interfaces/SatelliteFile.md)[]\>

Defined in: [src/clients/satellite.ts:37](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/satellite.ts#L37)

Get list of available satellite files

#### Parameters

##### sat

`string` = `'GK2A'`

Satellite identifier (default: 'GK2A')

##### vars

`string` = `'L1B'`

Variable/product type (default: 'L1B')

##### area

`string` = `'FD'`

Region code (default: 'FD' for Full Disk)

##### fmt

`string` = `'NetCDF'`

File format (default: 'NetCDF')

##### tm?

`string`

Time filter in YYYYMMDDHHmm format (optional)

#### Returns

`Promise`\<[`SatelliteFile`](../interfaces/SatelliteFile.md)[]\>

***

### getSatelliteImagery()

> **getSatelliteImagery**(`level`, `product`, `area`, `tm`): `Promise`\<[`SatelliteImagery`](../interfaces/SatelliteImagery.md)[]\>

Defined in: [src/clients/satellite.ts:63](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/satellite.ts#L63)

Get satellite imagery data

#### Parameters

##### level

`string`

Data level ('l1b' or 'l2')

##### product

`string`

Product type/channel

##### area

`string`

Area code (FD, KO, EA, ELA, TP)

##### tm

`string`

Time in YYYYMMDDHHmm format

#### Returns

`Promise`\<[`SatelliteImagery`](../interfaces/SatelliteImagery.md)[]\>

***

### makeRequest()

> `protected` **makeRequest**\<`T`\>(`endpoint`, `params`): `Promise`\<`T`[]\>

Defined in: [src/clients/base.ts:56](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/base.ts#L56)

#### Type Parameters

##### T

`T` = `unknown`

#### Parameters

##### endpoint

`string`

##### params

`Record`\<`string`, `unknown`\>

#### Returns

`Promise`\<`T`[]\>

#### Inherited from

[`BaseKMAClient`](../../base/classes/BaseKMAClient.md).[`makeRequest`](../../base/classes/BaseKMAClient.md#makerequest)
