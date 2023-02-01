# Apache Kafka

![Kafka logo](images/kafka_logo.png)

---



## Usage of Kafka

* Message broker on steroids
* Lambda architecture
* Kappa architecture
* Logging platform

![Kafka streams](images/kafka_streams.png)

![Kafka kappa](images/kafka_kappa.png)



---

## Microservices

* Apache Kafka is sometimes key component in microservice-based architectures



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

![Microservices2](images/microservices2.png)
---



### Communication between stateful microservices

* Not as easy as it might seem
    - "compound" transactions
    - should one service synchronously wait for second one?

![Microservices3](images/microservices3.png)
---



### Compensation transactions

* One possible solution

![Microservices4](images/microservices4.png)
---



### Apache Kafka as source of events

![Microservices5](images/microservices5.png)
---



### Apache Kafka as message broker

![Microservices6](images/microservices6.png)
---



### Kappa architecture
![Microservices7](images/microservices7.png)



---

## Monitoring

### JMX

* Java Management Extensions
* Standard in Java world for a long time
* Ability to monitor **any** JVM-based application
* Metrics etc. available through *MBeans*
* Standard tool named **jconsole**

(example of **jconsole** usage)



---

### Simple example of custom MBeans

#### MBean definition via interface named `xxxMBean`:

```java
public interface StatusMBean {
    Integer getAnswer();
    String getProgramName();
    Boolean getSwitchStatus();
}
```

#### Interface implementation:

```java
public class Status implements StatusMBean {
   private Integer answer;
   private String programName;
   private Boolean switchStatus;

   public Status(String programName) {
       this.answer = 42;
       this.programName = programName;
       this.switchStatus = false;
   }
   
   @Override
   public Integer getAnswer() {
       return this.answer;
   }

   @Override
   public String getProgramName() {
       return this.programName;
   }

   @Override
   public Boolean getSwitchStatus() {
       return switchStatus;
   }
}
```

