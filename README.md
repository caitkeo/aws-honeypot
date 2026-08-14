# AWS Cloud Honeypot & Threat Monitoring Platform

## Overview

This project is a cloud-based SSH honeypot built with AWS EC2, Cowrie, Amazon CloudWatch, CloudWatch Logs Insights, metric filters, alarms, Amazon SNS, and Python.

The project captures SSH authentication and command activity, forwards structured Cowrie telemetry into CloudWatch, visualizes activity through a SOC-style dashboard, detects elevated command execution, and sends automated email alerts.

## Architecture

EC2 → Cowrie → CloudWatch Logs → Dashboard → Alerts

## Technologies

- AWS EC2
- Ubuntu Linux
- Cowrie SSH Honeypot
- Amazon CloudWatch
- CloudWatch Logs
- CloudWatch Logs Insights
- CloudWatch Metric Filters
- CloudWatch Alarms
- Amazon SNS
- AWS IAM
- Python
- SSH
- JSON

## Features
This project accomplishes the following objectives: 
- Capturing SSH authentication attempts
- Recording commands executed inside a honeypot environment
- Collecting structured JSON security telemetry
- Centralizing logs in Amazon CloudWatch
- Querying activity with CloudWatch Logs Insights
- Building a SOC-style security dashboard
- Creating detection logic using metric filters
- Triggering CloudWatch alarms from suspicious activity
- Sending automated email notifications through Amazon SNS
- Analyzing Cowrie logs with Python

## EC2 Configuration

The EC2 security group separates administrative access from honeypot traffic:

| Port | Service | Source | Purpose |
|------|---------|--------|---------|
| 22 | SSH | Restricted IP | EC2 administration |
| 2222 | Cowrie SSH | Internet | Honeypot traffic |

Administrative SSH access is restricted while the Cowrie service is intentionally exposed on TCP port 2222.

## Cowrie Configuration
Cowrie listens for incoming SSH connections on port 2222.

[ssh]
listen_endpoints = tcp:2222:interface=0.0.0.0

A sanitized example configuration is available here:

config/cowrie.cfg.example

Cowrie records structured events in:

/home/ubuntu/cowrie/var/log/cowrie/cowrie.json

Common events include:

cowrie.session.connect
cowrie.login.success
cowrie.login.failed
cowrie.command.input
cowrie.session.closed

## Screenshots

![Crowie Dashboard Screenshot](screenshots/crowrie-dash-1.png)
![Crowie Dashboard Screenshot Part 2](screenshots/cowrie-dash-2.png)
![Crowie Dashboard Screenshot Part 3](screenshots/cowrie-dash-3.png)
