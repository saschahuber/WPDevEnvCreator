#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json

from WPDevEnvCreator import WPDevEnvCreator
from WPDevEnvCreator.Utils import Logger

def main():
    parser = argparse.ArgumentParser(description='Create a dev-env of your wordpress site!')
    parser.add_argument('--config', type=str, help='Path to the json-config-file')
    parser.add_argument('--temp_dir', type=str, default='/temp/WPDevEnvCreator/', help='Where to store temp-files?')
    parser.add_argument('--logging', action='store_true', help='Write logs?')

    args = parser.parse_args()

    config_file = args.config

    Logger.LOGGING = args.logging

    Logger.Logger.log(config_file, "CommandLine")

    with open(config_file) as json_file:
        config = json.load(json_file)

    Logger.Logger.log(str(config), "CommandLine")

    devEnvCreator = WPDevEnvCreator(config, args.temp_dir)

    devEnvCreator.createDevEnv()

if __name__ == "__main__":
    main()