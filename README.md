## weaviate vector Database Test


## Backup in S3
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jbc_admin" \
  -d '{
    "id": "your-backup-id"
  }' \
  http://54.168.235.76:8080/v1/backups/s3
```



