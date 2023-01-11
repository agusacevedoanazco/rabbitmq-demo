---
title: Message Queues
author: Agustin Acevedo
date: January 11, 2023
tags: [message queues, basics, fundamentals, microservices]
---

# Message queues

## Basic prerequisites

- Networking
- Distributed systems
- Asynchronous communication
- Data persistence
- Messaging patterns
- Concurrency and paralelism
- Reliability and fault tolerance

## The goal "Microservices"

Microservices are a software architecture pattern in which a large application is built as a collection of small, independent services. Each service is responsible for a specific function or capability, and communicates with other services as needed to perform its tasks.

One of the main benefits of using microservices is that they can make it easier to build and maintain large, complex applications. Since each service is independent and has a narrowly defined scope, it can be developed and deployed separately from the rest of the application. This can make it easier to scale and update the application, as it is possible to make changes to one service without affecting the others.

Microservices can also be more resilient to failures, as the failure of one service can often be isolated and does not necessarily affect the rest of the application. This can make it easier to ensure that the application is available and reliable, even in the face of issues such as hardware failures or network outages.

However, building and maintaining a microservices architecture can also be more complex than using a more monolithic approach, as it requires more coordination and integration between the different services. It can also be more difficult to debug issues and understand the overall behavior of the system, as it may be necessary to look at multiple services in order to understand how a particular feature or capability is implemented.

## Messaging patterns

There are several common patterns that are used when exchanging messages between systems. Here are a few examples:

- Request/response: In this pattern, one system sends a request message to another system, and the recipient responds with a response message. This is the most basic form of message exchange, and is often used when one system needs to request a specific piece of data or perform a specific task.
- Publish/subscribe: In this pattern, one system publishes a message to a specific topic or channel, and other systems that are subscribed to that topic or channel receive the message. This is a useful pattern for distributing messages to multiple recipients, or for allowing systems to selectively receive messages that are relevant to them.
- Message-oriented middleware: This pattern involves the use of specialized software, known as a message broker, to route messages between systems. The message broker acts as an intermediary between the sender and recipient, and can be used to implement a variety of messaging patterns and provide additional features such as reliability and message persistence.
- Point-to-point: In this pattern, a message is sent from a sender to a specific recipient, and is not intended to be received by any other system. This is a simple and direct form of messaging, and is often used when the sender and recipient have a direct relationship or when the message is specific to a particular system.

There are many other messaging patterns in addition to these, and which pattern is best to use will depend on the specific requirements of the systems and the nature of the messages being exchanged.

### Message patterns considerations

- Event-driven architecture: This is a design pattern that involves the use of message queues to trigger events in a system. For example, an application might publish a message to a message queue when a user performs a specific action, and a separate service might listen for those messages and trigger a process in response. This can be a useful way to decouple different parts of a system and enable them to evolve independently.
- Message durability: In some cases, it may be important to ensure that messages are not lost if a system or network failure occurs. Message queues can be configured to provide durability by storing messages on disk or in a database, rather than just in memory. This can help to ensure that messages are delivered even if a failure occurs.
- Message ordering: Depending on the needs of the system, it may be important to ensure that messages are delivered in a specific order. Message queues can often be configured to preserve message order, either globally or within specific groups of messages.
- Performance and scalability: When designing a system that uses message queues, it is important to consider the performance and scalability requirements of the system. This can involve optimizing the design of the message queues and the systems that use them, and using strategies such as message batching or parallel processing to improve performance.

## Message queues basics

Message queues are a type of software that enable the exchange of messages between microservices, or between different systems in a distributed architecture. They provide a way for microservices to communicate with each other asynchronously, without the need for each service to be constantly polling for new messages or waiting for a response.

One of the main benefits of using message queues in a microservices architecture is that they allow for loose coupling between services. This means that each service can be developed and deployed independently, without the need for the other services to be available or even aware of its existence. This can make it easier to scale and maintain the system, as it is possible to make changes to one service without affecting the others.

Message queues also provide a level of reliability and fault tolerance, as they can store messages that need to be delivered even if the recipient is temporarily unavailable. This can be especially useful in distributed systems where network failures or other issues may cause communication to be disrupted.

