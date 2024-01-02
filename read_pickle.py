#!/usr/bin/python3
"""
Grab a bunch of pickle files at a search path, and write a CSV summary row for each one

Requires a pretty recent python
"""

import logging
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from pydantic import TypeAdapter
from typing_extensions import NotRequired, TypedDict

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Parsed:
    """A row of the final table CSV, constructed from each file"""

    model_name: str
    pLDDT: float
    """averaged"""
    ipTM: float | None
    """only present for multimers"""
    pTM: float


class Raw(TypedDict):
    """The expected format on disk, used for validation"""

    plddt: list[float]
    """per-residue"""
    iptm: NotRequired[float]  # TODO(aatifsyed): is this right?
    """only present for multimers"""
    ptm: float


def parse_from_file(file: Path) -> Parsed:
    """Read a file in, validate the data and return it, with appropriate logging"""

    raw = pickle.loads(file.read_bytes())
    logger.debug(f"{raw=}")
    parsed = parse_raw(model_name=file.name, raw=raw)
    logger.debug(f"{parsed=}")
    return parsed


def parse_raw(model_name: str, raw: Any) -> Parsed:
    validated = TypeAdapter(Raw).validate_python(raw)
    return Parsed(
        model_name=model_name,
        pLDDT=np.mean(
            validated["plddt"]
        ),  # TODO(aatifsyed): how should we handle an empty list?
        ipTM=validated.get("iptm", None),
        pTM=validated["ptm"],
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Expected to be run from editor, so hardcode input and output
    search_folder = Path(
        "/Users/gabrielleadmans/Documents/_11 Computational/2023-12-29_Good_AF_SnC2_models/"
    )
    output_file = search_folder.joinpath(
        f"{datetime.today().strftime('%Y-%m-%d')}_AF_confidence_values.csv"
    )

    all_rows = []
    for file in filter(
        Path.is_file,  # `Path.glob` can returns files AND folders, which could break our code, so `filter` to only include files
        search_folder.glob("*.pkl"),  # we could make this recursive if required
    ):
        logger.info(f"reading file: {file}")
        parsed = parse_from_file(file)
        all_rows.append(parsed)

    pd.DataFrame(all_rows).set_index("model_name").to_csv(
        output_file
    )  # this gives us the CSV headers for free


def test():
    assert parse_raw("sample", {"plddt": [2], "ptm": 1}) == Parsed(
        "sample", 2.0, None, 1
    )
