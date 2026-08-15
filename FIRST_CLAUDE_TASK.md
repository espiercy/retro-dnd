# First Claude Code Assignment

Perform an architecture review of this repository before any production code is written.

Read, in this order:

1. `GAME_CONSTITUTION.md`
2. `SOURCE_HIERARCHY.md`
3. `AGENTS.md`
4. `ARCHITECTURE.md`
5. `CLAUDE.md`

Do not edit, create, delete, rename, or reformat any files.

## Review Goals

Evaluate whether the proposed architecture is a sound minimum foundation for a historically faithful 1974 Dungeons & Dragons dungeon-crawling simulator.

Pay particular attention to:

- separation of authoritative simulation from presentation and narration;
- deterministic and reproducible handling of randomness;
- keeping rules provenance visible and auditable;
- preventing rules ambiguity from being silently resolved in code;
- keeping AD&D assumptions out of the implementation;
- preserving historical encounter, reaction, morale, treasure, and dungeon procedures rather than replacing them with modern abstractions;
- applying survivability modifications after canonical historical generation while leaving treasure and XP unchanged;
- persistent dungeon state;
- avoiding premature frameworks or unnecessary architectural layers;
- the smallest useful first vertical slice.

## Required Output

Return a concise review with these sections:

### 1. Architecture Strengths
What should remain as proposed?

### 2. Risks or Overengineering
What should be simplified before implementation?

### 3. Missing Boundaries
What important architectural separation or invariant is absent?

### 4. Rules-Fidelity Risks
Where could an implementation agent accidentally introduce unsupported D&D behavior?

### 5. Proposed Minimum Module Layout
Recommend the smallest package/module structure sufficient for the first vertical slice. Do not design the full future application.

### 6. Proposed First Three Implementation Issues
Describe three small, dependency-ordered implementation tasks that would move toward the first vertical slice after the architecture is approved.

For each issue, identify which approved Rule Card(s) would need to exist before implementation begins.

### 7. Questions Requiring Human Decisions
List only questions that genuinely block architecture or the first implementation steps. Do not resolve them yourself.

Do not write code.
