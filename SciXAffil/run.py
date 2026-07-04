import argparse
import asyncio
import os

from API import template_server
from augment import augment

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="action")
    subparsers.add_parser("Affil_API", help="Initialize TEMPLATE gRPC API")
    subparsers.add_parser("AugmentApp", help="Initialize Affil Working Unit")
    args = parser.parse_args()

    if args.action == "AugmentApp":
        proj_home = os.path.realpath("/app/SciXAffil/")
        augment.init_pipeline(proj_home)

    elif args.action == "Affil_API":
        asyncio.run(template_server.serve())
