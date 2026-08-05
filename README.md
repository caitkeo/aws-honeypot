# AWS Cloud Honeypot & Threat Monitoring Platform

## Overview

Built an AWS-hosted SSH honeypot using Cowrie to collect attacker behavior and visualize threats.

## Architecture

EC2 → Cowrie → CloudWatch Logs → Dashboard → Alerts

## Technologies

- AWS EC2
- IAM
- CloudWatch Logs
- CloudWatch Alarms
- Linux
- Python
- SSH
- Cowrie Honeypot

## Features

- Captures SSH login attempts
- Records attacker IP addresses
- Logs commands executed
- Tracks usernames/passwords attempted
- Creates SOC-style dashboards
- Sends CloudWatch alerts

## Screenshots

![Crowie Dashboard Screenshot](screenshots/crowrie-dash-1.png)
![Crowie Dashboard Screenshot Part 2](screenshots/cowrie-dash-2.png)
![Crowie Dashboard Screenshot Part 3](screenshots/cowrie-dash-3.png)
