# An Overview of HTTP

## Introduction
In today’s interconnected world, exchanging information between devices is crucial. But how do we achieve that? The **HTTP protocol** is the answer.

For a more detailed explanation, you can refer to the [MDN Web Docs - HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview).

## What is HTTP?
HTTP (Hypertext Transfer Protocol) is the cornerstone of data communication on the Web. It’s a protocol designed to fetch resources like HTML documents and forms the basis for most data exchanges on the internet.

![Fetching a Page from Web Server](images/fetching-a-page.svg)

## How Does HTTP Work?
HTTP operates as a **client-server protocol**. This means that requests are initiated by the client—typically a web browser—and the server responds with the requested resources. A complete document is often assembled from various resources, such as HTML files, CSS files, images, and more.

Communication between clients and servers occurs through the exchange of individual messages, not continuous data streams. The client sends **requests**, and the server replies with **responses**.

![HTTP Layers](images/http-layers.svg)

HTTP works at the application layer and is transmitted over the Transmission Control Protocol (TCP).

## Components of an HTTP-Based System
HTTP-based systems use a client-server architecture. The key components include:

- **Client:** The entity initiating the requests, often a user-agent like a web browser or a proxy.
- **Server:** The entity handling the requests and returning the responses.
- **Proxies:** Intermediary entities between the client and server, performing operations like caching or acting as gateways to improve performance and security.

![Client Server Chain](images/client-server-chain.svg)

## HTTP Messages
HTTP messages are structured within a binary frame, which allows for optimizations like header compression and multiplexing.

### Request Messages
A request message consists of several components:

![Request Message](images/http-request.svg)

- **HTTP Method:** Defines the action the user wants to perform (e.g., GET, POST).
- **Resource Path:** Specifies the location of the resource to fetch.
- **HTTP Version:** Indicates the version of the HTTP protocol being used.
- **Headers:** Optional fields that provide additional information for the server.
- **Body:** Used in methods like `POST` to include data with the request.

### Response Messages
A response message is structured as follows:

![Response Message](images/http-response.svg)

- **HTTP Version:** Indicates the version of the HTTP protocol used in the response.
- **Status Code:** Shows whether the request was successful or not, along with the reason.
- **Status Message:** A short, non-authoritative description of the status code.
- **Headers:** Similar to request headers, these provide additional information.
- **Body:** Optionally contains the requested resource or error message.

## Summary
HTTP is a vital protocol enabling web communication by facilitating the exchange of messages between clients and servers. Understanding its components and how it works is essential to grasping the fundamentals of web interactions.
