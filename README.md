#  NeuralNetOps: AI-Driven Network Provisioning

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Cisco](https://img.shields.io/badge/Cisco-Networking-orange.svg)](https://www.cisco.com/)
[![LLM](https://img.shields.io/badge/AI-LLM_Integrated-green.svg)](https://groq.com/)

**NeuralNetOps** is an intelligent automation framework that bridges the gap between natural language intent and technical network execution. By leveraging Large Language Models (LLMs) via the **Groq/DeepSeek API** and **Netmiko**, it enables engineers to configure Cisco infrastructure using simple English commands.

---

##  Project Showcase

Below is a demonstration of **NeuralNetOps** in action. The tool successfully detects the Cisco OS, processes a natural language request, and pushes the generated CLI commands to the device.

<p align="center">
  <img src="image_cf8ec3.png" width="90%" alt="AI Logic and Execution" />
  <br>
  <em>Figure 1: AI-powered command generation and Netmiko execution flow.</em>
</p>

<p align="center">
  <img src="Screenshot 2026-03-14 161331.png" width="45%" alt="Terminal UI" />
  <img src="Screenshot 2026-03-14 161331.png" width="45%" alt="SecureCRT Verification" />
  <img src="Screenshot 2026-03-14 161331.png" width="45%" alt="Network Topology" />
</p>

---

##  Key Features
- **OS Intelligence:** Automatically detects the target device OS (IOS, IOS-XE, NX-OS) to ensure command syntax accuracy.
- **Natural Language to CLI:** Translates complex intents (e.g., "Configure a Site-to-Site VPN") into precise Cisco configuration sets.
- **Safety First:** Integrated **Dangerous Command Filter** to prevent accidental execution of destructive commands like `erase` or `reload`.
- **Human-in-the-Loop:** Interactive confirmation prompt before pushing any changes to production/lab devices.

##  Built With
- **Python:** The core engine.
- **Netmiko:** For multi-vendor SSH/Telnet connectivity.
- **Groq/DeepSeek API:** High-speed LLM inference for command generation.
- **Regular Expressions (Regex):** For parsing device output and safety filtering.

##  How It Works
1. **Connectivity:** The script establishes a session to the Cisco device.
2. **Identification:** It runs `show version` to identify the specific OS.
3. **Intent Parsing:** The user provides a goal in plain English.
4. **AI Generation:** The LLM generates the specific CLI syntax based on the detected OS.
5. **Validation:** The script checks for "forbidden" commands.
6. **Execution:** Upon user approval, commands are pushed via `send_config_set()`.

##  Installation & Usage

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/NeuralNetOps.git](https://github.com/YOUR_USERNAME/NeuralNetOps.git)
   cd NeuralNetOps
