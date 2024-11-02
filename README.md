
# Program: make_canned_documentation

1. Problem definition
2. High-level architecture - TODO
3. Data structures - TODO
4. Algorithms - TODO
5. Function/method signatures - TODO
6. Error handling - TODO
7. Testing strategy - TODO
8. Code organization - TODO
9. Naming conventions - TODO
10. External dependencies - TODO
11. Performance considerations - TODO
12. Scalability - TODO
13. Security considerations - TODO
14. Documentation needs - TODO


# 1. Problem Definition

## Objective: Create a documentation generator that converts natural language program descriptions into standardized technical documentation suitable for both human and AI implementation, with specific focus on reproducibility and completeness.


## 1.1 Input
- 1.1.1 Description: String containing program requirements
- 1.1.2 Format: Plain text, UTF-8 encoded
- 1.1.3 Delivery: Via API endpoint, terminal input, or uploaded file of arbitrary type (text, json, etc.)
- 1.1.4 Length: Arbitrary
- 1.1.5 Descriptiveness: Arbitrary
- 1.1.6 Description Format: Arbitrary
- 1.1.7 Language: English, with support for non-English inputs
- 1.1.8 Maximum Size Limit: 4096 tokens.
- 1.1.9 Required Inputs: A string containing program requirements.
- 1.1.10 Optional Inputs: None

### 1.2 Input Processing
- 1.2.1 Input must be a string of non-zero length. If it is, return an error indicating that the input is invalid.
- 1.2.2 Input must be in a supported format (plain text, UTF-8 encoded). If it is not, return an error indicating that the input format is unsupported.
- 1.2.3 Input must be within the maximum size limit. If exceeded, return an error indicating that the input is too large.
- 1.2.4 Input must in intelligible language (e.g. not gibberish, ASCII art, etc.). If it is not, return an error indicating that the input is not intelligible.
- 1.2.5 Remove any non-text characters (e.g. images, emojis, etc.)
- 1.2.6 Trim leading/trailing whitespace.
- 1.2.7 If the input is not in UTF-8 encoding, the program should attempt to convert it to UTF-8 encoding. If the conversion fails, the program should return an error message indicating that the input encoding is unsupported.

## 1.3 Outputs
- 1.4.1 Description: Software documentation files, each containing a specific aspect of the software's design and implementation.
- 1.4.2 Format: GitHub-style Markdown files, UTF-8 encoded
- 3. Delivery: Downloadable files of a specified format (zip, tar, etc.), either via API endpoint or uploaded to a specified location (e.g. GitHub repository, Google Drive, Selected Folder, etc.)
- 4. Length of Documents: Arbitrary
- 5. Descriptiveness of Documents: Comprehensive and detailed.
- 6. Language: English, with support for non-English outputs.
- 7. Minimum Size: 5 documents of at least 1000 words each.


### 2.2 Outputs Success Criteria
- 1. The 5 core documents are generated.
    - 1. Documents are README.md, PRD.md, Architecture.md, Data_structures, Style.md
    - 2. Able to generate additional docs as needed or requested, including but not limited to:
        - 1. Algorithms
        - 2. Function/method signatures
        - 3. Error handling
        - 4. Testing strategy
        - 5. Code organization
        - 6. Naming conventions
        - 7. External dependencies,
        - 8. Performance considerations
        - 9. Scalability
        - 10. Security considerations
- 2. Each core documents has the correct subsections, format, and thoroughness, including but not limited to:
    - 1.4.2.2 Valid GitHub Markdown syntax
    - 1.4.2.3 Function/Method signatures with Google-style docstrings
    - 1.4.2.4 Code snippets (when needed) in code block format
    - 1.4.2.5 Diagrams (when needed) in Mermaid syntax
    - 1.4.2.6 Math equations (when needed) in LaTeX syntax
- 3. Each core document is accurate to its purpose, as determined by the user and/or using the LLM's own judgement.
- 4. Each core document meets the specified constraints as listed in the constraints section of this README.


## 3.2 Constraints:
1. Comprehensiveness
    - Documentation must be detailed enough to enable a programmer to completely and faithfully reproduce a program that matches the input requirements with either minimal or no additional information.
