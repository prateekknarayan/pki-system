# PKI System Project

This project implements a simplified Public Key Infrastructure (PKI) system including:

- Key Management
- Certificate Authority (CA)
- Certificate Issuance
- Validation
- Revocation (CRL)

## Architecture

<pre> ```text ┌──────────────────────┐ │ Client/API │ └─────────┬────────────┘ │ ┌─────────▼────────────┐ │ PKI Core Services │ └─────────┬────────────┘ │ ┌──────────────┼──────────────┐ ▼ ▼ ▼ Key Mgmt Cert Mgmt Revocation │ │ │ └──────────┬───┴────┬─────────┘ ▼ ▼ Crypto Layer Storage Layer ``` </pre>
