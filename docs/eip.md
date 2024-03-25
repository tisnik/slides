# Enterprise Integration Patterns

---

## Používání návrhových vzorů

![Microservices1](images/apache_camel_message_translator.gif)

---

## Osnova

* Vzory nejsou vynalézány, ale rozpoznávány v praxi
* Komunikace po síti není spolehlivá
* Komunikace po síti je pomalá
* Každá aplikace je odlišná
* Aplikace se postupně mění
* Komunikace v současnosti: mikroslužby a serverless řešení
* Architektura založená na mikroslužbách
* Příklady řešení komunikace ve světě mikroslužeb

---

## Návrhové vzory pro enterprise systémy (1/2)

* Enterprise systém založený na mikroslužbách
* Používá se relativně malá sada ustálených způsobů
    - vzorů
* Vzory nejsou vynalézány, ale rozpoznávány v praxi
* Standardizace
    - slovní popis (slovník)
    - grafická podoba

---

## Návrhové vzory pro enterprise systémy (2/2)

* Snaha vyhnout se slepým uličkám
    - ty již někdo prozkoumal za nás
    - (a zaplatil za to)

---

## Standardizace - slovník

* Message
* Message bus
* Dead letter channel
* Pipe
* Filter
* Message router
* Guaranteed Delivery
* ...

---

## Standardizace - grafika
![Microservices1](images/apache_camel_eip1.png)
![Microservices2](images/apache_camel_eip2.png)

---

## Mikroslužby

* Vytvářeny různými týmy
    - odlišné ekosystémy (programovací jazyk, prostředky)
    - odlišné způsoby nasazení
* Požadavky + implementace se postupně mění
* Přidávání dalších služeb
* + další náklady
    - monitoring
    - alerting

---

## Komunikace mezi mikroslužbami

* Koordinace mezi mikroslužbami
* Komunikace mezi mikroslužbami
* Typicky řešeno posíláním zpráv
    - informace o událostech
    - příkazy
    - dotazy
* Synchronní či asynchronní zpracování
* Distribuované transakce

---

## Komunikační strategie

* Ad-hoc
* Bez nutnosti použití message brokera
* S použitím message brokera
* Využití dalších technologií
    - sběrnice
    - streaming

---

## Komunikace bez message brokera

---

## Požadavek-odpověď

![request-reply](images/eip_request_reply.gif)

---

## Požadavek-odpověď

![com-1](images/com-01-request_reply.png)

---

## Požadavek-odpověď

* často zneužíváno
    - polling
* spojení
    - stálé
    - nebo pro jedinou dvojici požadavek/odpověď

---

## Oboustranná komunikace

* navázání připojení
   - typicky stálé připojení
* dvojice uzlů
* posílání zpráv oběma směry

---

## Surveyor

* poslán požadavek na odpověď
* časový limit
* v časovém intervalu jsou sbírány odpovědi
* service discovery, hlasovací algoritmy atd.

---

## Surveyor

![com-2](images/com-02-surveyor.png)

---

## CQS a CQRS

* Command–query separation (CQS)
* Command-query responsibility segregation (CQRS)
    - COMMAND
    - EVENT
    - QUERY

---

## CQS a CQRS

* V EIP:
    - command message
    - document message
    - event message
    - (request-reply messages)

![command](images/eip_command.gif)
![document](images/eip_document.gif)
![event](images/eip_event.gif)

---

## Komunikace využívající message brokera

![NSQ](images/NSQ_logo.png)

---

## Message brokeři

* ActiveMQ (Artemis)
* RabbitMQ
* IBM MQ
* Amazon SQS (broker jako služba)
* ...

---

## Komunikační strategie a message brokeři

---

### Publish-subscribe

![Microservices1](images/eip_pub_sub.gif)

---

### Publish-subscribe

![com-3](images/com-03-pub-sub.png)

---

### Message channel

![message_channel](images/eip_message_channel.gif)

---

### Point-to-point channel

* Only one receiver consume message

![message_channel](images/eip_message_channel_2.gif)

---

### Push-pull

![com-4](images/com-04-push-pull.png)

---

## Apache Kafka

![Kafka logo](images/kafka_logo.png)

---

![Kafka topic](images/eip_kafka.png)

---


## Apache Camel

![apache](images/apache_camel_logo.png)

* [https://camel.apache.org/components/3.17.x/eips/enterprise-integration-patterns.html](https://camel.apache.org/components/3.17.x/eips/enterprise-integration-patterns.html)

---

![eip](images/eip.png)

---

## Architektura lambda

---

## Architektura kappa