2. User Involvement Agnostic
    - Program should default to documentation being generated without requiring user interference beyond the input.
    - Allow for user input/feedback during the documentation generation process to clarify ambiguities or provide additional information.
    - Allow for user input/feedback to override the program's default behavior in order to generate documentation that meets the user's specific needs or correct mistakes made by the program.
2. Hierarchical structure
    - Documentation must be structured in a hierarchical manner.
    - Each document should have a clear purpose and scope.
    - Clear section delineations.
    - Standardized templating and formatting patterns.
    - Logical flow of information.
3. LLM as first class citizen
    - Written with context window and token count limitations.
    - Formatting/prompting constraints that adhere to 3rd party LLM APIs (e.g. OpenAI, Anthropic, Mistral, etc.).
    - Able to handle multiple LLM calls to generate documentation.
    - Respect LLM refusals to generate documentation based on their alignment or safety policies.
    - Special handling of code blocks, special characters, diagrams, and math equations.
4. Semantic Clarity
    - Must include a step-by-step breakdown of complex operations.
    - Avoid ambiguous and overly complicated language.
    - Use consistent terminology.
    - Provide explicit relationships between components.
5. Validation Checkpoints
    - Unit test descriptions at key points along with expected intermediate outpoints.
    - Error detection and handling at the function/method level.
    - Progress verification steps for each document.
    - Optional logging and debugging features to aid in troubleshooting and verification.
6. Memory Management
    - Able to break down document generation into discrete steps or chunks.
    - Manage documentation state across multiple LLM calls.
    - Handle cross-references between sections and documents.
    - Progressive disclosure of implementation details as documentation advances from foundational to specific elements.
7. Error Recovery
    - Able to detect when an LLM misunderstands, hallucinates, or fails outright.
    - Programmatic fallback strategies and self-correction mechanisms.
    - Programmatic and/or User verification steps between major components.
    - Ability to regenerate output on user request.
8. Resource Usage.
    - Efficient use of LLM resources (tokens, context window, etc.)
    - Minimize unnecessary LLM calls
    - Cache and reuse intermediate results
    - Optimize prompting strategies for efficient information retrieval and generation.
    - Minimize cost in time and money per document generated, with a preference for cost.
    - Maximum and minimum values for metrics to be determined based on testing and user feedback.
9. Scalability
    - Able to handle large software projects with numerous and complex documentation needs.
    - Able to handle multiple software projects concurrently.
10. Flexibility
    - Able to work as a standalone program, as an API, or as part of a larger software pipeline.
12. Dependencies
    - Able to work with a wide range of third-party libraries and tools, including but not limited to:
        - 1. Required
            - GitHub (for version control and hosting the documentation)
            - OpenAI, Anthropic, Mistral, etc. (for LLM services)
            - PyTest, JUnit, etc. (for unit testing)
            - Sphinx, Doxygen, etc. (for documentation generation)
        - 2. Optional
            - Docker (for containerization and deployment)
            - Kubernetes (for orchestration and scaling)
            - Augmentoolkit, Socialtoolkit (for synthetic dataset creation and annotation)
13. System Requirements
    - Able to run on a standard desktop or laptop computer with a modern operating system (Windows, MacOS, Linux).
14. Recovery and Rollback

## Example Outputs
### Example 
```
program_name: MyPythonApp
version: 1.0.0
author: John Doe and Claude 3.5
1. Problem definition
2. High-level architecture
3. Data structures
4. Algorithms
5. Function/method signatures
6. Error handling
7. Testing strategy
8. Code organization
9. Naming conventions
10. External dependencies
11. Performance considerations
12. Scalability
13. Security considerations
14. Documentation needs


# 1. Problem Definition
## Objective: Create a simple Python application that demonstrates the use of a 3-tier architecture and Agile development methodology.


## 1.1 Input
...
```

## Proposed Timeline
- Phased development
    - Phase 1: Python and 3-tier architecture documentation (MVP) - 6 months
    - Phase 2: Expand to other programming languages and architectures - 12 months
    - Phase 3: Expand to other software development methodologies and programming styles - 18 months

