from sqlmodel import SQLModel, Field


class Benchmark(SQLModel, table=True):
    request_id: str = Field(
        description="Unique identifier for the benchmarking request.",
        default=None,
        primary_key=True,
    )
    prompt_text: str = Field(description="The input prompt text used for the LLM.")
    generated_text: str = Field(description="The output text generated by the LLM.")
    token_count: int = Field(description="The number of tokens in the generated text.")
    time_to_first_token: int = Field(
        description="The time taken to generate the first token (in milliseconds)."
    )
    time_per_output_token: int = Field(
        description="The average time per output token (in milliseconds)."
    )
    total_generation_time: int = Field(
        description="The total time to generate the response (in milliseconds)."
    )
    timestamp: str = Field(
        description="The timestamp when the benchmarking result was recorded."
    )
