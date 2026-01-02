# Hackathon II – Phase I Constitution  
## In-Memory Todo Console Application

---

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must originate from written specifications.
Code is not allowed unless:
- a requirement exists in `specify`
- a design exists in `plan`
- a task exists in `tasks`

Implementation must trace back to specs.
If behavior is unclear, the spec must be updated before coding.

---

### II. Single Authoritative State
There must be exactly one authoritative in-memory owner of all Todo state.

- All mutations flow through explicit interfaces
- No global state
- No hidden side effects
- No component may mutate state indirectly

This rule exists to guarantee Phase II and Phase III compatibility.

---

### III. Strict Phase Boundaries
Phase I is intentionally limited.

Phase I **must not** include:
- persistence of any kind
- databases or files
- web, GUI, or API layers
- AI or agent logic
- speculative future features

Phase I **must**:
- expose clean extension points
- remain fully deterministic
- be disposable only in data, not in architecture

---

### IV. Separation of Concerns
Responsibilities must be cleanly separated:

- Input handling and validation
- Business rules
- State management
- Read-only queries
- Console I/O

Violations include:
- menu logic mutating state
- business logic printing output
- functions doing more than one job

---

### V. Determinism Over Convenience
Given the same sequence of commands, the system must always produce the same result.

- No randomness
- No implicit behavior
- No time-based logic

Determinism is required for testability and AI integration in later phases.

---

### VI. Minimal Domain, Maximum Clarity
The Todo domain is intentionally simple.

Each task supports only:
- unique identifier
- title
- description
- completion status

Any additional attributes belong to later phases and are forbidden here.

---

## Technical Constraints

- Language: Python (standard library only)
- Interface: Console / Terminal
- Storage: In-memory only
- Program exit must clear all data
- No external libraries or APIs

---

## Development Workflow

1. Constitution defines the rules
2. Specifications define required behavior
3. Plans define architecture and boundaries
4. Tasks define atomic units of work
5. Code implements tasks exactly

Skipping steps is a violation.

---

## Governance

This constitution supersedes:
- convenience
- personal preference
- speed

Any change requires:
- explicit documentation
- justification
- confirmation it does not break Phase II or III

Architecture decisions must survive future phases without rewrite.

---

**Version**: 1.0.0  
**Ratified**: 2026-01-02  
**Phase**: Hackathon II – Phase I
