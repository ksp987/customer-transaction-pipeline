# customer-transaction-pipeline

### S3 Raw Zone Layout

- **Bucket**: `rawdatatecron`
- **Zone**: `raw/`
- **Domain**: `finance/`
- **Dataset**: `txn_payments/`
- **Partitioned By**:
  - `year=2024/`
  - `month=06/`

📁 Final Path:  
`s3://rawdatatecron/raw/finance/txn_payments/year=2024/month=06/PS_20174392719_1491204439457_log.csv`
