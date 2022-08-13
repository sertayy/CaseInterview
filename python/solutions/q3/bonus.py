import sys
import os
import logging
from typing import Tuple

logging.getLogger().setLevel(logging.INFO)


class KnownException(Exception):
    None


def validate_clock(elem):
    partition_index = elem.find(":")
    if partition_index == -1:
        raise KnownException("Invalid time format! Use \":\" for the time splitter.")
    hr, mnt = int(elem[:partition_index]), int(elem[partition_index + 1:])
    if not 0 < hr <= 12:
        raise KnownException("The time is not valid. Use 12-hour format!")
    elif not 0 <= mnt <= 59:
        raise KnownException("The time is not valid. Minute range is not correct!")
    return hr, mnt


def calc_angle(hr: int, mnt: int) -> Tuple[float, bool]:
    mnt_angle = 6 * mnt
    hr_angle = 30 * hr + mnt_angle / 12
    angle_between = hr_angle - mnt_angle
    if -180 < angle_between < 0:
        return abs(angle_between), True
    elif angle_between > 180:
        return -angle_between % 180, True
    elif angle_between < -180:
        return angle_between % 180, False
    else:
        return angle_between, False


def calc_results(clocks):
    angles = []
    for elem in clocks:
        try:
            hr, mnt = validate_clock(elem)
            angles.append(calc_angle(hr, mnt))
        except KnownException as ex:
            logging.info("The clock in the {0}. line of the csv file is skipped due to an error."
                         .format(clocks.index(elem) + 2))
            logging.error(ex)
        except Exception as ex:
            logging.exception(ex)
    return angles


def read_file(in_path):
    try:
        with open(in_path) as infile:
            clocks = infile.readlines()[1:]
    except Exception as ex:
        logging.info(ex)
    return clocks


def write_file(angles):
    with open("results.csv", "wb") as outfile:
        outfile.write("angle,clockwise\n".encode("utf-8"))
        for angle in angles:
            outfile.write("{0},{1}\n".format(angle[0], angle[1]).encode("utf-8"))


if __name__ == '__main__':
    in_path = sys.argv[1]
    if os.path.exists(in_path):
        clocks = read_file(in_path)
        angles = calc_results(clocks)
        write_file(angles)
    else:
        logging.info("Input does not file not exists!")
