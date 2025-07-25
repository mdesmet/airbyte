# Systeme
Systeme is an all in one marketing platform.
Using this connector we can extarct records from communities , contacts , tags , contact fields and course resources streams.
Docs : https://developer.systeme.io/reference/api

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key` | `string` | API Key.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| communities | id | DefaultPaginator | ✅ |  ❌  |
| contacts | id | DefaultPaginator | ✅ |  ❌  |
| tags | id | DefaultPaginator | ✅ |  ❌  |
| contact_fields |  | DefaultPaginator | ✅ |  ❌  |
| course_resources | id | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.24 | 2025-07-26 | [63942](https://github.com/airbytehq/airbyte/pull/63942) | Update dependencies |
| 0.0.23 | 2025-07-05 | [62693](https://github.com/airbytehq/airbyte/pull/62693) | Update dependencies |
| 0.0.22 | 2025-06-28 | [62215](https://github.com/airbytehq/airbyte/pull/62215) | Update dependencies |
| 0.0.21 | 2025-06-21 | [61811](https://github.com/airbytehq/airbyte/pull/61811) | Update dependencies |
| 0.0.20 | 2025-06-14 | [60130](https://github.com/airbytehq/airbyte/pull/60130) | Update dependencies |
| 0.0.19 | 2025-05-04 | [58443](https://github.com/airbytehq/airbyte/pull/58443) | Update dependencies |
| 0.0.18 | 2025-04-12 | [58002](https://github.com/airbytehq/airbyte/pull/58002) | Update dependencies |
| 0.0.17 | 2025-04-05 | [56902](https://github.com/airbytehq/airbyte/pull/56902) | Update dependencies |
| 0.0.16 | 2025-03-22 | [56284](https://github.com/airbytehq/airbyte/pull/56284) | Update dependencies |
| 0.0.15 | 2025-03-08 | [55626](https://github.com/airbytehq/airbyte/pull/55626) | Update dependencies |
| 0.0.14 | 2025-03-01 | [55154](https://github.com/airbytehq/airbyte/pull/55154) | Update dependencies |
| 0.0.13 | 2025-02-22 | [54535](https://github.com/airbytehq/airbyte/pull/54535) | Update dependencies |
| 0.0.12 | 2025-02-15 | [54031](https://github.com/airbytehq/airbyte/pull/54031) | Update dependencies |
| 0.0.11 | 2025-02-08 | [53582](https://github.com/airbytehq/airbyte/pull/53582) | Update dependencies |
| 0.0.10 | 2025-02-01 | [53046](https://github.com/airbytehq/airbyte/pull/53046) | Update dependencies |
| 0.0.9 | 2025-01-25 | [52450](https://github.com/airbytehq/airbyte/pull/52450) | Update dependencies |
| 0.0.8 | 2025-01-18 | [51996](https://github.com/airbytehq/airbyte/pull/51996) | Update dependencies |
| 0.0.7 | 2025-01-11 | [51427](https://github.com/airbytehq/airbyte/pull/51427) | Update dependencies |
| 0.0.6 | 2024-12-28 | [50817](https://github.com/airbytehq/airbyte/pull/50817) | Update dependencies |
| 0.0.5 | 2024-12-21 | [50307](https://github.com/airbytehq/airbyte/pull/50307) | Update dependencies |
| 0.0.4 | 2024-12-14 | [49763](https://github.com/airbytehq/airbyte/pull/49763) | Update dependencies |
| 0.0.3 | 2024-12-12 | [49428](https://github.com/airbytehq/airbyte/pull/49428) | Update dependencies |
| 0.0.2 | 2024-12-11 | [49124](https://github.com/airbytehq/airbyte/pull/49124) | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.0.1 | 2024-10-30 | | Initial release by [@ombhardwajj](https://github.com/ombhardwajj) via Connector Builder |

</details>
