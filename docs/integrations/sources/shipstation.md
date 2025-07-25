# Shipstation
This page contains the setup guide and reference information for Shipstation source connector.

Documentation reference:
Visit https://www.shipstation.com/docs/api/ for API documentation

Authentication setup

To get your API key and secret in ShipStation:

↳ Go to Account Settings.

↳ Select Account from the side navigation, then choose API Settings.

↳ Click &quot;Generate New API Keys&quot; if no key and secret are listed yet.

** IMPORTANT **
↳If you&#39;ve already generated your API keys, the existing API keys will be displayed here and the button will read Regenerate API Keys.

If you already have API keys, do NOT generate new ones. Instead, copy your existing key and secret.

Copy your key and secret and paste them into the respective fields.


## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `username` | `string` | API Key.  |  |
| `password` | `string` | API Secret.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| carriers | shippingProviderId | No pagination | ✅ |  ❌  |
| customers | customerId | DefaultPaginator | ✅ |  ❌  |
| fulfillments | fulfillmentId | DefaultPaginator | ✅ |  ❌  |
| orders | orderId | DefaultPaginator | ✅ |  ❌  |
| products | productId | DefaultPaginator | ✅ |  ❌  |
| shipments | shipmentId | DefaultPaginator | ✅ |  ❌  |
| marketplaces | name.marketplaceId | No pagination | ✅ |  ❌  |
| stores | storeId | No pagination | ✅ |  ❌  |
| users | userId | No pagination | ✅ |  ❌  |
| warehouses | warehouseId | No pagination | ✅ |  ❌  |
| webhooks | WebHookID | No pagination | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.2.11 | 2025-07-19 | [63634](https://github.com/airbytehq/airbyte/pull/63634) | Update dependencies |
| 0.2.10 | 2025-07-05 | [62735](https://github.com/airbytehq/airbyte/pull/62735) | Update dependencies |
| 0.2.9 | 2025-06-28 | [62253](https://github.com/airbytehq/airbyte/pull/62253) | Update dependencies |
| 0.2.8 | 2025-06-14 | [61308](https://github.com/airbytehq/airbyte/pull/61308) | Update dependencies |
| 0.2.7 | 2025-05-24 | [60504](https://github.com/airbytehq/airbyte/pull/60504) | Update dependencies |
| 0.2.6 | 2025-05-10 | [60142](https://github.com/airbytehq/airbyte/pull/60142) | Update dependencies |
| 0.2.5 | 2025-05-04 | [59604](https://github.com/airbytehq/airbyte/pull/59604) | Update dependencies |
| 0.2.4 | 2025-04-27 | [59020](https://github.com/airbytehq/airbyte/pull/59020) | Update dependencies |
| 0.2.3 | 2025-04-19 | [57453](https://github.com/airbytehq/airbyte/pull/57453) | Update dependencies |
| 0.2.2 | 2025-03-29 | [56874](https://github.com/airbytehq/airbyte/pull/56874) | Update dependencies |
| 0.2.1 | 2025-03-22 | [56257](https://github.com/airbytehq/airbyte/pull/56257) | Update dependencies |
| 0.2.0 | 2025-03-13 | [55738](https://github.com/airbytehq/airbyte/pull/55738) | add incremental for orders, shipments and fullfillments |
| 0.1.5 | 2025-03-09 | [55648](https://github.com/airbytehq/airbyte/pull/55648) | Update dependencies |
| 0.1.4 | 2025-03-01 | [55122](https://github.com/airbytehq/airbyte/pull/55122) | Update dependencies |
| 0.1.3 | 2025-02-22 | [54511](https://github.com/airbytehq/airbyte/pull/54511) | Update dependencies |
| 0.1.2 | 2025-02-15 | [54047](https://github.com/airbytehq/airbyte/pull/54047) | Update dependencies |
| 0.1.1 | 2025-02-08 | [53551](https://github.com/airbytehq/airbyte/pull/53551) | Update dependencies |
| 0.1.0 | 2025-02-03 | [52707](https://github.com/airbytehq/airbyte/pull/52707) | Change auth method |
| 0.0.6 | 2025-02-01 | [53109](https://github.com/airbytehq/airbyte/pull/53109) | Update dependencies |
| 0.0.5 | 2025-01-25 | [52405](https://github.com/airbytehq/airbyte/pull/52405) | Update dependencies |
| 0.0.4 | 2025-01-18 | [51911](https://github.com/airbytehq/airbyte/pull/51911) | Update dependencies |
| 0.0.3 | 2025-01-11 | [51328](https://github.com/airbytehq/airbyte/pull/51328) | Update dependencies |
| 0.0.2 | 2024-12-28 | [50726](https://github.com/airbytehq/airbyte/pull/50726) | Update dependencies |
| 0.0.1 | 2024-12-21 | | Initial release by [@JohnnyRafael](https://github.com/JohnnyRafael) via Connector Builder |

</details>
