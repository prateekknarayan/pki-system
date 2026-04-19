# PKI System Project

This project implements a simplified Public Key Infrastructure (PKI) system including:

- Key Management
- Certificate Authority (CA)
- Certificate Issuance
- Validation
- Revocation (CRL)

## Architecture

                ┌──────────────────────┐
                │      Client/API      │
                └─────────┬────────────┘
                          │
                ┌─────────▼────────────┐
                │   PKI Core Services  │
                └─────────┬────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Key Management   Certificate Mgmt   Revocation
        │                 │                 │
        └──────────┬──────┴──────┬──────────┘
                   ▼             ▼
             Crypto Layer   Storage Layer