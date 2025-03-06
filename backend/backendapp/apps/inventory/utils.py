import time
from django.db import connection, reset_queries
from collections import defaultdict
from functools import wraps
from django.conf import settings


def query_inspect(func=None, *, detail=False):
    if func is None:
        return lambda f: query_inspect(f, detail=detail)

    @wraps(func)
    def inner_func(*args, **kwargs):
        if settings.DEBUG:
            reset_queries()
            start_queries = len(connection.queries)
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            end_queries = len(connection.queries)
            if detail:
                query_count = defaultdict(int)
                for query in connection.queries:
                    query_count[query["sql"]] += 1
                print("\nDetailed SQL Query Analysis:")
                for sql, count in query_count.items():
                    print(f"Query: {sql}\nCount: {count}\n")
            print(
                f"Function {func.__name__} / {end_queries - start_queries} qrs; "
                f"{(end - start):.3f}s"
            )
        else:
            result = func(*args, **kwargs)
        return result

    return inner_func
