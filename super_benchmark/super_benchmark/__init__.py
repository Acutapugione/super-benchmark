from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlmodel import SQLModel, Field
import uvicorn

from .models import Benchmark, BenchmarkStatistic
from .data_processing import (
    get_average_stats,
    validate_timestamp,
    parse_timestamp,
    get_benchmark_results,
)

load_dotenv()  # Comment this if env variables not in .env file
DEBUG = getenv("SUPERBENCHMARK_DEBUG") != "False"
if not DEBUG:
    raise NotImplementedError("the feature is not ready for live yet")
app = FastAPI(
    title="SuperBenchmark",
    debug=DEBUG,
)


@app.get("/results/average", response_model=BenchmarkStatistic)
@app.get("/results/average/{start_time}/{end_time}", response_model=BenchmarkStatistic)
def average_results(start_time: str = "", end_time: str = ""):

    if all(
        [
            validate_timestamp(start_time),
            validate_timestamp(end_time),
        ]
    ):
        start_time, end_time = parse_timestamp(start_time), parse_timestamp(end_time)
        benchmark_results = get_benchmark_results(start_time, end_time)
    else:
        benchmark_results = get_benchmark_results()
    return get_average_stats(benchmark_results)


def run():
    uvicorn.run("super_benchmark:app", port=5000, log_level="info")
