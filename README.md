<p align="center">
  <img src="https://img.shields.io/badge/OMNIS-AI%20COGNITIVE%20OPERATING%20SYSTEM-6C63FF?style=flat-square" alt="OMNIS"> 
  <img src="https://img.shields.io/badge/STATUS-ACTIVE%20DEVELOPMENT-F97316?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/LICENSE-MIT-6C63FF?style=flat-square" alt="MIT License">
</p>

<h1 align="center">OMNIS — Omni-Modal Neural Intelligence System</h1>

<p align="center">
  <strong>A modular, persistent, tool-using AI systems platform designed for extensible machine intelligence.</strong>
</p>

<p align="center">
  <a href="https://github.com/Arvindhbabu/OMNIS-AI">GitHub</a> •
  <a href="http://127.0.0.1:8000/docs">API Documentation</a>
</p>

---

## 🧠 About OMNIS

**OMNIS (Omni-Modal Neural Intelligence System)** is an open-source AI systems project designed to provide a modular foundation for building intelligent applications with persistent memory, knowledge retrieval, tool usage, agent orchestration, and multimodal capabilities.

OMNIS is **not intended to be another ChatGPT clone**.

Instead, the project is being engineered as a broader **AI operating infrastructure**, where different cognitive capabilities can exist as independent, composable subsystems.

The long-term vision is to build a system capable of combining:

- 🧠 Persistent memory
- 📚 Knowledge retrieval
- 🔎 Semantic search
- 🛠️ Tool and plugin execution
- 🤖 Agent orchestration
- 👁️ Multimodal perception
- 🧩 Context management
- 🔄 Workflow execution
- 🗃️ Persistent state
- ⚡ Real-time runtime services

The architecture is intentionally designed so that models, memory systems, retrieval engines, tools, and agents can evolve independently.

> **OMNIS is being built as an intelligence infrastructure, not merely an interface to an AI model.**

---

## 🎯 Vision

Modern AI applications are often built around a single model surrounded by application-specific code.

OMNIS takes a different approach — it aims to provide a reusable cognitive architecture in which intelligence emerges from the interaction of multiple specialized systems:

```text
                         ┌──────────────────────┐
                         │        OMNIS         │
                         │   Cognitive Runtime  │
                         └──────────┬───────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       │                            │                            │
       ▼                            ▼                            ▼
   🧠 Memory                    📚 Knowledge                  🛠️ Tools
       │                            │                            │
       └────────────────────────────┼────────────────────────────┘
                                    │
                                    ▼
                           🤖 Agent Orchestration
                                    │
                                    ▼
                           👁️ Multimodal Layer
                                    │
                                    ▼
                            ⚙️ Runtime Services
```

The goal is to create an architecture where new models, tools, retrieval systems, and cognitive capabilities can be integrated without rewriting the entire platform.

---

## ✨ Core Objectives

OMNIS is being developed around several fundamental objectives.

### 🧠 Persistent Intelligence

Enable AI systems to retain and retrieve useful information across interactions.

Planned memory types:
- Short-term memory
- Long-term memory
- Semantic memory
- Episodic memory
- Conversation memory
- Context memory

### 📚 Knowledge-Centric Intelligence

Allow the system to reason over external knowledge rather than relying exclusively on model parameters.

Planned capabilities:
- Document ingestion
- PDF understanding
- Research paper retrieval
- GitHub repository understanding
- Semantic search
- Hybrid retrieval
- Vector search
- Retrieval-Augmented Generation (RAG)

### 🛠️ Tool-Using Intelligence

Provide a controlled mechanism through which agents can interact with external systems.

Potential tools:
- Web search
- File processing
- Code execution
- Database queries
- GitHub
- REST APIs
- Local tools
- External services

### 🤖 Agentic Orchestration

Provide infrastructure for intelligent task execution.

Planned capabilities:
- Task planning
- Tool selection
- Multi-step reasoning
- Agent workflows
- Agent memory
- Agent coordination
- Failure recovery
- Human-in-the-loop execution

### 👁️ Multimodal Intelligence

Extend OMNIS beyond text-based interaction.

Planned modalities:
- Text
- Images
- Audio
- Video
- Documents

The long-term goal is to enable cross-modal retrieval, understanding, and reasoning.

---

## 🏗️ Architecture

OMNIS follows a modular layered architecture.

