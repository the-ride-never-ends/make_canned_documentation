


graph TD
    A[Start] --> B{Is it raining?}
    B -->|Yes| C[Take an umbrella]
    B -->|No| D[Enjoy the weather]
    C --> E[Go outside]
    D --> E
    E --> F[End]

graph Prompt Pipeline
    1[Start] --> 2{Judge user input for clarity of purpose}
    2 -->|Unclear| 3{Ask for clarification}
    2 -->|Clear| 4{Formulate objective}
    2 -->|Refuse| 5[Acknowledge refusal and end]
    5 --> 5[End]



