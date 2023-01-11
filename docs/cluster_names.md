# Cluster names benchmark (in progress)

---

## Cluster name

* represented as UUID
    - in format `123e4567-e89b-12d3-a456-426614174000`
* how to store it in PostgreSQL?
    - `char(36)`
    - `varchar(36)`
    - `bytea`
    - `uuid`

---

## Why bother?

* DB size
    - `char`: 36 bytes per record
    - `varchar`: 1 byte + 36 bytes per record
    - `bytea`: 1 byte + 36/2 bytes per record
    - `uuid`: 36/2 bytes per record (automatically converted to/from char)

---

## Why bother?

* Performance
    - `column_name` is used in indices
    - so it's stored separately in B-tree or similar structure
    - and size matters there
    - (number of blocks stored in memory, number of block read for each query)

---

## Theory

* `uuid` might be the best option 
* `bytea` might be a bit worse
* `char` on third place
* `varchar` on the last place

---

## Don't trust theory...until proven

* Use real table schema
* Use real SQL statements

---

## Table schema

```sql
CREATE TABLE IF NOT EXISTS reported_benchmark_1 (
    org_id            integer not null,
    account_number    integer not null,
    cluster           character(36) not null,
                      -- varchar, bytea, uuid
    notification_type integer not null,
    state             integer not null,
    report            varchar not null,
    updated_at        timestamp not null,
    notified_at       timestamp not null,
    error_log         varchar,

    PRIMARY KEY (org_id, cluster, notified_at)
);
```

---

### SQL statements

```sql
SELECT org_id, account_number, notification_type, state, report, updated_at, notified_at, error_log
  FROM reported_benchmark_1
 WHERE cluster=$1
```

```sql
INSERT INTO reported_benchmark_1
(org_id, account_number, cluster, notification_type, state, report, updated_at, notified_at, error_log)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
```

```sql
DELETE FROM reported_benchmark_1
 WHERE cluster=$1
```

---

### Small tables with 100 records

* Just to quick check if benchmark works

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8          100      1990038 ns/op
BenchmarkInsertClusterAsVarchar-8       100      2099556 ns/op
BenchmarkInsertClusterAsBytea-8         100      2060851 ns/op
BenchmarkInsertClusterAsUUID-8          100      2024153 ns/op
BenchmarkDeleteClusterAsChar-8          100      2058986 ns/op
BenchmarkDeleteClusterAsVarchar-8       100      1855351 ns/op
BenchmarkDeleteClusterAsBytea-8         100      1645019 ns/op
BenchmarkDeleteClusterAsUUID-8          100      1955547 ns/op
BenchmarkSelectClusterAsChar-8          100       738880 ns/op
BenchmarkSelectClusterAsVarchar-8       100       487008 ns/op
BenchmarkSelectClusterAsBytea-8         100       751563 ns/op
BenchmarkSelectClusterAsUUID-8          100       725236 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      2884.159s
```

---

### Medium tables with 1000 records

* Possible speedup won't be much visible there

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8         1000      1926411 ns/op
BenchmarkInsertClusterAsVarchar-8      1000      2045086 ns/op
BenchmarkInsertClusterAsBytea-8        1000      2063993 ns/op
BenchmarkInsertClusterAsUUID-8         1000      1783965 ns/op
BenchmarkDeleteClusterAsChar-8         1000      2117746 ns/op
BenchmarkDeleteClusterAsVarchar-8      1000      2129500 ns/op
BenchmarkDeleteClusterAsBytea-8        1000      2156378 ns/op
BenchmarkDeleteClusterAsUUID-8         1000      2244083 ns/op
BenchmarkSelectClusterAsChar-8         1000       313019 ns/op
BenchmarkSelectClusterAsVarchar-8      1000       288332 ns/op
BenchmarkSelectClusterAsBytea-8        1000       294040 ns/op
BenchmarkSelectClusterAsUUID-8         1000       262347 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      2914.665s
```

---

### Larger tables with 10000 records

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8        10000      2006754 ns/op
BenchmarkInsertClusterAsVarchar-8     10000      2051222 ns/op
BenchmarkInsertClusterAsBytea-8       10000      2019572 ns/op
BenchmarkInsertClusterAsUUID-8        10000      2042202 ns/op
BenchmarkDeleteClusterAsChar-8        10000      2539460 ns/op
BenchmarkDeleteClusterAsVarchar-8     10000      2474926 ns/op
BenchmarkDeleteClusterAsBytea-8       10000      2552969 ns/op
BenchmarkDeleteClusterAsUUID-8        10000      2402486 ns/op
BenchmarkSelectClusterAsChar-8        10000      1269443 ns/op
BenchmarkSelectClusterAsVarchar-8     10000      1323098 ns/op
BenchmarkSelectClusterAsBytea-8       10000      1332636 ns/op
BenchmarkSelectClusterAsUUID-8        10000      1080828 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      6151.486s
```

---

### Huge tables with 50000 records

* Aprox. number of records stored in real Aggregator database

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8        50000      2044506 ns/op
BenchmarkInsertClusterAsVarchar-8     50000      2037891 ns/op
BenchmarkInsertClusterAsBytea-8       50000      2020112 ns/op
BenchmarkInsertClusterAsUUID-8        50000      2037548 ns/op
BenchmarkDeleteClusterAsChar-8        50000      7413309 ns/op
BenchmarkDeleteClusterAsVarchar-8     50000      7466647 ns/op
BenchmarkDeleteClusterAsBytea-8       50000      7296210 ns/op
BenchmarkDeleteClusterAsUUID-8        50000      6645221 ns/op
BenchmarkSelectClusterAsChar-8        50000      5375757 ns/op
BenchmarkSelectClusterAsVarchar-8     50000      5579126 ns/op
BenchmarkSelectClusterAsBytea-8       50000      5480033 ns/op
BenchmarkSelectClusterAsUUID-8        50000      4437253 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      9470.518s
```
---

### Huge tables with 100000 records

* Aprox. number of records stored in real Notification Service database

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8       100000      3030527 ns/op
BenchmarkInsertClusterAsVarchar-8    100000      3019363 ns/op
BenchmarkInsertClusterAsBytea-8      100000      2962184 ns/op
BenchmarkInsertClusterAsUUID-8       100000      2988198 ns/op
BenchmarkDeleteClusterAsChar-8       100000     11399657 ns/op
BenchmarkDeleteClusterAsVarchar-8    100000     11439103 ns/op
BenchmarkDeleteClusterAsBytea-8      100000     11334972 ns/op
BenchmarkDeleteClusterAsUUID-8       100000      9881923 ns/op
BenchmarkSelectClusterAsChar-8       100000     10860747 ns/op
BenchmarkSelectClusterAsVarchar-8    100000     11064993 ns/op
BenchmarkSelectClusterAsBytea-8      100000     10914949 ns/op
BenchmarkSelectClusterAsUUID-8       100000      8749562 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      17928.382s
```

---

### Problems that has been solved

* Delay between tests to "fix" DB vacuuming issue
* Total test time
    - by default benchmarks are killed after 10 minutes

---

## Links

* [Character Types in PostgreSQL](https://www.postgresql.org/docs/current/datatype-character.html)
* [Binary Data Types in PostgreSQL](https://www.postgresql.org/docs/current/datatype-binary.html)
* [UUID Type](https://www.postgresql.org/docs/current/datatype-uuid.html)
