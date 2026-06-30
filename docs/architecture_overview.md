# PORT Architecture Overview

PORT is designed as a decision-support system for Navy Reserve readiness planning.

## Workflow

```text
User Request
    ↓
PORT Coordinator Agent
    ↓
Synthetic Readiness Data + Retrieved Guidance
    ↓
Specialized Readiness Agents
    ↓
Readiness Planning Agent
    ↓
Human Review Check
    ↓
Draft Output
```

## Key Design Choices

PORT separates readiness functions into specialized agents so each domain can apply its own logic.

The retrieval layer grounds recommendations in sample guidance.

The planning layer prioritizes actions before Drill Weekend.

The safety layer prevents the prototype from acting autonomously when human review is needed.

## Deployment Boundary

This prototype does not connect to live systems. A production version would require DoD review and approval.
