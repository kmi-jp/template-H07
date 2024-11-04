import pathlib
import os
import json

expected = {
    "L01E01": 39,
    "L01E02": 38,
    "L01E03": 38,
    "L01E04PEP": 38,
    "L02E01": 36,
    "L02E02": 35,
    "L02E03": 35,
    "L02E04PEP": 37,
    "L03E01": 36,
    "L03E02": 31,
    "L04E01": 31,
    "L04E02": 32,
    "L04E03": 29,
    "L05E01": 31,
    "L05E02": 21,
    "L06E01": 17,
    "L06E02": 5,
}


def test_sum_points(script_runner):
    script_runner.run("sum_points.py")

    output_file = pathlib.Path.cwd() / "output.json"

    output_dict = json.loads(output_file.read_text())

    assert expected == output_dict
