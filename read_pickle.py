#!/usr/bin/python3
"""
Grab a bunch of pickle files at a search path, and write a CSV summary row for each one

Requires python3.11 or greater
"""

import logging
import pickle
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from pydantic import TypeAdapter
from typing_extensions import NotRequired, TypedDict


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


def load_and_parse(file: Path) -> Parsed:
    """Read a file in, validate the data and return it"""

    raw = pickle.loads(file.read_bytes())
    logging.debug(f"{raw=}")
    validated = TypeAdapter(Raw).validate_python(raw)
    parsed = Parsed(
        model_name=file.name,
        pLDDT=np.mean(validated["plddt"]),
        ipTM=validated.get("iptm", None),
        pTM=validated["ptm"],
    )
    logging.debug(f"{parsed=}")
    return parsed


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
        logging.info(f"reading file: {file}")
        parsed = load_and_parse(file)
        all_rows.append(parsed)

    pd.DataFrame(all_rows).set_index("model_name").to_csv(
        output_file
    )  # this gives us the CSV headers for free
