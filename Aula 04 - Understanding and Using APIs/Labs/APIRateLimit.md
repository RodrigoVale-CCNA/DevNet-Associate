# API Rate Limiting Algorithms

Rate limiting is crucial for maintaining the availability, responsiveness, and security of web services and APIs. By controlling the frequency of requests from users or applications, service providers can ensure fair usage, optimal performance, and safeguard against potential attacks. Different algorithms offer various ways to implement rate limiting based on specific needs.

## 1. **Token Bucket**

The **Token Bucket** algorithm adds tokens to a bucket at a fixed rate. Tokens represent permission to perform some actions. If the bucket runs out of tokens, further requests are denied until more tokens are added. This method allows for short bursts of requests up to the bucket size.

## 2. **Leaky Bucket**

The **Leaky Bucket** algorithm processes incoming requests at a steady, configurable rate. If incoming requests fill the bucket faster than it can be emptied, subsequent requests are discarded or leaked, hence the name.

## 3. **Fixed Window**

The **Fixed Window** approach divides time into fixed windows, for example, one minute. Each user gets a certain number of allowed requests within this window. The counter resets after each window, regardless of when the first request was made.

## 4. **Sliding Log**

**Sliding Log** keeps track of the timestamp of each request. When a new request comes in, it counts the number of requests within the current window, ensuring that rate limits are applied in real-time.

## 5. **Sliding Window**

A hybrid of the Fixed Window and Sliding Log, the **Sliding Window** algorithm uses a fixed window size but evaluates in real-time, ensuring a more uniform distribution of requests.

## 6. **GCRA (Generic Cell Rate Algorithm)**

**GCRA** is a refinement of the Token Bucket approach. It's often employed in telecommunications for traffic shaping and rate limiting. It uses a mathematical approach to ensure a steady rate without the need to store too much state.

## 7. **Cost-based Rate Limiting**

Instead of merely counting requests, **Cost-based Rate Limiting** assigns a cost to each API call, which is then deducted from the user's allocated quota. This ensures that heavier API calls have a greater impact on the rate limit.

## 8. **Concurrent Connections**

Rather than limiting based on the number of requests over time, **Concurrent Connections** limits based on the number of simultaneous connections from a user or application.

---

Each algorithm has its advantages and suits different scenarios. It's essential to understand the specific needs and traffic patterns of your service to choose the most appropriate rate limiting strategy.