from typing import Union
from datetime import datetime
from json import load

from .models import Benchmark, BenchmarkStatistic


def validate_timestamp(ts: str) -> bool:
    try:
        ts = datetime.fromisoformat(ts)
    except Exception as er:
        return False


def parse_timestamp(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def get_data(filename: str = "") -> dict[str, list[Union[str, int]]]:
    with open(filename, "r", encoding="utf-8") as fp:
        return load(fp)


def get_benchmark_results(start_time: datetime = None, end_time: datetime = None):
    data = get_data("test_database.json").get("benchmarking_results", {})
    results = [Benchmark(**item) for item in data]
    if all((start_time, end_time)):
        results = [
            item
            for item in results
            if start_time <= datetime.fromisoformat(item.timestamp) <= end_time
        ]

    return results


def get_average_stats(benchmark_results: list[Benchmark]) -> BenchmarkStatistic:
    avg = lambda items, field: sum([getattr(item, field) for item in items]) / len(
        items
    )
    average_statistic = BenchmarkStatistic(
        avg_token_count=avg(benchmark_results, "token_count"),
        avg_time_to_first_token=avg(benchmark_results, "time_to_first_token"),
        avg_time_per_output_token=avg(benchmark_results, "time_per_output_token"),
        avg_total_generation_time=avg(benchmark_results, "total_generation_time"),
    )
    return average_statistic
