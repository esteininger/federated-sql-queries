# federated-sql-queries
Demo for federated sql queries across MongoDB &amp; S3 using MongoDB's Atlas Data Lake and the aggregation pipeline stage: $sql

![alt text](https://github.com/esteininger/federated-sql-queries/blob/master/assets/architecture.png?raw=true)

## Install

```
$ pip install requirements.txt
```

## Usage

1st: configure your Atlas Data Lake according to this documentation: [https://docs.mongodb.com/datalake/reference/config-files/data-lake-configuration](https://docs.mongodb.com/datalake/reference/config-files/data-lake-configuration)

2nd: populate your database using a file like `insert_data.py`

3rd: output your data to S3 via `out_to_s3.py`

4th: query your atlas data lake via SQL using `dl_to_sql.py`

## Video demo: 
[https://www.loom.com/share/485c109f26704c0fb565ae24b1655a57](https://www.loom.com/share/485c109f26704c0fb565ae24b1655a57)


