graph TB
    Input[Input Handler]
    Validator[Input Validator]
    Processor[Doc Processor]
    LLM[LLM Service]
    Generator[Doc Generator]
    QA[Quality Assurance]
    Output[Output Handler]
    Cache[(Cache Store)]
    Storage[(Document Storage)]
    
    Input --> Validator
    Validator --> Processor
    Processor --> LLM
    LLM --> Generator
    Generator --> QA
    QA --> Output
    
    Processor --> Cache
    Generator --> Storage
    
    subgraph Input Layer
        Input
        Validator
    end
    
    subgraph Processing Layer
        Processor
        LLM
        Generator
    end
    
    subgraph Quality Layer
        QA
    end
    
    subgraph Storage Layer
        Cache
        Storage
    end


graph TB
    Input[User Input] --> VectorStore[(Vector Store)]
    VectorStore --> ParallelTrack
    
    subgraph ParallelTrack
        README[README.md] --> |Core Track| PRD[PRD.md]
        README --> |Infrastructure Track| Style[Style.md]
        PRD --> Architecture[Architecture.md]
        Style --> DataStructures[Data_Structures.md]
    end
    
    ParallelTrack --> QualityGate{Quality Gate}
    QualityGate -->|Pass| Extended[Additional Documentation]
    QualityGate -->|Fail| Revision[Revision Process]
    
    Revision --> ParallelTrack
    Extended --> FinalReview{Final Review}
    
    FinalReview -->|Pass| Output[Final Document Set]
    FinalReview -->|Fail| Revision
    
    subgraph Continuous
        VectorStore -.->|Update| ParallelTrack
        Output -.->|Feedback| VectorStore
    end