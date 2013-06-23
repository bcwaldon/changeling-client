import argparse

import changeling_client.api


parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', required=True)


def main():
    args = parser.parse_args()
    service = changeling_client.api.Service(args.endpoint)
    print service.get_change('43af1ff3-10b4-4060-9562-133d56efcc91')
