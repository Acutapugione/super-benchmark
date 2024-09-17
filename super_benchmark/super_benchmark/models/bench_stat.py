from sqlmodel import SQLModel, Field


class BenchmarkStatistic(SQLModel):
    avg_token_count: float = Field(
        description="The average number of tokens in the generated text."
    )
    avg_time_to_first_token: float = Field(
        description="The average time taken to generate the first token (in milliseconds)."
    )
    avg_time_per_output_token: float = Field(
        description="The average time per output token (in milliseconds)."
    )
    avg_total_generation_time: float = Field(
        description="The average total time to generate the response (in milliseconds)."
    )
