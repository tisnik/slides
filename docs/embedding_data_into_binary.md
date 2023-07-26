# Embedding data into executables produced by Go compiler

---

![Go](images/fiveyears.jpg)

---



## Go's strengths

- simple language
- rich standard library
- super fast compiler + linker
- and: statically linked executables

---



## Staticall linked executables

- does not depend on many external dynamic libraries

```
$ ldd hello_world
        not a dynamic executable
```

---



## But what about data?

- one executable with embedded data is a good idea
- possible in Go >= 1.16!

---



## Embedding string

```go
package main

import (
	_ "embed"
	"fmt"
)

//go:embed hello.txt
var helloMessage string

func main() {
	fmt.Println(helloMessage)
}
```

---



## Embedding multi-line string

```go
package main

import (
	_ "embed"
	"fmt"
)

//go:embed lorem_ipsum.txt
var loremIpsum string

func main() {
	fmt.Println(loremIpsum)
}
```

---



## Embedding binary data

```go
package main

import (
	_ "embed"
	"fmt"
)

//go:embed lorem_ipsum.txt
var loremIpsum []byte

func main() {
	fmt.Println(loremIpsum)
}
```

---



## No other data types can be embedded!

```go
package main

import (
	_ "embed"
	"fmt"
)

type Foo struct {
	x string
	y bool
}

//go:embed lorem_ipsum.txt
var loremIpsum Foo

func main() {
	fmt.Println(loremIpsum)
}
```

---



## Access embedded data via virtual filesystem

```go
package main

import (
	"embed"
	"fmt"
	"log"
)

//go:embed lorem_ipsum.txt
var f embed.FS

func main() {
	data, err := f.ReadFile("lorem_ipsum.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(data))
}
```

---



## Large binary data

```go
package main

import (
	"embed"
	"log"
	"os"
)

//go:embed npe.jpg
var f embed.FS

func main() {
	data, err := f.ReadFile("npe.jpg")
	if err != nil {
		log.Fatal(err)
	}

	// open output file
	fout, err := os.Create("npe2.jpg")
	if err != nil {
		log.Fatal(err)
	}
	// close fo on exit and check for its returned error
	defer func() {
		err := fout.Close()
		if err != nil {
			log.Fatal(err)
		}
	}()

	fout.Write(data)
}
```

---



## More "files" on virtual filesystem

```go
package main

import (
	"embed"
	"fmt"
	"log"
)

//go:embed hello.txt
//go:embed lorem_ipsum.txt
var f embed.FS

func main() {
	data, err := f.ReadFile("lorem_ipsum.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(data))
}
```

---



```go
package main

import (
	"embed"
	"fmt"
	"log"
)

//go:embed *.txt
var f embed.FS

func main() {
	data, err := f.ReadFile("lorem_ipsum.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(data))
}
```

---



## List of "files" on virtual filesystem

```go
package main

import (
	"embed"
	"fmt"
	"log"
)

//go:embed *.txt
var f embed.FS

func main() {
	entries, err := f.ReadDir(".")
	if err != nil {
		log.Fatal(err)
	}

	for _, entry := range entries {
		fmt.Printf("%-25s  %s\n", entry.Name(), entry.Type())
	}
}
```

---

# Finito

![Game Over](images/game_over.png)

