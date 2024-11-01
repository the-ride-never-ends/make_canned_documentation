
# Program: make_canned_documentation

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
11. Performance considerations - TODO
12. Scalability - TODO
13. Security considerations - TODO
14. Documentation needs - TODO


# 1. Problem Definition

## Objective: Create a documentation generator that converts natural language program descriptions into standardized technical documentation suitable for both human and AI implementation, with specific focus on reproducibility and completeness.

## Inputs
- Description: String containing program requirements
- Format: Plain text, UTF-8 encoded
- Delivery: Via API endpoint, terminal input, or uploaded file of arbitrary type (text, json, etc.)
- Length: Arbitrary
- Descriptiveness: Arbitrary
- Description Format: Arbitrary
- Language: English, with support for non-English inputs
- Input Validation 
    1. Input must be a string of non-zero length. If the input is empty, the program should return an error message indicating that the input is invalid.
    2. Input must be in a supported format (plain text, UTF-8 encoded). If the input is in an unsupported format, the program should return an error message indicating that the input format is unsupported.
- Maximum Size Limits: 10 MB per input. If the input exceeds this limit, the program should return an error message indicating that the input is too large.
- 

## Example Inputs
- 1. "Calendar scheduler."
- 2. "I wanna know what people think based on their Facebook posts."
- 3. "Create a web scraper that can extract user data from Linkedin profiles. The data should include the user's name, job title, company, location, and education in JSON format. It should follow ethical webscraping practices and respect user privacy."
- 4. "Make me a fucking sandwich."
- 5. "Objective: Develop a machine learning model to predict stock prices based on historical data. 
    Constraints:
    \1. The model should take into account various factors such as volume, price, and sentiment analysis of news articles. 
    \2. The output should be a prediction of the closing price for the next trading day."
- 6. ```json 
        {
            objective: "Create poetry from a specified subject matter.",
            inputs: {
                subject_matter: "A string containing the subject matter for the poetry.",
            }
        }
     ```

## Outputs
- Description: Software documentation files, each containing a specific aspect of the software's design and implementation.
- Format: GitHub-style Markdown files, UTF-8 encoded
- Delivery: Downloadble files of a specified format (zip, tar, etc.), either via API endpoint or uploaded to a specified location (e.g. GitHub repository, Google Drive, Selected Folder etc.)
- Length of Documents: Arbitrary
- Descriptiveness of Documents: Comprehensive and detailed
- Language: English, with support for non-English outputs

## Constraints:
1. Comprehensiveness
    - Documentation must be detailed enough to enable a programmer to completely and faithfully reproduce a program tha matches the input requirements with either minimal or no additional information.
2. Hiearcical structure
    - Documentation must be structured in a hierarchical manner, with clear section delineations, consistent formatting patterns, standard templating, and logical flow of information.
3. LLM as first class citizen
    - Documentation must take into account context window limitations, token count constraints, required formatting/prompting constraints, and handling of code blocks and special characters.
4. Semantic Clarity
    - Documentation must include a step-by-step breakdown of complex operations, avoid ambiguous language, use consistent termanology, and provide explicit relationships between components.
5. Validation Checkpoints
    - Unit test descriptions at key points and with expected intermediate outpoints, error detection and handling, and progress verification steps.
6. Memory Management
    - Program must be able to break down document generation into digestible chunks, manage documentation state across multiple LLM calls, handle cross-references between sections, and provide progressive disclosure of implementation details.
7. Error Recovery
    - Program must be able to detect when an LLM misunderstand or fails, have programatic fallback strategies and self-corretion mechanisms, and provide verification steps between major components.

## Specifications
- Markdown documentation files should consist of the following:
- 1. PRD.md (Product Requirements Document)
    - Overview of the program, its purpose, and its intended functionality.
    - User stories, use cases, and acceptance criteria.

- Format Requirements:
  - Valid GitHub Markdown syntax
  - Hierarchical structure
  - Code snippets (when needed) in code block format.
  - Diagrams (when needed) in Mermaid syntax.
  - Math equations (when needed) in LaTeX syntax.








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