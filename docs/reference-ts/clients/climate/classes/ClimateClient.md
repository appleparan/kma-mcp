[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/climate](../README.md) / ClimateClient

# Class: ClimateClient

Defined in: [src/clients/climate.ts:18](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L18)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new ClimateClient**(`config`): `ClimateClient`

Defined in: [src/clients/climate.ts:19](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L19)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`ClimateClient`

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

### getAnnualNormals()

> **getAnnualNormals**(`stn`): `Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

Defined in: [src/clients/climate.ts:94](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L94)

Get annual climate normal values

#### Parameters

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

***

### getDailyNormals()

> **getDailyNormals**(`startMonth`, `startDay`, `endMonth`, `endDay`, `stn`): `Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

Defined in: [src/clients/climate.ts:31](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L31)

Get daily climate normal values for a date range

#### Parameters

##### startMonth

`number`

Start month (1-12)

##### startDay

`number`

Start day (1-31)

##### endMonth

`number`

End month (1-12)

##### endDay

`number`

End day (1-31)

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

***

### getMonthlyNormals()

> **getMonthlyNormals**(`startMonth`, `endMonth`, `stn`): `Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

Defined in: [src/clients/climate.ts:78](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L78)

Get monthly climate normal values

#### Parameters

##### startMonth

`number`

Start month (1-12)

##### endMonth

`number`

End month (1-12)

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

***

### getNormalsByPeriod()

> **getNormalsByPeriod**(`periodType`, `startMonth?`, `startDay?`, `endMonth?`, `endDay?`, `stn?`): `Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

Defined in: [src/clients/climate.ts:109](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L109)

Get climate normals with flexible period specification

#### Parameters

##### periodType

Type of period ('daily', 'tenday', 'monthly', 'annual')

`"daily"` | `"tenday"` | `"monthly"` | `"annual"`

##### startMonth?

`number`

Start month (required for daily, tenday, monthly)

##### startDay?

`number`

Start day (required for daily) or period (1-3 for tenday)

##### endMonth?

`number`

End month (required for daily, tenday, monthly)

##### endDay?

`number`

End day (required for daily) or period (1-3 for tenday)

##### stn?

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

***

### getTenDayNormals()

> **getTenDayNormals**(`startMonth`, `startPeriod`, `endMonth`, `endPeriod`, `stn`): `Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

Defined in: [src/clients/climate.ts:56](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/climate.ts#L56)

Get 10-day (dekad) climate normal values
Each month is divided into three periods: 1 (1-10), 2 (11-20), 3 (21-end)

#### Parameters

##### startMonth

`number`

Start month (1-12)

##### startPeriod

`number`

Start period (1-3)

##### endMonth

`number`

End month (1-12)

##### endPeriod

`number`

End period (1-3)

##### stn

Station ID (0 for all stations)

`string` | `number`

#### Returns

`Promise`\<[`ClimateNormal`](../interfaces/ClimateNormal.md)[]\>

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
