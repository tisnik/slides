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

---

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

---

#### MBean export

```java
import java.util.Scanner;

import javax.management.*;
import java.lang.management.ManagementFactory;

public class Main {
   public static void main(String[] args) {
       try {
           String programName = (args.length == 0) ? "foobar" : args[0];

           StatusMBean systemStatus = new Status(programName);

           MBeanServer platformMBeanServer = ManagementFactory.getPlatformMBeanServer();
           ObjectName objectName = new ObjectName("cz.root.app:name=StatusExample");
           platformMBeanServer.registerMBean(systemStatus, objectName);

       } catch (Exception e) {
           e.printStackTrace();
       }

       new Scanner(System.in).nextLine();
   }
}
```

---

#### Example of **jconsole** usage

(live)

---

#### JMX can be used to *control* applications as well

* MBean definition via interface named `xxxMBean`:

```java
public interface StatusMBean {
    Integer getAnswer();
    Long getCounter();
    String getProgramName();
    Boolean getSwitchStatus();
    void setSwitchStatus(Boolean newStatus);
    void flipSwitchStatus();
}
```

---

#### Interface implementation

```java
public class Status implements StatusMBean {
   private Integer answer;
   private String programName;
   private Boolean switchStatus;
   private Long counter;

   public Status(String programName) {
       this.answer = 42;
       this.programName = programName;
       this.switchStatus = false;
       this.counter = 0L;
   }
   
   @Override
   public Integer getAnswer() {
       return this.answer;
   }

   @Override
   public Long getCounter() {
       this.counter++;
       return this.counter;
   }

   @Override
   public String getProgramName() {
       return this.programName;
   }

   @Override
   public Boolean getSwitchStatus() {
       return switchStatus;
   }

   @Override
   public void setSwitchStatus(Boolean newStatus) {
       this.switchStatus = newStatus;
   }

   @Override
   public void flipSwitchStatus() {
       System.out.println("Flip switch status called!");
       this.switchStatus = !this.switchStatus;
   }
}
```

