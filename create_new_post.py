""" 
Creates a new template for a Markdown post, with a required
title and optional category and tag options. 

The date and modified date are automatically set to the date
used when this script is run.
"""

from datetime import datetime

now = datetime.now()

# Should probably never be changed, Pelican will probably never change this
date_format = "%Y-%m-%d %H:%M"
date_string = now.strftime(date_format)

import argparse

parser = argparse.ArgumentParser(
    description="Use this file to create a basic Markdown file for writing content in Pelican"
)

parser.add_argument(
    "-t",
    "--title",
    nargs="*",
    required=True,
    type=str,
    help="The title for your new content post",
)

parser.add_argument("--tags", nargs="*", help="Tags for your post", default="misc")

parser.add_argument(
    "-c",
    "--category",
    type=str,
    help="A category for your post to be filed under",
    default="misc",
)

args = parser.parse_args()

print(args.title)

title = ' '.join(args.title)

template = f"""
Title: {title}
Date: {date_string}
Modified: {date_string}
Category: {args.category}
Tags: {', '.join(args.tags)}
Authors: Yashas Lokesh
Summary: *** FILL IN THIS PART ***
""".strip()

print(template)

file_name = f"{'-'.join(map(str.lower, title.split()))}.md"

import os

with open(os.path.join('content', file_name), mode='w') as f:
    f.write(template)