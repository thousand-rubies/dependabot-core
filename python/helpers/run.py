import sys
import json

from lib import parser, hasher

if __name__ == "__main__":
    args = json.loads(sys.stdin.read())

    if args["function"] == "parse_requirements":
        print(parser.parse_requirements(args["args"][0]))
    elif args["function"] == "parse_setup":
        print(parser.parse_setup(args["args"][0]))
    elif args["function"] == "parse_pep621_dependencies":
        print(parser.parse_pep621_dependencies(args["args"][0]))
    elif args["function"] == "get_dependency_hash":
        print(hasher.get_dependency_hash(*args["args"]))
    elif args["function"] == "get_pipfile_hash":
        print(hasher.get_pipfile_hash(*args["args"]))
    elif args["function"] == "get_pyproject_hash":
        print(hasher.get_pyproject_hash(*args["args"]))