## Scope
1. Phase 1: Core Features
    - 1. Primary Software Project: Command-line applications
    - 1. Primary Languages: Python, MySQL, 
    - 2. Primary software architecture: 3-tier architecture
    - 2. Agile development methodology
    - 3. Object-oriented programming paradigm.
    - 3. Modular design with clear separation of concerns.

2. Phase 2: Future Enhancements
    - Later phases should be able to generate documentation for a wide range of software projects, including but not limited to:
        - 1. Web applications
        - 2. Mobile applications
        - 3. Desktop applications
        - 4. Command-line applications.
    - Support common general and domain-specific programming languages, including but not limited to:
        - 1. General Purpose: Python, Java, C++, C#, JavaScript, TypeScript, Go, Rust, Swift
        - 2. Domain-Specific: MySQL and other SQL dialects, R, STATA, and MatLab.
    - Support common software architectures, including but not limited to:
        - 1. Monolithic (e.g. single-tier, three-tier, etc.)
        - 2. Microservices (e.g. service-oriented, event-driven, etc.)
        - 3. Serverless (e.g. AWS Lambda, Google Cloud Functions, etc.)
        - 4. Cloud-native (e.g. Kubernetes, Docker, etc.)
        - 5. Edge computing (e.g. IoT, fog computing, etc.)
    - Support mainstream software development methodologies, including but not limited to:
        - 1. Agile (e.g. Scrum, Kanban, etc.)
        - 2. Waterfall (e.g. SDLC, V-model, etc.)
        - 3. Lean (e.g. Lean Startup, Lean Software Development, etc.)
        - 4. DevOps (e.g. CI/CD, Infrastructure as Code, etc.)
        - 5. Test-Driven Development (TDD)
    - Support a wide range of programming styles, including but not limited to:
        - 1. Object-oriented programming (OOP)
        - 2. Functional programming (FP)
        - 3. Procedural programming (PP)
        - 4. Event-driven programming (EDP)
        - 5. Reactive programming (RP)
        - 6. Asynchronous programming (AP)
    - Select a language(s), architecture, development methodology, and programming style that complement and are coherent with one another.
2. The program should not:
    - Support documentation for hardware projects, including but not limited to:
        - 1. Electronic circuits
        - 2. Mechanical designs
        - 3. Embedded systems.
    - Support documentation for non-software projects, including but not limited to:
        - 1. Business plans
        - 2. Research papers
        - 3. Technical reports.
    - Support documentation for projects that are not written in a programming language, including but not limited to:
        - 1. Visual design projects
        - 2. UX/UI projects
        - 3. Data analysis projects.
    - Create the software itself.


- Error Handling
    - 1. If the program encounters an error, it should return an error message indicating the nature of the error.
    - 2. If the error is recoverable, the program should attempt to recover from the error.
    - 3. If the error is not recoverable, the program should terminate and return an error message indicating that the program could not generate the documentation.
- Version Control
    - Storing the documentation in a GitHub repository
    - Default version control system is Git.
    - Optional support for Mercurial, or SVN. 
    - Option to allow the user to specify a version control system to use.




### TODO: Check to see what Codestral hallucinated. There's a lot of jargon here.


## Core Output Specifications
- Markdown documentation files should consist of the following:
- 1. PRD.md (Product Requirements Document)
    - Overview of the program, its purpose, and its intended functionality.
    - User stories, use cases, and acceptance criteria.









# Appendix A: Example Inputs
### 1.3 Example Inputs
- 1.3.1 "Calendar scheduler."
- 1.3.2 "I wanna know what people think based on their Facebook posts."
- 1.3.3 "Create a web scraper that can extract user data from Linkedin profiles. The data should include the user's name, job title, company, location, and education in JSON format. It should follow ethical web-scraping practices and respect user privacy."
- 1.3.4 "Make me a sandwich yesterday."
- 1.3.5 "Objective: Develop a machine learning model to predict stock prices based on historical data.
    Constraints:
    \1. The model should take into account various factors such as volume, price, and sentiment analysis of news articles.
    \2. The output should be a prediction of the closing price for the next trading day."
