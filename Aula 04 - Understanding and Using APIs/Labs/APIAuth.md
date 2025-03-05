# API Authorization Mechanisms

When designing secure and efficient APIs, it's vital to ensure that the right users have the correct level of access to resources. Authorization mechanisms play a pivotal role in achieving this. Below are some widely recognized authorization methods:

## 1. JWT (JSON Web Token)
- A compact and self-contained way to represent information exchanged between two parties.
- Widely used in Single Sign-On (SSO) systems.
- Can be signed and encrypted to enhance data's security and integrity.

## 2. RBAC (Role-Based Access Control)
- Authorization is based on the user's role within the system.
- Access rights are assigned to roles, not individual users.

## 3. ABAC (Attribute-Based Access Control)
- Authorization decisions are based on user, environment, resource attributes, etc.
- Offers more granular and dynamic access control than RBAC.

## 4. API Gateway
- Solutions like AWS API Gateway, Kong, and others provide authorization capabilities.
- Allows specific access policies for your APIs to be defined and enforced.

## 5. MAC (Mandatory Access Control)
- Authorization is centralized and enforced by a central authority.
- Users are not allowed to set or change policies; only administrators can.

## 6. SAML (Security Assertion Markup Language)
- A standard for exchanging authentication and authorization data between parties.
- Mainly used for Single Sign-On authentication.

## 7. OAuth
- Combines authentication with authorization.
- Developed as a response to insecure authentication mechanisms.
- Offers enhanced security compared to other options.
- Exists in two versions: OAuth 1.0 and OAuth 2.0. Note that OAuth 2.0 isn't backward compatible.
- The OAuth 2.0 authorization framework enables a third-party app to gain limited access to an HTTP service.
- Involves obtaining an access token from an authorization server [Identity Provider (IdP) or an Identity Service (IdS)] which is then shared with the application. This process of acquiring the token is termed a flow.

When selecting an authorization mechanism, it's essential to weigh the specific needs and requirements of the system or application.