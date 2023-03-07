# Apache Kafka

![Kafka logo](images/kafka_logo.png)

---

"Every enterprise is powered by data"

---

## Multifaceted Apache Kafka

* scalable real-time messaging platform
    - able to process millions of messages per second
* event streaming platform for massive volumes of big data analytics
* distributed storage
    - with support for replayability of events
    - and with guaranteed ordering
* data integration framework for streaming ETL
* data processing framework
    - continuous stateless or stateful stream processing

---

## Kafka in not:

* proxy for millions of clients
    - like mobile apps
* API Management platform
* database for complex queries and batch analytics workloads
    - simple aggregations possible thanks to ksqlDB
* IoT platform with features such as device management
* technology for hard real-time applications
    - safety-critical systems
    - deterministic systems

---

## Typical usage of Kafka

* Message broker on steroids
* Central part of Lambda architecture
* Central part of Kappa architecture
* Logging platform
* ETL with capability to "replay" data

---

### Kafka streams

![Kafka streams](images/kafka_streams.png)

---

### Source of truth

[full image](images/kafka_kappa.png)
![Kafka kappa](images/kafka_kappa.png)

---

### Kafka: Message broker on steroids

---

### Message brokers

* Classic ones
   - ActiveMQ (Artemis)
   - RabbitMQ
   - IBM MQ
   - etc.

---

### Why message brokers?

![Without broker](images/kafka_without_broker.png)

---

### Why message brokers?

![With broker](images/kafka_with_broker.png)

---

### Message brokers: communication strategies

* Enterprise integration patterns (EIP)

---

### Request reply

![com-1](images/com-01-request_reply.png)

---

### Surveyor

![com-2](images/com-02-surveyor.png)

---

### Pub-sub

![com-3](images/com-03-pub-sub.png)

---

### Push-pull

![com-4](images/com-04-push-pull.png)

---

### Push-pull with messages redistribution

![com-5](images/com-05-push-pull.png)

---

### Push-pull with reply to producer

![com-6](images/com-06-push-pull-reply.png)

---

### Other strategies (NATS etc.)

![com-7](images/com-07-req-pull.png)

---

## Microservices

* Apache Kafka is sometimes used as a key component in microservice-based architectures
* "Design the organisation you want, the architecture will follow (kicking and screaming)"

---

### Classic architecture

* Front-end
* Back-end
    - business logic
    - data layer
* Storage

![Microservices1](images/microservices1.png)

---

### Stateless and stateful microservices

* Services w/o state
    - super easy to test
    - usually very easy to scale up
    - restarts are usually not a big deal
* Stateful service
    - the opposite is true

---

[Full image](images/microservices2.png)
![Microservices2](images/microservices2.png)

---

## Basic concepts

* Message
    - also called event
* Topic
    - a named log of events
* Producer
    - sends messages/events into selected topic
* Consumer
    - retrieves messages/events from selected topic

---

### Producer and consumer

![ProducerConsumer1](images/kafka1.png)

---

### More producers and consumers

![ProducerConsumer2](images/kafka2.png)

---

### Messages in Kafka

* Array of bytes
    - no prior knowledge about format
* Optional key
* Batch(es)
    - multiple messages for the same topic+partition
    - written as one block
    - efficiency

---

### Topics and partitions

* Messages are categorized into topics
* Topic is splitted into partitions

---

## Append-only log

* new mesage/event is always written on the end of topic
* messages/events are immutable
* can be read by
    - seeking and arbitrary offset
    - sequential scanning

---

## Three basic operations

* Producer
    - produce (send) message to given topic
* Consumer
    - rewind (seek) to message X
    - consume message + update offset

---

## Topic is NOT a queue

* Topic is basically stateless
    - consumers have to maintain their state
    - by storing their offsets "somewhere"
* Message is not deleted after consumption
    - just messages past the retention period are deleted
* FIFO model is not followed

---

## Key features

* Scalability
* Reliability
* Log compaction

---

## Scalability

* Topic can be partitioned
    - across different servers
    - consumers can consume messages paralelly

---

## Reliability

* Replication
* Changing leadership role

---

## Topic with one partition only

```
+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...
+---+---+---+---+---+---+---+---+---+
                ^                        ^
                |                        |
              read                     write
```

---

## Kafka technology is much more difficult though

* Partitions
* Multiple replicas per partition
* Sharding

---

### Multiple partitions for one topic

```
              +---+---+---+---+---+---+
partition #0  | 0 | 1 | 2 | 3 | 4 | 5 | ...
              +---+---+---+---+---+---+
partition #1  | 0 | 1 | 2 | ...
              +---+---+---+
partition #2  | ...
              +---+---+---+---+---+---+---+---+---+
partition #3  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...
              +---+---+---+---+---+---+---+---+---+
```

---

### Multiple replicas per partition