In summary, message queues can be a powerful tool for enabling communication between microservices and building scalable, resilient distributed systems.

### Pros and cons

#### Pros:

- Asynchronous communication: Message queues allow for asynchronous communication between systems, which can improve the performance and scalability of the system.
- Loose coupling: Message queues can help to decouple systems and allow them to evolve independently, which can make it easier to scale and maintain the system.
- Reliability: Message queues can provide reliability by storing messages that need to be delivered, even if the recipient is temporarily unavailable.
- Flexibility: Message queues can support a variety of messaging patterns and can be used to implement a wide range of communication scenarios.

#### Cons:

- Complexity: Implementing and maintaining a message queueing system can be more complex than using other types of communication, such as HTTP APIs or database updates.
- Performance: In some cases, message queueing may not be as efficient as other types of communication, especially if the messages are small or the system has high performance requirements.
- Error handling: Message queues can introduce additional complexity when it comes to error handling and retry logic, as it may be necessary to handle cases where messages cannot be delivered or processed.
- Visibility: It can be more difficult to see the overall state of the system when using message queues, as messages may be in transit or stored temporarily before being delivered. This can make it harder to troubleshoot issues or understand how the system is functioning.

### Alternatives for loosely coupled systems

- Remote procedure calls (RPC): This is a method of communication between services in which one service can invoke a method on another service as if it were a local object. This can be a simple way to invoke functionality on a remote service, but can be less flexible than message queues and may be less suitable for scenarios where the services are distributed over a wide area or are subject to intermittent failures.
- HTTP APIs: Services can also communicate with each other using HTTP APIs, which allows them to exchange data over the web using standard HTTP methods such as GET, POST, and PUT. This can be a simple and flexible way to expose functionality to other services, but can be less efficient than message queues and may require more complex error handling and retry logic.
- Databases: In some cases, services may communicate with each other by reading and writing data to a shared database. This can be a simple way to share data between services, but can be less flexible than message queues and may be more difficult to scale.
- Synchronous communication: Another option is to use synchronous communication between services, in which one service blocks and waits for a response from the other service before continuing. This can be a simple approach, but can be less resilient to failures and may not be suitable for scenarios where the services are distributed or have high latencies.

## Message queues services

Some of the most popular message queueing services include:

- RabbitMQ: This is an open-source message broker that is widely used and supports a variety of messaging patterns and protocols. It can be installed on-premises or in a cloud environment.
- Apache Kafka: This is an open-source distributed messaging system that is designed for high performance and scalability. It is often used for streaming data and real-time processing applications.
- Amazon Simple Queue Service (SQS): This is a fully-managed message queueing service provided by Amazon Web Services (AWS). It is designed to be easy to use and provides features such as message durability and automatic scaling.
- Google Cloud Pub/Sub: This is a fully-managed message queueing service provided by Google Cloud Platform. It is designed for high performance and reliability, and can automatically scale to meet demand.
- Microsoft Azure Service Bus: This is a message queueing service provided by Microsoft Azure that supports a variety of messaging patterns and can be used to build scalable, reliable distributed systems.

### GCP Pub/Sub vs RabbitMQ (Cloud Engineer hypocrite)

Google Cloud Pub/Sub is a fully-managed message queueing service provided by Google Cloud Platform, while RabbitMQ is an open-source message broker software that can be installed and run on-premises or in a cloud environment.

One key difference between the two is the level of control and customization that is available. With Google Cloud Pub/Sub, you can create and publish messages to topics and subscribe to those topics to receive messages, but you do not have access to the underlying infrastructure or the ability to customize the behavior of the message broker. With RabbitMQ, on the other hand, you have more control over the configuration and operation of the message broker, including the ability to use different messaging patterns and plugins to extend its functionality.

Another difference is the level of scalability and reliability that is provided. Google Cloud Pub/Sub is designed to handle very high volumes of messages and can automatically scale to meet demand. It also provides built-in features such as message persistence and automatic retries to ensure the reliability of message delivery. RabbitMQ can also handle high volumes of messages, but may require more manual configuration and management to achieve the same level of scalability and reliability.

