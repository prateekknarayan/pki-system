# PKI System Project

This project implements a simplified Public Key Infrastructure (PKI) system including:

- Key Management
- Certificate Authority (CA)
- Certificate Issuance
- Validation
- Revocation (CRL)

## Architecture

sequenceDiagram
    participant Client
    participant PKI
    participant CA

    Client->>PKI: Request Certificate
    PKI->>CA: Send CSR
    CA->>PKI: Signed Certificate
    PKI->>Client: Return Certificate

