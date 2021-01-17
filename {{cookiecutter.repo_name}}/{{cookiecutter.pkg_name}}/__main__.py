#!/usr/bin/env python3

import argparse
from .{{cookiecutter.file_name}} import sample_func_pos_args_only, sample_func_opt_args_too


def apply_pos_arg_only_func(arg):
    sample_func_pos_args_only()


def apply_opt_arg_too_func(arg):
    sample_func_opt_args_too(arg.text_to_print)


def get_arguments():
    parser = argparse.ArgumentParser(
        description='sample arg parser implementation')
    parser.set_defaults(func=apply_pos_arg_only_func)
    subparser = parser.add_subparsers()

    parser_pos = subparser.add_parser('pos')
    parser_pos.set_defaults(func=apply_pos_arg_only_func)

    parser_opt_pos = subparser.add_parser('opt-pos')
    parser_opt_pos.add_argument('-t', dest='text_to_print')
    parser_opt_pos.set_defaults(func=apply_opt_arg_too_func)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    args.func(args)