- 1.3.6 ```json
        {
            objective: "Create poetry from a specified subject matter.",
            inputs: {
                subject_matter: "A string containing the subject matter for the poetry.",
            }
        }
     ```













- 1. README.md
   - Project overview, system requirements, and general architecture design. 
- 2. architecture.md
   - Specific high-level architecture, including modules, components, and their interactions.
   - Structured in a hiearchical manner, 
- 3. style.md
   - Coding style, naming conventions, and documentation standards.
- 4. testing.md
   - Testing strategy, including unit tests, integration tests, and system tests.
   - Formatted as a traceability matrix, with each test case linked to the corresponding requirement or design decision.


## Constraints:
1. Comprehensive: Documentation must be detailed enough to enable a programmer to completely and faithfully reproduce the program with either minimal or no additional information.
2. Lifeform agnostic: Documentation must be written in a way that is understandable and useful to both human and AI developers.

2. Scalability:
   - 
3. Performance:
   - 
4. Reliability: 
   - 
5. Maintainability: 
   - 
6. Robustness:
   - 
7. Output format: Human-readable plaintext.


## Scope:
1. Geographic Coverage:
   - 
2. Timeframe
   - 
3. Language
   - 
4. Content Completeness
   - 
5. Data validation:
   - 
6. Error handling: 
   - 
7. Legal compliance
   - Respect copyright laws and terms of service. 



## Data Integrity and Verification:
   - 
## Scalability Plans
   - 
## Update Process:
   - 


## Use cases:
1. Constructing
   - Key Metric: Size of Dataset
2.  researchers:
   - Key Metric: Accuracy
3. Lgal professionals: 
   - Key Metric: Accuracy
4. ML researchers: Train models.
   - Key Metric: Size
5. analysts: Compare
   - Key Metric: Accuracy


# 2. High-Level Architecture
1. **Input Processing Module 'input.py'**


2. **Search Engine Interface 'search.py'**


3. **Query Generator 'query.py'**


4. **Scraping Module 'BLANK'**


12. **Scalability Management Module 'scale.py'**


13. **API/Interface Module 'api.py'**

14. **Scheduler 'schedule.py'**



# 3. Data Structures
## 1. In-Memory Data Structures:

## 2. Database Structures

## 3. File Structures



# 4. Algorithms
# 4.1 Search Query Generation
1. Input:
   - 
- Process:
  1. 
- Output: Formatted search query and associated metadata.

# 4.4 Content Extraction and Cleaning
- Input:
- Process:
  1. 
- Output: 

# 4.5 Update Detection
- Input: 
- Process:
  1. 
- Output:


## 4.1.1 Specific details for Search Query Generation:
1. Query formats for different search engines:
   - 

2. Handling synonyms or related terms:
   - 

3. Incorporating location-specific information:
   - 

4. Avoiding search engine detection and blocking:
   - 

5. Query construction and optimization:
   - 
6. Query storage and management:
   - 

7. Error handling and edge cases:
   - 

8. Compliance and ethical considerations:
   - 

9. Performance optimization:
   - 

10. Integration with other system components:
   - 

# 5. Function/method signatures
   - 
# 6. Error handling
   - 

# 7. Testing strategy
   - 

# 8. Code organization
   - 

# 9. Naming conventions
   1. Python conforms to PEP8 naming conventions.
      - Variables and functions are named use lowercase with underscores.
      - Classes use CamelCase.
      - Constants and global variables use ALL_CAPS.
      - Private variables and methods are named using a single underscore prefix.
      - 3rd party libraries are imported using staandard naming conventions (e.g. import pandas as pd).
      - Utility file namings follow the same conventions as their primary function or class (e.g. AsyncPlaywrightScrapper class is in AsyncPlaywrightScrapper.py)
      - Critical orchestration files are one word, undercase (e.g. database.py)
      - **TODO: Standardization of formats**
   2. MySQL follows standard SQL naming conventions.
      - Tables and input and output variables are named using lowercase with underscores.
      - Commands are written in ALL CAPS.


# 10. External dependencies
   - 


11. Performance considerations - TODO
12. Scalability - TODO
13. Security considerations - TODO
14. Documentation needs - TODO