```text
                         ┌───────────────────────────┐
                         │       User Interfaces     │
                         │  Web / Desktop / CLI / API│
                         └─────────────┬─────────────┘
                                       │
                                       ▼
                         ┌───────────────────────────┐
                         │        API Gateway        │
                         │          FastAPI          │
                         └─────────────┬─────────────┘
                                       │
                 ┌─────────────────────┼─────────────────────┐
                 │                     │                     │
                 ▼                     ▼                     ▼
        ┌────────────────┐   ┌──────────────────┐   ┌────────────────┐
        │    Services    │   │  Orchestration   │   │     Tools      │
        └────────┬───────┘   └─────────┬────────┘   └───────┬────────┘
                 │                     │                    │
                 └─────────────────────┼────────────────────┘
                                       ▼
                         ┌───────────────────────────┐
                         │     Cognitive Runtime     │
                         │                           │
                         │  Memory                   │
                         │  Knowledge                │
                         │  Context                  │
                         │  Agents                   │
                         │  Models                   │
                         │  Multimodal Processing    │
                         └─────────────┬─────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
             ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
             │  PostgreSQL  │   │    Redis     │   │ Vector Store │
             │  Persistent  │   │Runtime/Cache │   │    / RAG     │
             │    State     │   │              │   │              │
             └──────────────┘   └──────────────┘   └──────────────┘
```

---

## 🧱 Engineering Principles

### Modular Architecture

Every major subsystem is designed to have a clear responsibility and interface.

```text
API
 ↓
Services
 ↓
Repositories
 ↓
Database
```

This separation makes the system easier to test, maintain, and extend.

### Model Agnostic

OMNIS is not architecturally tied to a single AI model or provider. The long-term architecture is intended to support:
- Cloud-based models
- Local models
- Open-source models
- Specialized models
- Multimodal models

### Persistent State

AI systems become significantly more useful when they can maintain state. OMNIS therefore treats persistence as a first-class architectural concern rather than an optional feature.

### Extensibility

The platform is being designed to allow new capabilities to be added as modules rather than tightly coupled features. Future modules may include:
- Memory providers
- Vector stores
- LLM providers
- Embedding providers
- Tools
- Plugins
- Agents
- Model routers
- Retrieval engines
- Workflow engines

### Production-Oriented Engineering

OMNIS emphasizes engineering quality alongside AI functionality. The project currently incorporates:
- Type-safe Python
- Static type checking
- Automated formatting
- Automated linting
- Unit testing
- Integration testing
- Database migrations
- Dependency injection
- Docker infrastructure
- Environment-based configuration
- Versioned APIs

---

## 🚀 Current Status

### Phase 1 — Backend Foundation
**Status: ✅ Complete**

The initial backend infrastructure has been implemented and verified.

**Implemented**
- [x] Python project configuration
- [x] uv dependency management
- [x] FastAPI application factory
- [x] Versioned REST API
- [x] API routing architecture
- [x] Health endpoint
- [x] Version endpoint
- [x] System endpoint
- [x] Metadata API
- [x] PostgreSQL integration
- [x] Async SQLAlchemy
- [x] Repository pattern
- [x] Service layer
- [x] Dependency injection
- [x] Pydantic schemas
- [x] Alembic migrations
- [x] Redis integration
- [x] Docker Compose infrastructure
- [x] Unit tests
- [x] Integration tests
- [x] Ruff linting
- [x] Ruff formatting
- [x] Mypy type checking

**Current Test Status**
```
10 tests passed
0 failures
0 errors
```

**Current Code Quality**

| Check | Status |
|---|---|
| Ruff | ✅ Passed |
| Formatting | ✅ Passed |
| Mypy | ✅ Passed |
| Pytest | ✅ Passed |

---

## ⚙️ Current API

The OMNIS backend currently exposes a versioned API under `/api/v1`.

### Health
```
GET /api/v1/health
```
Example response:
```json
{
  "status": "healthy"
}
```

### Readiness

The readiness endpoint verifies the availability of core runtime dependencies.
```
GET /api/v1/health/ready
```
Example:
```json
{
  "status": "ready",
  "database": "healthy",
  "redis": "healthy"
}
```

### System
```
GET /api/v1/system
```
Example:
```json
{
  "name": "OMNIS",
  "version": "0.1.0",
  "environment": "development",
  "status": "operational"
}
```

### Version
```
GET /api/v1/version
```
Returns application version information.

### Metadata

OMNIS currently contains a complete metadata subsystem demonstrating the project's backend architecture.

**Create**
```
POST /api/v1/metadata
```
Request:
```json
{
  "key": "app_name",
  "value": "OMNIS AI Cognitive Operating System"
}
```

