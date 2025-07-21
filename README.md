This project sets up a real-time monitoring stack using **Nakama**, **Prometheus** and **Grafana**.
It also includes a python script that simulates login to Nakama server, enabling Prometheus to scrape useful metric which are visualized in Grafan dashboards.

---

## Stack Components

* \*\*Nakama\*\* – Game server exposing metrics on `/metrics`

* \*\*CockroachDB\*\* – Persistent storage for Nakama

* \*\*Prometheus\*\* – Scrapes and stores metrics from Nakama

* \*\*Grafana\*\* – Visualizes login metrics via dashboards

* \*\*Python script\*\* – Simulates multiple user logins to generate metrics

---

\## Requirements

* Docker \& Docker Compose
* Python 3.7+
* Internet connection to pull images



\## Getting Started

* 1. Clone the repository

```bash

git clone https://github.com/your-username/prometheus-grafana-monitoring.git

cd prometheus-grafana-monitoring

run docker compose up


\# This will start:

* Prometheus at http://localhost:9090
* Grafana at http://localhost:3000
* Nakama at http://localhost:7350
* Nakama admin panel at http://localhost:7351
* CockroachDB console at http://localhost:8080


\## Login Credentials

\# Nakama admin panel:

* User: admin
* Password: password


\# Grafana Dashboard:

* user: admin
* password: admin


\## To simulate logins:

* pip install nakama
* python simulate\_logins.py


\## Metrics You Can Track


| Metric                                | Description          |

| ------------------------------------- | -------------------- |

| `nakama\_AuthenticateEmail\_count`      | Total email logins   |

| `nakama\_AuthenticateEmail\_latency\_ms` | Login latency        |

| `nakama\_overall\_request\_count`        | All requests handled |

| `nakama\_db\_total\_open\_conns`          | DB connections       |


You can visualize metrics using PromQL queries in Grafana like

* rate(nakama\_AuthenticateEmail\_count\[$\_\_rate\_interval])

## Grafana Dashboards

The `dashboards/` folder contains pre-configured Grafana dashboard JSONs.
* `nakama-monitoring.json` – Tracks login rate, latency, DB connections, and request count.

To import:
1. Go to Grafana → Dashboards → Import
2. Upload or paste the JSON
3. Select Prometheus as the data source






