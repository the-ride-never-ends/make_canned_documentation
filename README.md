# Program: make_canned_documentation
Version: 0.1.1

## Table of Contents
1. Problem Definition
2. Requirements Matrix
3. System Requirements
4. Constraints
5. Implementation Phases
6. Dependencies

# 1. Problem Definition

## 1.1 Objective
Create a software documentation generator that converts natural language program descriptions into standardized technical documentation suitable for both human and AI implementation, with specific focus on exact reproducibility and completeness.

## 1.2 Input Specifications
| Attribute        | Specification                                       | Bounds/Constraints                      |
|------------------|-----------------------------------------------------|-----------------------------------------|
| Description      | Text containing program requirements                | Non-zero length                         |
| Format           | Plain text, UTF-8 encoded                           | Must be convertible to UTF-8            |
| Size             | Variable                                            | Max: 4096 tokens                        |
| Language         | Primary: English                                    | Support for detected non-English inputs |
| Delivery Methods | - API endpoint<br>- Terminal input<br>- File upload | File types: .txt, .json, .md            |

## 1.3 Input Processing Requirements
1. Validation
   - Non-zero length verification
   - Format compatibility check
   - Size limit enforcement
   - Language intelligibility assessment (e.g. not gibberish, ASCII art, etc.)

2. Preprocessing
   - Non-text character removal (e.g. images, emojis, etc.)
   - Whitespace normalization
   - Encoding standardization

## 1.4 Outputs

### 14.1 Output Specifications
| Attribute        | Specification                                       | Bounds/Constraints                                      |
|------------------|-----------------------------------------------------|---------------------------------------------------------|
| Description      | Software documentation files                        | - Min: 5 Core Docs (P0)<br>- Max: 10 Extended Docs (P1) |
| Content          | Technical documentation based on input description  | See Section 1.4.3 'Output Content Requirements'         |
| Format           | Plain text, UTF-8 encoded                           | See Section 1.4.3 'Output Format Requirements'          |
| Size             | Variable                                            | - Min: 20480 tokens<br>- Max: 40960 tokens              |
| Language         | Primary: English                                    | Support for non-English outputs                         |
| Delivery Methods | - API endpoint<br>- File download                   | File types: .txt, .json, .md                            |

### 1.4.1 Core Documentation Set (P0)
| Document           | Minimum Length  | Purpose                    |
|--------------------|-----------------|----------------------------|
| README.md          | 4096 tokens     | Project overview and setup |
| PRD.md             | 4096 tokens     | Product requirements       |
| Architecture.md    | 4096 tokens     | System design              |
| Data_Structures.md | 4096 tokens     | Data organization          |
| Style.md           | 4096 tokens     | Coding standards           |

### 1.4.2 Extended Documentation Set (P1)
| Document      | Minimum Length | Purpose                 |
|---------------|----------------|-------------------------|
| Algorithms.md | 4096 tokens    | Algorithm descriptions  |
| API.md        | 4096 tokens    | API documentation       |
| Testing.md    | 4096 tokens    | Testing procedures      |
| Deployment.md | 4096 tokens    | Deployment instructions |
| Security.md   | 4096 tokens    | Security measures       |

### 1.4.3 Output Format Requirements
1. Document Structure
   - GitHub-flavored Markdown
   - Hierarchical organization
   - Cross-document referencing
   - Version control compatible

