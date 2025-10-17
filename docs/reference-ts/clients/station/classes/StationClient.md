[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/station](../README.md) / StationClient

# Class: StationClient

Defined in: [src/clients/station.ts:17](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/station.ts#L17)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new StationClient**(`config`): `StationClient`

Defined in: [src/clients/station.ts:18](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/station.ts#L18)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`StationClient`

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

### getAsosStations()

> **getAsosStations**(`stn`): `Promise`\<[`StationInfo`](../interfaces/StationInfo.md)[]\>

Defined in: [src/clients/station.ts:26](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/station.ts#L26)

Get ASOS station information

#### Parameters

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`StationInfo`](../interfaces/StationInfo.md)[]\>

***

### getAwsStations()

> **getAwsStations**(`stn`): `Promise`\<[`StationInfo`](../interfaces/StationInfo.md)[]\>

Defined in: [src/clients/station.ts:36](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/station.ts#L36)

Get AWS station information

#### Parameters

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`StationInfo`](../interfaces/StationInfo.md)[]\>

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
