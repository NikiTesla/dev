def config_parser(config_path):
    with open(config_path, 'r') as config_file:
        config = dict()
        lines = config_file.readlines()
        for line in lines:
            k, v = line.split(' = ')
            config[k] = v.split("\n")[0]
        return config