## weaviate vector Database Test
this is an example to connect with docker based weaviate, deployed in aws cloud service.


## Backup in S3

To back-up the db run the command.
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jbc_admin" \
  -d '{
    "id": "your-backup-id"
  }' \
  http://54.168.235.76:8080/v1/backups/s3
```

## restore the db from S3
replace the backup id only
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jbc_admin" \
  -d '{
    "id": "your-backup-id"
  }' \
  http://54.168.235.76:8080/v1/backups/s3/your-backup-id/restore

```


