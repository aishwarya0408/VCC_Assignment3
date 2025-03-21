# Auto-Scaling Monitoring

## Overview
This project implements a local Virtual Machine (VM) monitoring system that tracks CPU and memory usage. If resource utilization exceeds 75%, the system triggers an auto-scaling mechanism that deploys workloads to a public cloud (AWS/GCP/Azure).

## Features
- **Real-time monitoring** of CPU and memory usage using Python (psutil).
- **Auto-scaling trigger** when resource usage surpasses thresholds.
- **Cloud deployment automation** using shell scripts.
- **Customizable thresholds** and monitoring intervals.

## Technologies Used
- Python
- psutil (for system monitoring)
- Bash scripting (for cloud deployment)
- Prometheus & Grafana (for visualization) *(optional)*

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Auto-Scaling-Monitoring.git
   cd Auto-Scaling-Monitoring
   ```
2. Install dependencies:
   ```bash
   pip install psutil
   ```
3. Run the monitoring script:
   ```bash
   python monitoring/monitor.py
   ```

## Configuration
- Modify the `CPU_THRESHOLD` and `MEMORY_THRESHOLD` values in `monitor.py` to adjust scaling conditions.
- Edit `deploy_to_cloud.sh` to configure cloud migration logic.

## Auto-Scaling Workflow
1. **Monitor local VM resources** (CPU & memory usage).
2. **Trigger auto-scaling** if usage > 75%.
3. **Migrate workloads to the cloud** using a predefined deployment script.
4. **Update system logs & alerts** for monitoring.

## Architecture
![Architecture Diagram](docs/architecture_diagram.png)

## Contributions
Feel free to submit pull requests or report issues. Contributions are welcome!

## License
This project is licensed under the MIT License.
