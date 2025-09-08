"""
kafka_consumer_mk.py

Consume messages from a Kafka topic and process them.
"""

import os
from dotenv import load_dotenv
from utils.utils_consumer import create_kafka_consumer
from utils.utils_logger import logger

load_dotenv()


def get_kafka_topic() -> str:
    topic = os.getenv("KAFKA_TOPIC", "unknown_topic")
    logger.info(f"Kafka topic: {topic}")
    return topic


def get_kafka_consumer_group_id() -> int:
    group_id: str = os.getenv("KAFKA_CONSUMER_GROUP_ID_JSON", "default_group")
    logger.info(f"Kafka consumer group id: {group_id}")
    return group_id


def process_message(message: str) -> None:
    print(f"Consumed: {message}")
    logger.info(f"Processing message: {message}")

    if "MK-ALERT" in message:
        print(f"[ALERT] {message}")
        logger.warning(f"[ALERT] {message}")


def main() -> None:
    logger.info("START consumer.")

    topic = get_kafka_topic()
    group_id = get_kafka_consumer_group_id()
    logger.info(f"Consumer: Topic '{topic}' and group '{group_id}'...")

    consumer = create_kafka_consumer(topic, group_id)

    logger.info(f"Polling messages from topic '{topic}'...")
    try:
        for message in consumer:
            message_str = message.value
            logger.debug(f"Received message at offset {message.offset}: {message_str}")
            process_message(message_str)
    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Error while consuming messages: {e}")
    finally:
        consumer.close()
        logger.info(f"Kafka consumer for topic '{topic}' closed.")

    logger.info(f"END consumer for topic '{topic}' and group '{group_id}'.")


if __name__ == "__main__":
    main()
