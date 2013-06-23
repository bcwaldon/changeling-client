import argparse

import changeling_client.api


parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', required=True)


def main():
    args = parser.parse_args()
    service = changeling_client.api.Service(args.endpoint)
    print service.list_changes()
