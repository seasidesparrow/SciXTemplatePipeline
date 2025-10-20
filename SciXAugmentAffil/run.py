import argparse
import asyncio
import os

from API import template_server
from affildb import template

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="action")
    subparsers.add_parser("affildb_API", help="Initialize affildb gRPC API")
    subparsers.add_parser("affildb_APP", help="Initialize affildb Working Unit")
    args = parser.parse_args()

    if args.action == "affildb_APP":
        proj_home = os.path.realpath("/app/SciXAugmentAffil/")
        template.init_pipeline(proj_home)

    elif args.action == "affildb_API":
        asyncio.run(template_server.serve())
