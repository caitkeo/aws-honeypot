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
