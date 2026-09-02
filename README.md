# VISION-mini

VISION-mini is a lightweight variant of VISION designed for users who have limited access to capable or high-context AI models.

It preserves the core VISION workflow while intentionally reducing **context usage, Skill count, and instruction complexity**.

## Why VISION-mini Exists

The full VISION V1 prioritizes reliability and capability. Its Skills contain detailed instructions, validation rules, workflows, and deliberate redundancy to improve behavioral consistency.

That comes with a cost: **context and model capability requirements**.

VISION-mini takes the opposite approach:

> **Use less context and fewer capabilities so VISION can run on more constrained models and free-tier tooling.**

## V1 vs VISION-mini

|                     | VISION V1          | VISION-mini                   |
| ------------------- | ------------------ | ----------------------------- |
| Goal                | Maximum capability | Minimum resource requirements |
| Instructions        | Detailed           | Compressed                    |
| Skills              | Full set           | Reduced set                   |
| Context usage       | Higher             | Lower                         |
| Behavioral guidance | Extensive          | Essential rules only          |
| Redundancy          | Intentional        | Minimized                     |
| Capability          | Full               | Reduced                       |
| Reliability         | Higher             | Potentially lower             |
| Model requirements  | Higher             | Lower                         |

## What Is Reduced?

VISION-mini reduces the system in two ways.

### 1. Smaller Skills

Skills are rewritten into compact, model-oriented instructions.

Explanations, repetition, and non-essential guidance are removed while preserving the core workflow and safety constraints.

### 2. Fewer Skills

VISION-mini does not include every VISION V1 capability.

For example, advanced capabilities such as:

* Project management
* Email management
* Other larger or specialized Skills

may be excluded entirely.

This is intentional. A smaller Skill set reduces both the amount of context required and the complexity the model must reason over.

## The Tradeoff

VISION-mini should **not be considered feature-equivalent to VISION V1**.

The tradeoff is straightforward:

```text
More capabilities
        +
More detailed instructions
        +
More contextual guidance
        ↓
Higher resource requirements
        ↓
VISION V1
```

versus:

```text
Fewer capabilities
        +
Shorter instructions
        +
Less contextual overhead
        ↓
Lower resource requirements
        ↓
VISION-mini
```

A capable model with sufficient context should generally prefer **VISION V1**.

A constrained or free model may benefit from **VISION-mini**, even if that means sacrificing capabilities or some behavioral reliability.

## Design Principle

VISION-mini follows one principle:

> **Preserve the core VISION experience while spending as few tokens as reasonably possible.**

The goal is not to make VISION-mini equally powerful.

The goal is to make **a useful version of VISION available when model capability, context limits, or cost are constraints**.

## Relationship to VISION V1

VISION V1 remains the **full reference implementation**.

VISION-mini is a separate, intentionally constrained profile derived from it.

Changes made to VISION-mini should therefore be evaluated against two questions:

1. **Does the reduced version still behave correctly for its supported capabilities?**
2. **Did the reduction meaningfully decrease its context/resource requirements?**

If a capability is not essential to the mini profile, it may be removed rather than compressed.

## In Short

**VISION V1:** Full-featured, detailed, reliability-first.

**VISION-mini:** Lightweight, reduced, cost/context-first.

VISION-mini exists so that the VISION architecture is not limited to users with expensive or high-capability models.
