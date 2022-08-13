import logging


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


def calc_angle(hr: int, mnt: int):
    mnt_angle = 6 * mnt
    hr_angle = 30 * hr + mnt_angle / 12
    angle_between = hr_angle - mnt_angle
    if -180 < angle_between < 0:
        print("minute-hand is {0} degrees clockwise from hour-hand".format(abs(angle_between)))
    elif angle_between > 180:
        print("minute-hand is {0} degrees clockwise from hour-hand".format(-angle_between % 180))
    elif angle_between < -180:
        print("hour-hand is {0} degrees clockwise from minute-hand".format(angle_between % 180))
    else:
        print("hour-hand is {0} degrees clockwise from minute-hand".format(angle_between))


if __name__ == '__main__':
    clock = input("Please enter the time: ")
    try:
        hr, mnt = validate_clock(clock)
        calc_angle(hr, mnt)
    except KnownException as ex:
        logging.error(ex)
