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
DELETE FROM reported_benchmark_1 WHERE cluster=$1
```

---

### Small tables with 100 records

```
goos: linux
goarch: amd64
pkg: github.com/RedHatInsights/ccx-notification-service
BenchmarkInsertClusterAsChar-8               100           1990038 ns/op
BenchmarkInsertClusterAsVarchar-8            100           2099556 ns/op
BenchmarkInsertClusterAsBytea-8              100           2060851 ns/op
BenchmarkInsertClusterAsUUID-8               100           2024153 ns/op
BenchmarkDeleteClusterAsChar-8               100           2058986 ns/op
BenchmarkDeleteClusterAsVarchar-8            100           1855351 ns/op
BenchmarkDeleteClusterAsBytea-8              100           1645019 ns/op
BenchmarkDeleteClusterAsUUID-8               100           1955547 ns/op
BenchmarkSelectClusterAsChar-8               100            738880 ns/op
BenchmarkSelectClusterAsVarchar-8            100            487008 ns/op
BenchmarkSelectClusterAsBytea-8              100            751563 ns/op
BenchmarkSelectClusterAsUUID-8               100            725236 ns/op
PASS
ok      github.com/RedHatInsights/ccx-notification-service      2884.159s
```

---

### Medium tables with 1000 records

```
```

---

### Larger tables with 10000 records

```
```

---

### Huge tables with 100000 records

```
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
