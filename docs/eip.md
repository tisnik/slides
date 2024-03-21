# Enterprise Integration Patterns

## Používání návrhových vzorů

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

## Návrhové vzory pro enterprise systémy

* Enterprise systém založený na mikroslužbách
* Používá se relativně malá sada ustálených způsobů
    - vzorů
* Vzory nejsou vynalézány, ale rozpoznávány v praxi
* Standardizace
    - slovní popis
    - grafická podoba
* Snaha vyhnout se slepým uličkám
    - ty již někdo prozkoumal za nás
    - (a zaplatil za to)

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

![com-3](images/com-03-pub-sub.png)

---

### Push-pull

![com-4](images/com-04-push-pull.png)

---

## Apache Kafka

---

---

## Architektura lambda

---

## Architektura kappa