2. Content Elements
   - Natural Language
   - Code blocks (```language)
   - Mermaid diagrams
   - LaTeX equations
   - Tables and lists
   - Google-style function signatures

## 1.5 Critical Path Requirements

### 1.5.1 Performance Metrics
| Metric                     | Threshold       | Optimal         |
|----------------------------|-----------------|-----------------|
| Doc Generation Time        | < 5 minutes/doc | < 2 minutes/doc |
| Token Usage                | < 4000/doc      | < 2000/doc      |
| API Calls                  | < 10/doc        | < 5/doc         |
| Error Rate                 | < 5%            | < 1%            |
| Documentation Quality*     | >= 85%          | >= 95%          |

*See section 1.5.2 'Quality Metrics' for details.
### 1.5.2 Quality Metrics
Documentation Quality is an average of the following metrics, each weighted according to their importance to the documentation's overall quality.

| Metric                        | Description                                                                   | Threshold | Optimal | Weight |
|-------------------------------|-------------------------------------------------------------------------------|-----------|---------|--------|
| Purpose Alignment             | How well a doc's content aligns with the doc's intended purpose               | >= 90%    | >= 99%  | 25%    |
| Readability (Flesch-Kincaid)  | How easily the doc can be understood                                          | >= 60     | >= 80   | 12%    |
| Internal Coherency            | How coherent a doc is at a logical level                                      | >= 90%    | >= 95%  | 20%    |
| External Coherency            | Coherence compared with the other docs and the project and user requirements  | >= 90%    | >= 95%  | 20%    |
| Completeness                  | All required sections present and filled                                      | >= 90%    | >= 95%  | 15%    |
| Format Compliance             | Format follows the requirements in section 1.4.3 'Output Format Requirements' | >= 90%    | >= 95%  | 8%     |

Each document is scored by an advanced LLM (e.g. GPT4, Claude 3.5 Sonnet, etc.) on a section-by-section basis based on a pass/fail judgement. Rubrics for these metrics are in the prompts folder. Readability is calculated programmatically based on a Flesch-Kincaid readability test. All metrics are normalized to [0-1] before weights are applied.

### 1.5.2 Feature Priority Matrix
| Feature                 | Priority | Phase | Success Criteria                 |
|-------------------------|----------|-------|----------------------------------|
| Core Doc Generation     | P0       | 1     | 5 core docs generated            |
| Extended Doc Generation | P1       | 2     | 5 extended docs generated        |
| Multi-language Support  | P2       | 3     | Python, JS, MySQL support        |
| Advanced Architectures  | P3       | 4     | Microservices, serverless        |

## 1.6 Backup and Recovery
1. Documentation State
   - Autosave every 5 minutes
   - Checkpoint after each major section
   - Local cache of intermediate results

2. Error Recovery
   - Automatic retry on API failures
   - Fallback to cached results
   - Manual override options for LLM generation

## 1.7 Version Control
1. Documentation Versioning
   - Semantic versioning (MAJOR.MINOR.PATCH)
   - Git commit hooks for validation
   - Automated changelog generation

2. Version Control Integration
   - Primary: Git
   - Optional: Mercurial, SVN
   - Branch strategy enforcement

## 1.8 System Requirements

### 1.8.1 Hardware Requirements
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU       | 2 cores | 4+ cores    |
| RAM       | 4GB     | 8GB+        |
| Storage   | 1GB     | 5GB+        |
| Network   | 1Mbps   | 10Mbps+     |

### 1.8.2 Software Requirements
| Component | Required Version |
|-----------|------------------|
| Python    | 3.10+            |
| Git       | 2.0+             |


## 1.9 Constraints
1. Technical Constraints
   - Context size limits (4096 tokens per API call)
   - API rate limits
   - Memory usage limits
   - Network bandwidth limits

2. Business Constraints
   - Cost per document < $0.50
   - Monthly API budget < $1000
   - Support response time < 24h

3. Legal Constraints
   - GDPR compliance
   - Data retention policies
   - License compatibility

4. Ethical Constraints
   - AI alignment policies
   - Hippocratic oath principal


## 1.10 Example Input and Output
### 1.10.1 Example Inputs
- "Calendar scheduler."
- "I wanna know what people think based on their Facebook posts."
- "Create a web scraper that can extract user data from Linkedin profiles. The data should include the user's name, job title, company, location, and education in JSON format. It should follow ethical web-scraping practices and respect user privacy."
- "Make me a sandwich yesterday."
- "Objective: Develop a machine learning model to predict stock prices based on historical data.
    Constraints:
    \1. The model should take into account various factors such as volume, price, and sentiment analysis of news articles.
    \2. The output should be a prediction of the closing price for the next trading day."
- ```json
        {
            objective: "Create poetry from a specified subject matter.",
            inputs: {
                subject_matter: "A string containing the subject matter for the poetry.",
            }
        }
     ```

### 1.10.2 Example Output
```text
# MyPythonApp
Version: 1.0.0
Authors: John Doe, Claude 3.5 Sonnet

## Overview
Three-tier Python application demonstrating Agile methodology...
[Additional sections follow standard template]
```

## 1.11 Scope Definition

### 1.11.1 Minimum Viable Product (MVP)
| Feature            | Description                          | Success Criteria                                                                                          |
|--------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Basic Doc Creation | Create README.md and PRD.md only     | - Successfully makes both docs <br>- Meets quality metrics (Section 1.5.2)<br>- Completes in < 5 minutes |
| Single Language    | English-only input/output            | - Correctly processes English text <br>- Rejects non-English inputs                                       |
| File Input         | .txt and .md file processing         | - Successfully reads both file types <br>- Handles UTF-8 encoding                                         |
| Error Handling     | Input validation and error reporting | - Catches and reports common errors <br>- Provides clear error messages                                   |

## 1.11.2 Explicitly Out of Scope
| Feature                      | Description                                                                                                |
|------------------------------|------------------------------------------------------------------------------------------------------------|
| Real-time Documentation      | - Live document updates <br>- Websocket connections <br>- Real-time collaboration                          |
| Advanced Features            | - Code generation <br>- Test case generation <br>- Automated implementation <br>- Custom template creation |
| Integration Features         | - CI/CD pipeline integration <br>- IDE plugins <br>- Direct repository management                          |
| Authentication/Authorization | - User management <br>- Role-based access <br>- Multi-tenant support                                       |


## 1.11 Dependencies

### 1.11.1 External Services
TODO: GO through all of these and make sure they're correct. 
This seems like the perfect spot for an LLM to hallucinate things.

| Service    | Purpose                       | Min Version | Alternatives           | Criticality |
|------------|-------------------------------|-------------|------------------- ----|-------------|
| OpenAI API | Core documentation generation | GPT-4       | Claude, PaLM           | Critical    |
| GitHub API | Version control integration   | v3          | GitLab API             | Important   |
| MySQL API  | Document storage and backup   | Latest      | Azure Blob, AWS S3/GCS | Important   |

### 1.11.2 Python Libraries
| Library       | Purpose                             | Min Version | License | Updates    |
|---------------|-------------------------------------|-------------|---------|------------|
| augmentoolkit | LLM orchestration                   | 0.1.0       | MIT     | Monthly    |
| numpy         | Numerical computations              | 1.24.0      | BSD     | Quarterly  |
| pandas        | Data manipulation                   | 2.0.0       | BSD     | Quarterly  |
| fastapi       | API framework                       | 0.100.0     | MIT     | Monthly    |
| pydantic      | Data validation                     | 2.0.0       | MIT     | Monthly    |
| pytest        | Testing framework                   | 7.0.0       | MIT     | Quarterly  |

### 1.11.3 Development Tools
| Tool           | Purpose                             | Min Version | Required    |
|----------------|-------------------------------------|-------------|-------------|
| Poetry         | Dependency management               | 1.5.0       | Yes         |
| Pre-commit     | Git hooks                           | 3.3.0       | Yes         |
| Black          | Code formatting                     | 23.3.0      | Yes         |
| Ruff           | Linting                             | 0.1.0       | Yes         |
| mypy           | Type checking                       | 1.4.0       | Yes         |

### 1.11.4 Dependency Management
1. Version Control
   - Strict semantic versioning
   - Lock file maintenance
   - Automated dependency updates via Dependabot

2. Security
   - Weekly vulnerability scanning
   - License compliance checking
   - SBOM generation

3. Performance Impact
   - Maximum total package size: 100MB
   - Maximum cold start time: 5s
   - Maximum memory overhead: 500MB

### 1.11.5 Fallback Strategies
| Dependency     | Fallback Strategy                   | Data Migration | Recovery Time |
|----------------|-------------------------------------|----------------|---------------|
| OpenAI API     | Switch to Claude API                | Not needed     | < 5 minutes   |
| GitHub API     | Local Git operations                | Manual sync    | < 30 minutes  |
| FastAPI        | Fallback to Flask                   | Not needed     | < 60 minutes  |

### 1.11.6 Dependency Update Policy
1. Critical Updates
   - Security patches: Immediate deployment
   - Bug fixes: Within 24 hours
   - Feature updates: Monthly review

2. Non-Critical Updates
   - Scheduled monthly updates
   - Tested in staging environment
   - Rollback plan required

3. Update Verification
   - Automated testing suite
   - Integration test coverage
   - Performance benchmark comparison