```
                                     write
                                       |
+---+---+---+---+---+---+---+---+---+  v
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...    (leader)
+---+---+---+---+---+---+---+---+---+
                  ^               ^
                read              |
                                 sync
                                  |
                                  v
+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |        (follower)
+---+---+---+---+---+---+---+---+---+
                                  ^
                                  |
                                 sync
                                  |
                                  v
+---+---+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |        (follower)
+---+---+---+---+---+---+---+---+---+
```

---

### Multiple replicas for partitioned topic

```
              +---+---+---+---+---+---+
partition #0  | 0 | 1 | 2 | 3 | 4 | 5 | ...
              +---+---+---+---+---+---+
partition #1  | 0 | 1 | 2 | ...
              +---+---+---+                               (leader)
partition #2  | ...
              +---+---+---+---+---+---+---+---+---+
partition #3  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...
              +---+---+---+---+---+---+---+---+---+
                                      ^
                                      |
                                     sync
                                      |
                                      v
              +---+---+---+---+---+---+
partition #0  | 0 | 1 | 2 | 3 | 4 | 5 | ...
              +---+---+---+---+---+---+
partition #1  | 0 | 1 | 2 | ...
              +---+---+---+
partition #2  | ...                                       (follower)
              +---+---+---+---+---+---+---+---+---+
partition #3  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...
              +---+---+---+---+---+---+---+---+---+
                                      ^
                                      |
                                     sync
                                      |
                                      v
              +---+---+---+---+---+---+
partition #0  | 0 | 1 | 2 | 3 | 4 | 5 | ...
              +---+---+---+---+---+---+
partition #1  | 0 | 1 | 2 | ...
              +---+---+---+
partition #2  | ...                                       (follower)
              +---+---+---+---+---+---+---+---+---+
partition #3  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...
              +---+---+---+---+---+---+---+---+---+
```


---

## Log compaction

* Keeps the latest known value for each record key
* Preserves the most recent version of a record during deletion

---

## Consumer groups, clusters, multiple brokers

* Consumer groups
    - at most one consumer per partition
    - scalability
* Clusters
    - one broker is controller
    - elected automatically
    - assigning partitions
    - monitoring broker failures

---

## Consumer groups, clusters, multiple brokers

* Partition can be assigned to more brokers
    - replication
    - redundancy
    - can survive broker(s) failure

---

### Retention

* Retention policy
    - setup globally
    - and possible to setup for topic
    - retention limits are minimum guarantees

```
log.retention.hours
log.retention.bytes
log.segment.bytes
log.retention.check.interval.ms
log.roll.hours
```

---

## Kafkacat (kcat)

```
kafkacat -L -b localhost:9092
kafkacat -P -b localhost:9092 -t "upload"
kafkacat -P -b localhost:9092 -t filedrop -p 0 file1.bin file2.txt /etc/motd dalsi_soubor.tgz
kafkacat -C -b localhost:9092 -t "upload"
kafkacat -C -b localhost:9092 -t topic1 -p 0 -o -1000 -e
kafkacat -b localhost:9092 -G skupina_konzumentů topic1
kafkacat -b localhost:9092 -G skupina_konzumentů téma1 téma2
```

---

## Clients for Apache Kafka

* [Supported languages/ecosystems](https://cwiki.apache.org/confluence/display/KAFKA/Clients)
    - C/C++
    - Python
    - Go (AKA golang)
    - Erlang
    - PowerShell
    - .NET
    - Ruby
    - Node.js
    - Proxy (HTTP REST, etc)
    - Perl
    - stdin/stdout
    - PHP
    - Rust
    - Alternative Java
    - Storm
    - Scala DSL 
    - Clojure
    - Swift

---

## Kafka connect


* "Distributed scalable framework"
* Automatic consuming or producing data
    - with data persistence in-between
* Part of Apache Kafka
* Just configuration files
* And connectors

---

## Kafka Connect components

* Sources
* Kafka Cluster
* Sinks

---

## Kafka Connect use cases

---

### Moving data from one DB to another one

![Kafka_Connector_1](images/kafka_connect_1.png)

---

### Connection between MQTT and AWS SQS

![Kafka_Connector_2](images/kafka_connect_2.png)

---

### From one source to various sinks

* Amazon S3
* Logs
* Storage (database)

![Kafka_Connector_3](images/kafka_connect_3.png)

---

#### Custom consumers are possible

* Amazon S3
* Logs
* Storage (database)
* And bunch of custom consumers

![Kafka_Connector_4](images/kafka_connect_4.png)

---

## Kafka Connect from developers PoV

* Is separate process
* It requires no programming
    - failures handling
    - logging
    - monitoring
    - scaling
    - migrating
    - sec. handling etc.

---

## Kafka Connect from developers PoV (cont.)

* Lightweight data transformations
* Sometimes defined by one simple property file

---