Ultimately, the choice between the two will depend on your specific needs and requirements, including whether you need a fully-managed solution or more control over the message broker, and whether you need high levels of scalability and reliability.

As a developer, i like the idea to develop with a tool in my machine and then exactly the same technology use it as a cloud service

## RabbitMQ

RabbitMQ is a message broker software that allows applications to communicate with each other by sending and receiving messages. The message broker acts as a middleman for these communications, allowing the sender and receiver to be decoupled from one another and improving the overall scalability and reliability of the system.

RabbitMQ is based on the Advanced Message Queuing Protocol (AMQP) and supports a wide range of programming languages and platforms, including Java, C#, Python, Ruby, and more. It also has a rich set of features, such as reliable message delivery, routing, and high availability, that make it well-suited for building large, complex, and distributed systems.

One of the key features of RabbitMQ is its support for message queues, which are used to temporarily store messages that are sent between applications. This allows the sender and receiver to operate at different rates, and ensures that messages are not lost if the receiver is temporarily unavailable.

Additionally, RabbitMQ provides a number of mechanisms for routing and filtering messages, including direct, fanout, topic, and headers exchanges, which can be used to send messages to specific recipients based on the contents of the message or other criteria.

RabbitMQ is an open-source software, can be deployed in various ways, such as on-premises, Cloud and Containerization. it is often used as a foundation for building systems that need to process large numbers of messages in parallel, such as real-time data pipelines, stream processing systems, and more.

### About the AMQP protocol

Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for message-oriented middleware. The protocol defines a binary wire-level protocol, which is platform independent and can be implemented in many programming languages.

AMQP provides a standard way for applications to communicate with a message broker, which acts as a middleman for the communication. With AMQP, a sender application can send messages to the broker, and the broker can then route those messages to one or more receiver applications.

One of the key features of AMQP is its support for message queues, which are used to temporarily store messages that are sent between applications. This allows the sender and receiver to operate at different rates, and ensures that messages are not lost if the receiver is temporarily unavailable.

AMQP also provides a number of features for routing and filtering messages, such as:

-   Direct message routing: where messages are routed to a specific queue, based on a routing key.
-   Topic-based message routing: where messages are routed to one or more queues based on a pattern-matching rule.
-   Fanout message routing: where messages are broadcast to all queues that are bound to an exchange
-   Headers-based message routing: where messages are routed based on headers, rather than routing keys

AMQP also provides other features like:

-   Quality of Service(QoS) for messaging
-   Error Handling
-   Security
-   Transactions

AMQP is designed to be a high-performance, high-throughput protocol that can handle large numbers of messages with low overhead. It is widely supported across different platforms and programming languages, and is often used in financial, healthcare and IoT applications where messaging is a critical part of the infrastructure. RabbitMQ is one of the most popular message brokers that implement the AMQP protocol.

### Supported Platforms

RabbitMQ is a cross-platform message broker that can run on a variety of operating systems and platforms, including:

-   Windows: RabbitMQ can be installed as a service on Windows systems and run as a background process.
-   Linux: RabbitMQ can be installed on a wide variety of Linux distributions, including Debian, Ubuntu, CentOS, and more. It can be run as a background service using systemd or other init systems.
-   Mac OS: RabbitMQ can be installed on Mac OS systems using Homebrew or MacPorts package managers.
-   Cloud Platforms: RabbitMQ can be deployed on various cloud platforms like AWS, Azure, GCP and can be run on virtual machines, containers or using managed services like AWS MQ, Azure Event Hub, GCP Cloud Pub/Sub
-   Containerization: RabbitMQ can be deployed in containerized environments using popular container orchestration systems such as Kubernetes, Docker Compose, and more.

RabbitMQ also provides clients libraries for multiple programming languages, including:

-   Java
-   .NET
-   C
-   C++
-   Python
-   Ruby
-   JavaScript
-   PHP
-   Perl
-   Go
-   and many more

This makes it easy to integrate RabbitMQ into a wide variety of systems and applications, regardless of the platform or programming language that you are using.

Additionally, RabbitMQ can be managed and monitored with a variety of tools like the management UI built into RabbitMQ, through command line interface and programmatically through HTTP API calls.