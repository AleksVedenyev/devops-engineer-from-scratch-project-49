# Brain Games

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AleksVedenyev/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AleksVedenyev/devops-engineer-from-scratch-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=AleksVedenyev_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=AleksVedenyev_devops-engineer-from-scratch-project-49)

## "Brain Games is a collection of console mini-games designed to train logic and math skills"

### Links

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

---

## Quick Start

### Clone repository

```bash
git clone https://github.com/AleksVedenyev/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

### Install dependencies

```bash
make install
```

or directly with `uv`:

```bash
uv sync
```

### Run game

```bash
make brain-even
```

or:

```bash
uv run brain-even
```

---

# Available Commands

| Command | Description |
|---|---|
| `make install` | Install dependencies |
| `make build` | Build package |
| `make package-install` | Install built wheel package |
| `make lint` | Run Ruff linter |
| `make brain-games` | Run brain-games welcome script |
| `make brain-even` | Run even game |
| `make brain-calc` | Run calculator game |
| `make brain-gcd` | Run greatest common divisor game |
| `make brain-progression` | Run progression game |
| `make brain-prime` | Run prime number game |

## Run games directly with uv

```bash
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```
---

# Build Package

Build wheel and source distribution:

```bash
make build
```

Install built package:

```bash
make package-install
```

After installation, CLI commands will be available globally.

---

# Development

## Run linter

```bash
make lint
```

or directly:

```bash
uv run ruff check brain_games
```

## Dependency management

Install and sync dependencies:

```bash
uv sync
```
---

Brain-Even
[![asciicast](https://asciinema.org/a/2KSQbE6rYI0Lg5mM.svg)](https://asciinema.org/a/2KSQbE6rYI0Lg5mM)

Brain-Calc
[![asciicast](https://asciinema.org/a/NNZbVSJjwZnhqeEq.svg)](https://asciinema.org/a/NNZbVSJjwZnhqeEq)

Brain-GCD
[![asciicast](https://asciinema.org/a/dFcHaAvWp27M8Iyy.svg)](https://asciinema.org/a/dFcHaAvWp27M8Iyy)

Brain-Progression
[![asciicast](https://asciinema.org/a/psydlzTHmijzY2Ch.svg)](https://asciinema.org/a/psydlzTHmijzY2Ch)

Brain-Prime
[![asciicast](https://asciinema.org/a/itR3P3ssjUr94Pxl.svg)](https://asciinema.org/a/itR3P3ssjUr94Pxl)