**Retrieve**
```
GET /api/v1/metadata/{key}
```

**Update**
```
PUT /api/v1/metadata/{key}
```
Request:
```json
{
  "value": "OMNIS AI Cognitive Operating System"
}
```

The metadata flow follows:

```text
HTTP Request
     ↓
FastAPI Router
     ↓
Dependency Injection
     ↓
Service Layer
     ↓
Repository Layer
     ↓
SQLAlchemy
     ↓
PostgreSQL
```

This subsystem serves as the foundation for future persistent cognitive state.

---

## 🗄️ Data Layer

OMNIS uses PostgreSQL as its primary relational persistence layer.

```text
SQLAlchemy Async Engine
        ↓
   AsyncSession
        ↓
  Repositories
        ↓
    Services
        ↓
       API
```

Database schema changes are managed through Alembic.

Run migrations:
```bash
uv run alembic upgrade head
```

Check the current migration:
```bash
uv run alembic current
```

---

## ⚡ Redis

Redis is included as the runtime caching and fast-state infrastructure.

Current connectivity can be verified through the readiness endpoint:
```
GET /api/v1/health/ready
```
Example:
```json
{
  "status": "ready",
  "database": "healthy",
  "redis": "healthy"
}
```

Future Redis usage will support capabilities such as:
- Caching
- Session state
- Task coordination
- Rate limiting
- Event-driven workflows
- Temporary agent state

---

## 🐳 Docker Infrastructure

OMNIS currently uses Docker Compose for local infrastructure.

```text
┌───────────────────────────────┐
│           OMNIS API           │
│            :8000              │
└───────────────┬───────────────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
┌──────────────┐  ┌──────────────┐
│  PostgreSQL  │  │    Redis     │
│    :5432     │  │    :6379     │
└──────────────┘  └──────────────┘
```

Start the complete development stack:
```bash
docker compose -f deployment/docker/compose.yaml up -d
```

Check service status:
```bash
docker compose -f deployment/docker/compose.yaml ps
```

Stop the stack:
```bash
docker compose -f deployment/docker/compose.yaml down
```

---

## 💻 Development Setup

### Prerequisites

