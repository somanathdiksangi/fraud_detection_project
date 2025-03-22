import os

# Define the folder structure
folders = [
    "models",
    "dataset",
    "backend",
    "kafka_streaming",
    "spark_streaming",
    "utils",
    "tests",
    "notebooks",
    "logs"
]

files = {
    "dataset/creditcard.csv": "",
    "backend/app.py": "",
    "backend/requirements.txt": "pandas\nnumpy\nscikit-learn\nflask\njoblib\nkafka-python\npyspark\nrequests\n",
    "kafka_streaming/kafka_producer.py": "",
    "kafka_streaming/kafka_consumer.py": "",
    "spark_streaming/spark_consumer.py": "",
    "utils/preprocess.py": "",
    "tests/test_model.py": "",
    "tests/test_api.py": "",
    "notebooks/fraud_detection.ipynb": "",
    "logs/kafka_logs.log": "",
    "logs/spark_logs.log": "",
    "README.md": "# Fraud Detection Project\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("✅ Project structure created successfully!")
