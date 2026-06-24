import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.main import app  # noqa: E402


def test_seeded_lab_data_shape() -> None:
    corpus_path = ROOT / "data" / "corpus_vn.jsonl"
    golden_path = ROOT / "data" / "golden_set.jsonl"

    corpus = [json.loads(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]
    golden = [json.loads(line) for line in golden_path.read_text(encoding="utf-8").splitlines()]

    assert len(corpus) == 1000
    assert len(golden) == 50
    assert {"doc_id", "topic", "title", "text"} <= corpus[0].keys()
    assert {"query", "topic", "mode_hint", "relevant_doc_ids"} <= golden[0].keys()


def test_fastapi_search_route_is_registered() -> None:
    routes = {route.path for route in app.routes}
    assert {"/", "/healthz", "/search"} <= routes
