import time


def time_str():
    return time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))


def create_file(filename, md):
    return open(filename, mode=md)


def close_file(fo):
    fo.close()


def write_file(fo, str_list):
    fo.writelines(str_list)
