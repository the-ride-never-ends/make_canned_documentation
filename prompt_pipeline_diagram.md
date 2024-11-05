**README.md Prompt 1: Clarify User Input**
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart LR
    style G stroke:#90EE90,stroke-width:2px
    style A stroke:#90EE90,stroke-width:2px
    subgraph Clarify User Input
        A@{shape: manual-input, label: "User Input"} --> C{Judge user input for clarity of purpose}
        C -->|Input is Unclear| D{Ask for clarification}
        C -->|Input is Clear| G@{shape: in-out, label: "Clarified User Input"}
        D -.-> A
        D -->|User Refuses to Clarify| F[Acknowledge refusal]
        F --> 5@{ shape: dbl-circ, label: "END PROGRAM" }
    end
**README.md Prompt 2: Create Program Objective**
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart LR
    style E stroke:#90EE90,stroke-width:2px
    style Y stroke:#90EE90,stroke-width:2px
    subgraph Create Program Objective
        E@{ shape: out-in, label: "Clarified User Input" } --> F
        F[Formulate objective] --> G@{ shape: procs, label: "Grade Objective according to each output quality rubric"}
        G -->|All Pass| H[Program Objective]
        G -->|At Least One Failure| Z@{shape: loop-limit, label: "Retry Limit"}
        Z --> K[Generate Constructive Criticism for Each Failure]
        K --> I[Reformulate objective based on constructive criticism]
        I --> G
        Z -->|Limit Reached| 5@{ shape: dbl-circ, label: "END PROGRAM" }
        H --> A@{shape: manual-input, label: "Optional User Approval"}
        A --> |Disapprove| I
        A --> |Approve| Y@{shape: in-out, label: "Approved Program Objective"}
    end

**Prompt Pipeline Architecture: Cumulative Review**
flowchart LR
    style Y stroke:#90EE90,stroke-width:2px
    style A stroke:#90EE90,stroke-width:2px
    subgraph Pipeline
        4@{shape: procs, label: "Cumulative Documentation via Recursive Search, Vector Embeddings"} --> B
        4 --> C
        4 --> D
        4 --> F
        4 --> G
    end
    subgraph Pipeline
        A@{shape: manual-input, label: "User Input"} --> B[README.md]
        B --> C[PRD.md]
        C --> D[Architecture.md]
        D --> E[Data_Structures.md]
        E --> F[Style.md]
        F --> G[Additional Documentation]
        G --> H{Final Document Review}
        H --> |Pass| Y@{shape: in-out, label: "Final Document Set"}
        H --> |Fail| Z@{shape: dbl-circ, label: "END PROGRAM"}
    end

**README.md Prompt 3: Create Input Specifications**
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart LR
    subgraph Create Objective
        E@{ shape: out-in, label: "Clarified User Input" } --> F
        F[Formulate objective] --> G@{ shape: procs, label: "Grade Objective according to output quality rubric"}
        G -->|Pass| H@{shape: in-out, label: "Program Objective"}
        G -->|Fail| I[Reformulate objective based on feedback from rubric]
        I -.-> Z@{shape: loop-limit, label: "Retry Limit"} -.-> F
        Z -->|Limit Reached| 5@{ shape: dbl-circ, label: "END PROGRAM" }
    end

