from . import CSV as csv
import loris_extension


def read_file(file_name, file_name_dat_aps=None):
    """parse a file from a neuromorphic camera and return events
    supported file formats are .aedat, .dat, .es and .csv
    """
    if file_name.endswith('.aedat'):
        print("Not yet implemented")
        return None
    elif file_name.endswith('.dat') and '_td' in file_name and file_name_dat_aps == None:
        parsed_file = loris_extension.read_dat_td(file_name)
    elif file_name.endswith('.dat') and '_aps' in file_name and file_name_dat_aps == None:
        parsed_file = loris_extension.read_dat_aps(file_name)
    elif file_name.endswith('.dat') and file_name_dat_aps.endswith('.dat'):
        parsed_file = loris_extension.read_dat_td_aps(file_name, file_name_dat_aps)
    elif file_name.endswith('.es'):
        parsed_file = loris_extension.read_event_stream(file_name)
    elif file_name.endswith('.csv'):
        parsed_file = csv.parse_file(file_name)
    else:
        print("I don't know what kind of format you want to read. "
              + "Please specify a valid file name ending such as .aedat etc")
        return None

    if file_name_dat_aps == None:
        print("Read " + str(len(parsed_file['events'])) + " events from file with " + parsed_file['type'] + " events.")
    else:
        print("Read " + str(len(parsed_file['events'])) + " events from combined files with dvs and atis events.")
    return parsed_file