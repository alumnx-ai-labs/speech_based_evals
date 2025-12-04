from typing import TypedDict, List, Dict, Any, Optional

class EvaluationResult(TypedDict):
    model_name: str
    evaluation: str
    input_tokens: int
    output_tokens: int
    cost: float

class GraphState(TypedDict):
    audio_path: str
    transcription: Optional[str]
    transcription_cost: float
    evaluations: List[EvaluationResult]
    total_cost: float
    errors: List[str]
