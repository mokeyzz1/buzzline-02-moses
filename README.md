# buzzline-02-moses

This project demonstrates streaming data in Python using **Apache Kafka**.  
A custom Kafka producer generates messages continuously, and a custom Kafka consumer processes those messages in real time, detecting special alerts.

---

## Setup

Clone and prepare the environment (Python 3.11 recommended).

```zsh
git clone https://github.com/mokeyzz1/buzzline-02-moses.git
cd buzzline-02-moses
python3 -m venv .venv
source .venv/bin/activate    # Mac/Linux
# .venv\Scripts\activate     # Windows PowerShell
pip install -r requirements.txt
```

#### Running Kafka Services

Kafka must be running locally before starting producer and consumer

Terminal 1 – Start ZooKeeper
``` zsh
cd ~/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```

#### Terminal 2 – Start Kafka Broker
``` zsh
cd ~/kafka
bin/kafka-server-start.sh config/server.properties
```

### Custom MK Kafka Producer & Consumer

#### Custom producer and consumer were added for Task 2.
They demonstrate real-time streaming with MK-style messages and alert detection for MK-ALERT.

Mac/Linux
Terminal 3 – MK Producer
``` zsh
cd ~/buzzline-02-moses
source .venv/bin/activate
python3 -m producers.kafka_producer_mk
```

Terminal 4 – MK Consumer
``` zsh 
cd ~/buzzline-02-moses
source .venv/bin/activate
python3 -m consumers.kafka_consumer_mk
```