import argparse

import changeling_client.api
import changeling_client.commands


parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', required=True)

subparsers = parser.add_subparsers()
changeling_client.commands.register(subparsers)


def main():
    args = parser.parse_args()
    service = changeling_client.api.Service(args.endpoint)

    args.func(service, args)
