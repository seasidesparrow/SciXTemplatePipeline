# LOGGING_LEVEL = 'WARN'
# LOGGING_LEVEL = "INFO"
LOGGING_LEVEL = "DEBUG"
LOG_STDOUT = True
# SQLALCHEMY Configuration
SQLALCHEMY_URL = "postgresql://affildb:affildb@localhost:5432/affildb"
SQLALCHEMY_ECHO = False
# REDIS Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
# Kafka Configuration
KAFKA_BROKER = "localhost:9092"
SCHEMA_REGISTRY_URL = "http://localhost:8081"
# AFFIL AVRO Schema Parameters
AFFIL_INPUT_SCHEMA = "AffilInputSchema"
AFFIL_INPUT_TOPIC = "AffilInput"
AFFIL_OUTPUT_SCHEMA = "AffilOutputSchema"
AFFIL_OUTPUT_TOPIC = "AffilOutput"
# S3 Configuration
S3_PROVIDERS = ["AWS", "MINIO"]
# AWS Configuration
AWS_ACCESS_KEY_ID = "CHANGEME"
AWS_SECRET_ACCESS_KEY = "SECRETS"
AWS_DEFAULT_REGION = "us-east-1"
PROFILE_NAME = "SESSION_PROFILE"
AWS_BUCKET_NAME = "BUCKETNAME"
AWS_BUCKET_ARN = "BUCKETARN"
# MINIO Configuration
MINIO_ACCESS_KEY_ID = "admin"
MINIO_SECRET_ACCESS_KEY = "supersecret"
MINIO_BUCKET_NAME = "scix-AugmentAffil"
MINIO_S3_URL = "http://localhost:9000"
