# PORT: Personnel Operational Readiness Tracker

## Overview
PORT is a multi-agent AI system for Navy Reserve Readiness Action Planning. It helps Sailors and unit leadership understand requirements before upcoming Drill Weekend(s) and generate action plans for the Sailor.

This repository is a capstone prototype. It does not connect to live US Navy or DoD systems.

## Problem
Navy Reserve readiness information is often spread across systems, emails, calendars, and local process knowledge. Missing a readiness requirement can affect mobilization readiness and create additional work for the unit.

## System Goal
PORT provides decision support by reviewing a Sailor's readiness record, retrieving sample guidance, generating a Drill Weekend action plan, and flagging readiness-impacting actions for human review.

## Architecture
PORT is designed as a multi-agent system.

Conceptual agents:
- Coordinator Agent
- Medical Readiness Agent
- Training Readiness Agent
- Administrative Readiness Agent
- Action Planning Agent
- Communications Agent

Human review is required before any communication or action is finalized.

## Repository Contents
```text
PORT-Capstone/
├── README.md
├── requirements.txt
├── src/
│   └── port_demo.py
├── data/
│   ├── dummy_sailor_record.json
│   └── dummy_readiness_guidance.json
├── outputs/
│   └── sample_dwe_action_plan.md
├── evaluation/
│   └── evaluation_summary.md
└── docs/
    └── architecture_overview.md
```

## Setup
```bash
pip install -r requirements.txt
```

## Run the Demo
From the repository root:

```bash
python src/port_demo.py
```

The demo loads readiness data, applies dummy readiness rules, and writes a generated action plan to the `outputs` folder.

## Safety Notes
PORT is a decision-support prototype. It does not update official records, submit forms, or send communications. Any action that could affect readiness status is flagged for human review.

## Data Note
All data in this repository is synthetic and created for demonstration only.
