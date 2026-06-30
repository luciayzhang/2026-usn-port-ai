# Evaluation Summary

This prototype was evaluated with synthetic readiness scenarios.

## Recommendation Accuracy
The demo checks whether PORT recommends the expected action for each readiness issue.

Result: PASS for the included synthetic test case.

## Groundedness
Each recommendation should reference a sample guidance source.

Result: PASS for the included synthetic test case.

## Fallback Behavior
When guidance is unavailable or an action could affect readiness status, PORT should flag the output for review.

Result: PASS for the included synthetic test case.

## Limitation
This evaluation uses synthetic data only. It does not validate performance against live US Navy or DoD systems.
