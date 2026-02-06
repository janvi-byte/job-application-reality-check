## System Architecture Overview

The project follows a simple modular architecture designed
for clarity, readability, and easy understanding.

The system is divided into three main layers:

1. User Interaction Layer
2. Evaluation Logic Layer
3. Documentation Layer

## Component Breakdown

- `main.py`
  Handles user interaction such as input collection and output display.

- `evaluation.py`
  Contains the core logic for confidence-based skill evaluation
  and decision-making.

- `docs/`
  Contains all design explanations, reasoning, and project documentation.

## Data Flow

User Input
→ Skill Confidence Evaluation
→ Readiness Percentage Calculation
→ Decision & Guidance Output

This separation ensures that logic and explanation remain independent,
making the project easy to maintain and extend.
