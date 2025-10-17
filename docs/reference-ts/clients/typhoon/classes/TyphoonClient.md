[**@appleparan/kma-mcp-server**](../../../README.md)

***

[@appleparan/kma-mcp-server](../../../README.md) / [clients/typhoon](../README.md) / TyphoonClient

# Class: TyphoonClient

Defined in: [src/clients/typhoon.ts:20](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L20)

## Extends

- [`BaseKMAClient`](../../base/classes/BaseKMAClient.md)

## Constructors

### Constructor

> **new TyphoonClient**(`config`): `TyphoonClient`

Defined in: [src/clients/typhoon.ts:21](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L21)

#### Parameters

##### config

[`KMAClientConfig`](../../base/interfaces/KMAClientConfig.md)

#### Returns

`TyphoonClient`

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

### getCurrentTyphoons()

> **getCurrentTyphoons**(): `Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

Defined in: [src/clients/typhoon.ts:28](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L28)

Get information on currently active typhoons

#### Returns

`Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

***

### getTyphoonById()

> **getTyphoonById**(`typhoonId`): `Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

Defined in: [src/clients/typhoon.ts:36](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L36)

Get detailed information for a specific typhoon

#### Parameters

##### typhoonId

`string`

Typhoon identification number (e.g., '2501')

#### Returns

`Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

***

### getTyphoonForecast()

> **getTyphoonForecast**(`typhoonId`): `Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

Defined in: [src/clients/typhoon.ts:46](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L46)

Get forecast track for a specific typhoon

#### Parameters

##### typhoonId

`string`

Typhoon identification number

#### Returns

`Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

***

### getTyphoonHistory()

> **getTyphoonHistory**(`year`): `Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

Defined in: [src/clients/typhoon.ts:56](https://github.com/appleparan/kma-mcp/blob/d76825d83b398a574a6e9215caa9b03d62b638c4/typescript/src/clients/typhoon.ts#L56)

Get typhoon history for a specific year

#### Parameters

##### year

Year in YYYY format

`string` | `number`

#### Returns

`Promise`\<[`TyphoonInfo`](../interfaces/TyphoonInfo.md)[]\>

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
