[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/aws\_oa](../README.md) / AWSOAClient

# Class: AWSOAClient

Defined in: [src/clients/aws\_oa.ts:19](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/aws_oa.ts#L19)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new AWSOAClient**(`config`): `AWSOAClient`

Defined in: [src/clients/aws\_oa.ts:20](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/aws_oa.ts#L20)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`AWSOAClient`

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

### getAnalysisData()

> **getAnalysisData**(`tm`, `x`, `y`): `Promise`\<[`AWSOAData`](../interfaces/AWSOAData.md)[]\>

Defined in: [src/clients/aws\_oa.ts:30](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/aws_oa.ts#L30)

Get AWS objective analysis data for a specific location and time

#### Parameters

##### tm

Time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### x

`number`

Longitude coordinate

##### y

`number`

Latitude coordinate

#### Returns

`Promise`\<[`AWSOAData`](../interfaces/AWSOAData.md)[]\>

***

### getAnalysisPeriod()

> **getAnalysisPeriod**(`tm1`, `tm2`, `x`, `y`): `Promise`\<[`AWSOAData`](../interfaces/AWSOAData.md)[]\>

Defined in: [src/clients/aws\_oa.ts:46](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/aws_oa.ts#L46)

Get AWS objective analysis data for a location over a time period

#### Parameters

##### tm1

Start time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### tm2

End time in YYYYMMDDHHmm format or Date object

`string` | `Date`

##### x

`number`

Longitude coordinate

##### y

`number`

Latitude coordinate

#### Returns

`Promise`\<[`AWSOAData`](../interfaces/AWSOAData.md)[]\>

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