Install the following:
- Python 3.12+
- [uv](https://github.com/astral-sh/uv)
- Docker Desktop
- Git

### Clone Repository
```bash
git clone https://github.com/Arvindhbabu/OMNIS-AI.git
cd OMNIS
```

### Install Dependencies
```bash
uv sync
```

### Configure Environment

Copy the example environment file.

**Windows PowerShell**
```powershell
Copy-Item .env.example .env
```

**Linux / macOS**
```bash
cp .env.example .env
```

> ⚠️ Never commit `.env` to Git.

### Start Infrastructure
```bash
docker compose -f deployment/docker/compose.yaml up -d
```

### Run the API
```bash
uv run uvicorn omnis_api.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI: `http://127.0.0.1:8000/openapi.json`

---

## 🧪 Testing

Run the complete test suite:
```bash
uv run pytest
```

Run with verbose output:
```bash
uv run pytest -v
```

Run unit tests:
```bash
uv run pytest apps/api/tests/unit -v
```

Run integration tests:
```bash
uv run pytest apps/api/tests/integration -v
```

---

## 🔍 Code Quality

OMNIS uses multiple automated quality gates.

**Ruff**
```bash
uv run ruff check .
```

**Formatting**
```bash
uv run ruff format --check .
```
Format the project:
```bash
uv run ruff format .
```

**Mypy**
```bash
uv run mypy apps/api/src
```

**Recommended verification before committing:**
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy apps/api/src
uv run pytest
```

All checks should pass before changes are committed.

---

## 📁 Project Structure

```text
OMNIS/
│
├── apps/
│   └── api/
│       │
│       ├── migrations/
│       │   └── versions/
│       │
│       ├── src/
│       │   └── omnis_api/
│       │       │
│       │       ├── api/
│       │       │   ├── routes/
│       │       │   │   ├── health.py
│       │       │   │   ├── metadata.py
│       │       │   │   ├── system.py
│       │       │   │   └── version.py
│       │       │   │
│       │       │   ├── dependencies.py
│       │       │   ├── responses.py
│       │       │   └── router.py
│       │       │
│       │       ├── cache/
│       │       │   └── redis.py
│       │       │
│       │       ├── core/
│       │       │   ├── config.py
│       │       │   └── constants.py
│       │       │
│       │       ├── database/
│       │       │   ├── models/
│       │       │   ├── repositories/
│       │       │   ├── base.py
│       │       │   ├── dependencies.py
│       │       │   └── session.py
│       │       │
│       │       ├── schemas/
│       │       │
│       │       ├── services/
│       │       │
│       │       ├── app.py
│       │       └── main.py
│       │
│       └── tests/
│           ├── integration/
│           └── unit/
│
├── deployment/
│   └── docker/
│       ├── compose.yaml
│       └── Dockerfile.api
│
├── tests/
│   └── integration/
│
├── alembic.ini
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

---

## 🗺️ Roadmap

OMNIS is being developed incrementally, with infrastructure preceding higher-level intelligence.

### Phase 1 — Backend Foundation
**Status: ✅ Complete**
- [x] Project foundation
- [x] FastAPI application
- [x] API versioning
- [x] Health API
- [x] Readiness API
- [x] System API
- [x] Version API
- [x] Metadata API
- [x] PostgreSQL
- [x] SQLAlchemy
- [x] Repository layer
- [x] Service layer
- [x] Dependency injection
- [x] Pydantic schemas
- [x] Alembic
- [x] Redis
- [x] Docker
- [x] Unit testing
- [x] Integration testing
- [x] Ruff
- [x] Mypy

### Phase 2 — Runtime Infrastructure
**Status: 🚧 In Progress**
- [ ] Application lifecycle management
- [ ] Runtime health model
- [ ] Structured error handling
- [ ] Request correlation IDs
- [ ] Structured logging
- [ ] Observability
- [ ] Metrics
- [ ] Configuration hardening
- [ ] Runtime dependency management
- [ ] Background task infrastructure

### Phase 3 — Security & Identity
**Status: 📋 Planned**
- [ ] Authentication
- [ ] Authorization
- [ ] API key management
- [ ] User identity
- [ ] Role-based access control
- [ ] Permission system
- [ ] Secrets management
- [ ] Audit logging
- [ ] Security middleware

### Phase 4 — Memory Engine
**Status: 📋 Planned**
- [ ] Conversation memory
- [ ] Short-term memory
- [ ] Long-term memory
- [ ] Semantic memory
- [ ] Episodic memory
- [ ] Memory retrieval
- [ ] Memory ranking
- [ ] Context compression
- [ ] Memory consolidation
- [ ] Memory lifecycle management

### Phase 5 — Knowledge Engine
**Status: 📋 Planned**
- [ ] Document ingestion
- [ ] PDF processing
- [ ] Document parsing
- [ ] Intelligent chunking
- [ ] Embedding pipeline
- [ ] Vector storage
- [ ] Semantic search
- [ ] Hybrid search
- [ ] RAG pipeline
- [ ] Research paper understanding
- [ ] GitHub repository understanding

### Phase 6 — Tool & Plugin Runtime
**Status: 📋 Planned**
- [ ] Tool registry
- [ ] Tool schemas
- [ ] Tool discovery
- [ ] Tool execution
- [ ] Tool permissions
- [ ] Plugin architecture
- [ ] External API integration
- [ ] Sandboxed execution
- [ ] Tool observability
- [ ] Tool failure handling

### Phase 7 — Agent Orchestration
**Status: 📋 Planned**
- [ ] Agent runtime
- [ ] Task planning
- [ ] Tool selection
- [ ] Multi-step execution
- [ ] Agent memory
- [ ] Workflow engine
- [ ] Multi-agent coordination
- [ ] Agent communication
- [ ] Failure recovery
- [ ] Human-in-the-loop workflows

### Phase 8 — Multimodal Intelligence
**Status: 📋 Planned**
- [ ] Text understanding
- [ ] Image understanding
- [ ] Audio understanding
- [ ] Video understanding
- [ ] Document vision
- [ ] Multimodal embeddings
- [ ] Cross-modal retrieval
- [ ] Multimodal reasoning

### Phase 9 — User Interfaces
**Status: 📋 Planned**
- [ ] Web interface
- [ ] Real-time streaming
- [ ] Conversation interface
- [ ] Knowledge explorer
- [ ] Agent workspace
- [ ] Tool management
- [ ] System dashboard
- [ ] Developer console
- [ ] Administration interface

### Phase 10 — Production Platform
**Status: 📋 Planned**
- [ ] CI/CD
- [ ] Automated deployment
- [ ] Cloud deployment
- [ ] Horizontal scaling
- [ ] Distributed tracing
- [ ] Metrics infrastructure
- [ ] Fault tolerance
- [ ] Backup and recovery
- [ ] Security hardening
- [ ] High availability
- [ ] Production observability

---

## 🔬 Research Directions

OMNIS is intended to serve as both an engineering platform and an experimental environment for AI systems research.

Potential research areas include:

**Persistent AI Memory**
Investigating how intelligent systems can selectively retain, consolidate, retrieve, and forget information.

**Context Engineering**
Developing mechanisms for dynamically constructing useful context from conversations, memories, documents, tools, and external knowledge.

**Agentic Systems**
Exploring planning, tool usage, multi-step execution, self-correction, and agent coordination.

**Retrieval-Augmented Intelligence**
Combining semantic retrieval, structured knowledge, external documents, and model reasoning.

**Multimodal Intelligence**
Investigating unified processing and retrieval across text, images, audio, video, and documents.

**AI Infrastructure**
Exploring reliable, observable, scalable infrastructure for long-running intelligent systems.

---

## 🔐 Security

Security is treated as a core architectural concern. The project will progressively introduce:

- Authentication
- Authorization
- Permission boundaries
- Secret isolation
- Sandboxed tool execution
- Audit trails
- Input validation
- Rate limiting
- Secure API practices

> Do not commit credentials, API keys, database passwords, or private configuration files.

---

## 🤝 Contributing

Contributions and technical discussions are welcome.

Before submitting a pull request, ensure that the following checks pass:
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy apps/api/src
uv run pytest
```

When contributing:
- Keep modules focused on a single responsibility.
- Prefer explicit interfaces over tightly coupled implementations.
- Add tests for new behavior.
- Maintain type safety.
- Keep API changes backward compatible where practical.
- Document significant architectural decisions.
- Avoid introducing unnecessary dependencies.

---

## 📌 Development Philosophy

OMNIS follows a foundation-first development strategy. Rather than immediately implementing high-level agent behavior, the project establishes reliable infrastructure first:

```text
                    FOUNDATION
                        │
                        ▼
                  API + Runtime
                        │
                        ▼
                    Persistence
                        │
                        ▼
                     Memory
                        │
                        ▼
                    Knowledge
                        │
                        ▼
                      Tools
                        │
                        ▼
                     Agents
                        │
                        ▼
                   Multimodal
                        │
                        ▼
                 Intelligence
                        │
                        ▼
                Production System
```

This approach is intended to prevent the common failure mode of building an impressive AI interface on top of fragile infrastructure.

---

## 📊 Project Maturity

| Component | Status |
|---|---|
| Project Foundation | ✅ Complete |
| FastAPI Backend | ✅ Complete |
| API Versioning | ✅ Complete |
| PostgreSQL | ✅ Complete |
| SQLAlchemy Async | ✅ Complete |
| Redis | ✅ Integrated |
| Alembic | ✅ Complete |
| Metadata Service | ✅ Complete |
| Unit Tests | ✅ Implemented |
| Integration Tests | ✅ Implemented |
| Static Type Checking | ✅ Implemented |
| Linting | ✅ Implemented |
| Docker Infrastructure | ✅ Implemented |
| Runtime Observability | 🚧 In Progress |
| Authentication | 📋 Planned |
| Memory Engine | 📋 Planned |
| Knowledge Engine | 📋 Planned |
| RAG | 📋 Planned |
| Tool Runtime | 📋 Planned |
| Agent Runtime | 📋 Planned |
| Multimodal Layer | 📋 Planned |
| Web Interface | 📋 Planned |
| Production Deployment | 📋 Planned |

---

## 📜 License

OMNIS is released under the MIT License. See the [LICENSE](LICENSE) file for the complete license text.

---

## 👨‍💻 Author

**Arvindh Babu V**
B.Tech — Artificial Intelligence and Data Science

Interested in:
- Artificial Intelligence
- Machine Learning
- Data Science
- Backend Engineering
- Distributed Systems
- Generative AI
- AI Agents
- Computer Vision

**Links**
- GitHub: [github.com/Arvindhbabu](https://github.com/Arvindhbabu)
- LinkedIn: [linkedin.com/in/arvindhbabuv23](https://www.linkedin.com/in/arvindhbabuv23/)

---

## ⭐ Support the Project

If you find OMNIS interesting, consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting improvements
- 🔧 Contributing code
- 📚 Sharing research ideas

<p align="center">
  <strong>OMNIS</strong><br>
  <em>Building infrastructure for persistent, extensible machine intelligence.</em>
</p>

<p align="center">
  <sub>Built with Python • FastAPI • PostgreSQL • Redis • Docker</sub>
</p>
