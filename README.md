# PKI System Project

This project implements a simplified Public Key Infrastructure (PKI) system including:

- Key Management
- Certificate Authority (CA)
- Certificate Issuance
- Validation
- Revocation (CRL)

## Architecture

```mermaid
graph TD
    A[Client / API] --> B[PKI Core Services]

    B --> C[Key Management]
    B --> D[Certificate Management]
    B --> E[Revocation]

    C --> F[Crypto Layer]
    D --> F
    E --> F

    F --> G[Storage Layer]