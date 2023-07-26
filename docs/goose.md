# Goose: database migration tool for Go

---



## Goose

- database migration tool
- similar to SQLAlchemy
- written in Go
- controlled from CLI
- and also from Go code

---



## Installation check

```
goose
```

---



## Create migration file

```
goose create users sql
```

---



## Update migration file

```
-- +goose Up
-- +goose StatementBegin
CREATE TABLE users (
    id      INTEGER NOT NULL,
    name    VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    PRIMARY KEY (id)
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE users;
-- +goose StatementEnd
```

---



## DB status

```
goose sqlite3 ./test.db status
```

```
goose sqlite3 ./test.db version
```

---



## Migration

```
goose sqlite3 ./test.db up
```

---



## Check DB

```
sqlite3 test.db

.tables

.schema goose_db_version

.schema users
```

---



## Migration back

```
goose sqlite3 ./test.db down

sqlite3 test.db

.tables

.schema goose_db_version

.schema users
```

---



## More migrations

```
goose create role-column sql
```

```
-- +goose Up
-- +goose StatementBegin
ALTER TABLE users ADD COLUMN role VARCHAR;
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
ALTER TABLE users DROP COLUMN role;
-- +goose StatementEnd
```

```
goose sqlite3 ./test.db status

goose sqlite3 ./test.db up
```

---



## Migrate up/down to specific version

```
goose sqlite3 ./test.db down-to 20230708113941
```

---



## Calling Goose from Go

```go
package main

import (
	"log"

	"github.com/pressly/goose/v3"
	_ "modernc.org/sqlite"
)

const databaseType = "sqlite"

const databaseFile = "./test.db"

const command = "status"

const migrationScriptsDirectory = "./"

func main() {
	db, err := goose.OpenDBWithDriver(databaseType, databaseFile)
	if err != nil {
		log.Fatalf("goose: failed to open DB: %v\n", err)
	}

	defer func() {
		if err := db.Close(); err != nil {
			log.Fatalf("goose: failed to close DB: %v\n", err)
		}
	}()

	arguments := []string{}

	err = goose.Run(command, db, migrationScriptsDirectory, arguments...)
	if err != nil {
		log.Fatalf("goose %v: %v", command, err)
	}
}
```

---



## Migration from Go

```go
package main

import (
	"log"

	"github.com/pressly/goose/v3"
	_ "modernc.org/sqlite"
)

const databaseType = "sqlite"

const databaseFile = "./test.db"

const command = "up"

const migrationScriptsDirectory = "./"

func main() {
	db, err := goose.OpenDBWithDriver(databaseType, databaseFile)
	if err != nil {
		log.Fatalf("goose: failed to open DB: %v\n", err)
	}

	defer func() {
		if err := db.Close(); err != nil {
			log.Fatalf("goose: failed to close DB: %v\n", err)
		}
	}()

	arguments := []string{}

	err = goose.Run(command, db, migrationScriptsDirectory, arguments...)
	if err != nil {
		log.Fatalf("goose %v: %v", command, err)
	}
}
```

---



## Migration written in Go

```go
package main

import (
	"database/sql"

	"github.com/pressly/goose/v3"
)

func init() {
	goose.AddMigration(Up00001, Down00001)
}

func Up00001(tx *sql.Tx) error {
	_, err := tx.Exec(`
CREATE TABLE users (
    id      INTEGER NOT NULL,
    name    VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    PRIMARY KEY (id)
);
        `)
	if err != nil {
		return err
	}
	return nil
}

func Down00001(tx *sql.Tx) error {
	_, err := tx.Exec("DROP TABLE users;")
	if err != nil {
		return err
	}
	return nil
}
```

---




```go
package main

import (
	"database/sql"

	"github.com/pressly/goose/v3"
)

func init() {
	goose.AddMigration(Up00002, Down00002)
}

func Up00002(tx *sql.Tx) error {
	_, err := tx.Exec("ALTER TABLE users ADD COLUMN role VARCHAR;")
	if err != nil {
		return err
	}
	return nil
}

func Down00002(tx *sql.Tx) error {
	_, err := tx.Exec("ALTER TABLE users DROP COLUMN role;")
	if err != nil {
		return err
	}
	return nil
}
```

---



```go
package main

import (
	"log"
	"os"

	"github.com/pressly/goose/v3"
	_ "modernc.org/sqlite"
)

const databaseType = "sqlite"

const databaseFile = "./test.db"

const migrationScriptsDirectory = "./"

func main() {
	args := os.Args

	if len(args) <= 1 {
		log.Fatalf("command is expected")
		return
	}

	command := args[1]

	db, err := goose.OpenDBWithDriver(databaseType, databaseFile)
	if err != nil {
		log.Fatalf("goose: failed to open DB: %v\n", err)
	}

	defer func() {
		if err := db.Close(); err != nil {
			log.Fatalf("goose: failed to close DB: %v\n", err)
		}
	}()

	arguments := []string{}

	if len(args) > 1 {
		arguments = append(arguments, args[1:]...)
	}

	err = goose.Run(command, db, migrationScriptsDirectory, arguments...)
	if err != nil {
		log.Fatalf("goose %v: %v", command, err)
	}
}
```

---



# Finito

![Game Over](images/game_over.png)

