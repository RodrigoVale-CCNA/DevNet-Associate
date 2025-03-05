# REST (Representational State Transfer)

## Overview

REST, which stands for Representational State Transfer, is an architectural style for distributed systems. It's often used in the development of web services and provides a standardized way for systems to communicate over the internet.

## Key Characteristics of REST

- **Statelessness**: Each request is independent; server responses do not depend on the stored state. Every necessary piece of information should be provided by the client within each request.

- **Client-Server Architecture**: There's a clear separation of concerns. The client handles the user interface and user experience, whereas the server focuses on data logic and persistence.

- **Cacheable**: Server responses can be marked as cacheable or non-cacheable. This lets clients store response copies, enhancing performance and minimizing server-client interactions.

- **Uniform Interface**: Ensures consistency and simplicity. Resources are identified through URLs and are interacted with using standard HTTP methods (GET, POST, PUT, DELETE).

- **Layered System**: Clients directly interact with the nearest layer without needing awareness of subsequent layers, aiding in scalability and modularity.

- **Communication Based on Representations**: Resources can have one or more representations (e.g., JSON, XML), and clients interact with these representations.

## Comparing REST with RESTful

While REST is an architectural style with a set of guidelines and best practices, a RESTful application or service is one that implements these REST principles rigorously. Here are some notes comparing the two:

- **Implementation**: When an application or service is termed RESTful, it means it's an implementation that adheres to the principles of REST.

- **Consistency**: RESTful APIs maintain a uniform and consistent interface, which is one of the guiding principles of REST.

- **Interactivity**: REST is more about the guidelines, while RESTful services provide a way to interact using these guidelines.

- **Popularity**: Many modern APIs claim to be RESTful, showcasing their adherence to the REST architecture. It's a testament to the popularity and robustness of REST as a design choice.

In essence, while REST provides the rules, RESTful is the practical application of those rules.