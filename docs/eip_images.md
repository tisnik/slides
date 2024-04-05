# Enterprise Integration Patterns

---

## Používání návrhových vzorů

* Pavel Tišnovský (tisnik@centrum.cz)

![Microservices1](https://tisnik.github.io/slides/images/apache_camel_message_translator.gif)

---

## Osnova

* Vzory nejsou vynalézány, ale rozpoznávány v praxi
* Každá aplikace je odlišná
* Aplikace se postupně mění
* Komunikace v současnosti: mikroslužby a serverless řešení
* Komunikace po síti není spolehlivá
* Komunikace po síti je pomalá
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
![Microservices1](https://tisnik.github.io/slides/images/apache_camel_eip1.png)
![Microservices2](https://tisnik.github.io/slides/images/apache_camel_eip2.png)

---

## 65 vzorů

[vzory](https://www.enterpriseintegrationpatterns.com/patterns/messaging/)

---

## Nejužitečnější vzory

* Agregace dat z více zdrojů
* Broadcasting událostí
* Streaming dat
* Synchronizace dat mezi zdrojem a cílem
* Sdílení dat s externími partnery
* Dávkové zpracování dat
* Synchronní přenos (s potvrzováním)
* Asynchronní přenos (fire and forget)
* Orchestrace přenosu dat
* + kombinace předchozích

---

## Vývoj EIP

* Monolitické aplikace &rarr; mikroslužby

![Everything](https://tisnik.github.io/slides/images/everything.jpg)

---

## Mikroslužby

* Vytvářeny různými týmy
    - odlišné ekosystémy (programovací jazyk, prostředky)
    - odlišné způsoby nasazení
* Požadavky + implementace se postupně mění
* Přidávání dalších služeb
* plus další náklady
    - monitoring
    - alerting

---

## Nejsou mikroslužby vlastně SOA?

* Podobný koncept
    - znovupoužití služeb
    - kombinace služeb pro složitější úlohy
* SOA
    - většinou kód + datová integrace
    - splňují nějakou ucelenou business roli
    - typicky založeno na XML
* Mikroslužby
    - rozdělují celou aplikaci na menší celky

---

## Mikroslužby vs. SOA

* SOA (1/2)
     - spíše hrubší granularita služeb („mikromonolity“)
     - zaměření na standardizaci procesů, nástrojů atd.
     - použití ESB (Enterprise Service Bus)
     - podpora většího množství protokolů pro přenos zpráv
     - založeno na jednom programovacím jazyku a sadě knihoven
     - běh ve více vláknech

---

## Mikroslužby vs. SOA

* SOA (2/2)
     - služby dělené podle business požadavků
     - jediná databáze pro celou aplikaci
     - požadavek na změnu: úprava (mikro)monolitu

---

## Mikroslužby vs. SOA

* Mikroslužby (1/2)
     - jemnější granularita služeb
     - zaměření na spolupráci lidí a možnost svobodného výběru technologií
     - jednoduché systémy pro posílání zpráv
     - zaměření na použití jednoduchých protokolů (HTTP, STOMP, ...)
     - volnost výběru jazyka i knihoven podle potřeby
     - typicky běh v jednom vláknu s non-locking I/O, použití zelených vláken

---

## Mikroslužby vs. SOA

* Mikroslužby (2/2)
     - dělení spíše podle kontextu
     - každá mikroslužba používá vlastní datové úložiště
     - požadavek na změnu: vytvoření nové mikroslužby

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

![Smart Proxy](https://tisnik.github.io/slides/images/smart_proxy.png)

---

![Smart Proxy](https://tisnik.github.io/slides/images/smart_proxy_2.png)

---

![Smart Proxy](https://tisnik.github.io/slides/images/smart_proxy_3.png)

---

## Komunikace mezi mikroslužbami

* Komunikace po síti není spolehlivá
    - potvrzování (?)
    - distribuované transakce (?)
* Komunikace po síti je pomalá

---

## Mylné předpoklady o síti

* Síť je spolehlivá
* Zpoždění při přenosu zpráv je nulové či velmi nízké
* Přenosová kapacita je nekonečná či dostatečně vysoká
* Síť je bezpečná
* Topologie sítě se nemění
* O síť se stará pouze jeden (dohledatelný) administrátor
* Cena přenosu dat je nulová či prakticky nulová
* Síť je homogenní

---

![latency](https://tisnik.github.io/slides/images/computer_latency_1.png)

---

![latency](https://tisnik.github.io/slides/images/computer_latency_2.png)

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

![request-reply](https://tisnik.github.io/slides/images/eip_request_reply.gif)

---

## Požadavek-odpověď

![com-1](https://tisnik.github.io/slides/images/com-01-request_reply.png)

---

## Požadavek-odpověď

* často zneužíváno
    - polling
* spojení
    - stálé
    - nebo pro jedinou dvojici požadavek/odpověď

---

## Synchronní vs. asynchronní volání
---

## Oboustranná komunikace

* navázání připojení
   - typicky stálé připojení
* dvojice uzlů
* posílání zpráv oběma směry
   - přímé
   - fronty

---

## Surveyor

* poslán požadavek na odpověď
* časový limit
* v časovém intervalu jsou sbírány odpovědi
* service discovery, hlasovací algoritmy atd.

---

## Surveyor

![com-2](https://tisnik.github.io/slides/images/com-02-surveyor.png)

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
    - [C] command message
    - [D] document message
    - [E] event message
    - (request-reply messages)

![command](https://tisnik.github.io/slides/images/eip_command.gif)
![document](https://tisnik.github.io/slides/images/eip_document.gif)
![event](https://tisnik.github.io/slides/images/eip_event.gif)

---

## Komunikace využívající message brokera

![NSQ](https://tisnik.github.io/slides/images/NSQ_logo.png)

---

## Message brokeři

* ActiveMQ (Artemis)
* RabbitMQ
* IBM MQ
* Amazon SQS (broker jako služba)
* ...

---

## Message brokeři: časté problémy

* Tok dat není explicitně deklarován
* Údržba další infrastruktury
* Komplikovanější kód
* Pořadí zpráv
* Potvrzování zpráv (kdy přesně)
* At least once/at most once delivery
* Obousměrná komunikace (pub-sub atd.)!

---

## Komunikační strategie a message brokeři

---

### Publish-subscribe

![Microservices1](https://tisnik.github.io/slides/images/eip_pub_sub.gif)

---

### Publish-subscribe

![com-3](https://tisnik.github.io/slides/images/com-03-pub-sub.png)

---

### Publish-subscribe s komunikačním kanálem

![com-4](https://tisnik.github.io/slides/images/eip_pub_sub_2.gif)

---

### Message channel

![message_channel](https://tisnik.github.io/slides/images/eip_message_channel.gif)

---

### Point-to-point channel

* Pouze jeden konzument přijme zprávu

![message_channel](https://tisnik.github.io/slides/images/eip_message_channel_2.gif)

---

### Competing consumers

![message_channel](https://tisnik.github.io/slides/images/eip_competing_consumers.gif)

---

### Push-pull

![com-4](https://tisnik.github.io/slides/images/com-04-push-pull.png)

---

### Message routers

* Fan-in/fan-out lze považovat za speciální případy

![message_routers](https://tisnik.github.io/slides/images/eip_message_routers.gif)

---

### Fan-out

* RabbitMQ

![rabbit](https://tisnik.github.io/slides/images/rabbitmq2-1.png)

---

## Apache Kafka

![Kafka logo](https://tisnik.github.io/slides/images/kafka_logo.png)

---

## Apache Kafka

* Zcela nezapadá do konceptu EIP
    - kombinace několika technik
    - témata &rarr; oddíly
    - konzument &rarr; skupiny konzumentů
    - &bdquo;přehrávání&ldquo; zpráv
* Některé aspekty Kafky lze namodelovat

---

![Kafka topic](https://tisnik.github.io/slides/images/eip_kafka.png)

---

## Apache Camel

![apache](https://tisnik.github.io/slides/images/apache_camel_logo.png)

* [https://camel.apache.org/components/3.17.x/eips/enterprise-integration-patterns.html](https://camel.apache.org/components/3.17.x/eips/enterprise-integration-patterns.html)

---

![eip](https://tisnik.github.io/slides/images/eip.png)

---

## Architektura lambda

* Kombinace dávkového a proudového zpracování
* Vybalancování
    - zpoždění při zpracování
    - propustnost
    - odolnost proti chybám
* Dva pohledy na data
* Lze spojit před prezentační vrstvou

---

## Lambda: rychlá a pomalá cesta

![lambda usage](https://tisnik.github.io/slides/images/eip_lambda.png)

---


![Kafka usage](https://tisnik.github.io/slides/images/pipeline-animation.gif)

---

## Architektura kappa

* Alternativa ke klasické architektuře lambda
* Založeno na proudovém zpracování
* Lze použít i pro celé IT (nikoli jen pro zpracování dat)

---

[full image](https://tisnik.github.io/slides/images/kafka_kappa.png)
![Kafka kappa](https://tisnik.github.io/slides/images/kafka_kappa.png)

---

## Děkuji za pozornost

