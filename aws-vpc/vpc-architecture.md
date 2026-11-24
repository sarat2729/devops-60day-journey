# Multi-Tier AWS VPC Architecture (Days 9–12)
- **Region:** Asia Pacific (Sydney) `ap-southeast-2`
- **VPC:** `DevOps-Prod-VPC` (`10.0.0.0/16`)
- **Public Tier:** `Public-Subnet-AZ1` (`10.0.1.0/24` in `ap-southeast-2a`) -> Routed via `Public-Route-Table` (`0.0.0.0/0`) to `DevOps-Prod-IGW`
- **Private Tier:** `Private-Subnet-AZ1` (`10.0.2.0/24` in `ap-southeast-2a`) -> Isolated on Main Route Table (local `10.0.0.0/16` routing only, zero direct internet access)
- **Security Groups (Chained Firewall Architecture):**
  - `DevOps-Public-SG`: Allows inbound HTTP (`80`) and SSH (`22`) to public-facing tier
  - `DevOps-Private-SG`: Blocks public internet; allows inbound SSH (`22`) strictly from `DevOps-Public-SG` source ID
