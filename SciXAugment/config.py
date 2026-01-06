# LOGGING_LEVEL = 'WARN'
# LOGGING_LEVEL = "INFO"
LOGGING_LEVEL = "DEBUG"
LOG_STDOUT = True
# SQLALCHEMY Configuration
SQLALCHEMY_URL = "postgresql://augmentaff:augmentaff@localhost:5432/augmentaff"
SQLALCHEMY_ECHO = False
# REDIS Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
# Kafka Configuration
KAFKA_BROKER = "kafka:9092"
SCHEMA_REGISTRY_URL = "http://schema-registry:8081"
# TEMPLATE AVRO Schema Parameters
AUGMENT_INPUT_SCHEMA = "AffilInputSchema"
AUGMENT_INPUT_TOPIC = "AffilInput"
AUGMENT_OUTPUT_SCHEMA = "AffilOutputSchema"
AUGMENT_OUTPUT_TOPIC = "AffilOutput"
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
MINIO_S3_URL = "http://minio:9000"
