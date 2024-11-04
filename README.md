# Program: make_canned_documentation
Version: 0.1.1

## Table of Contents
1. Problem Definition
2. Requirements Matrix
3. System Requirements
4. Constraints
5. Implementation Phases
6. [Future sections to be completed]

# 1. Problem Definition

## 1.1 Objective
Create a software documentation generator that converts natural language program descriptions into standardized technical documentation suitable for both human and AI implementation, with specific focus on reproducibility and completeness.

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

Each document is scored by an LLM on a section-by-section basis based on a pass/fail judgement. Rubrics for these metrics are in the prompts folder.
Note: Readability is calculated programmatically based on a Flesch-Kincaid readability test.

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
   - Manual override options

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
   - Token limits (4096 per API call)
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
   - Hippocratic oath policies
   - License compatibility

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
```markdown
# MyPythonApp
Version: 1.0.0
Authors: John Doe, Claude 3.5 Sonnet

## Overview
Three-tier Python application demonstrating Agile methodology...
[Additional sections follow standard template]
```