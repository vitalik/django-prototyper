#!/usr/bin/env python
import os
from prototyper.cli import main

if __name__ == "__main__":
    # This file is used only development mode, in distrbution we have a `prototyper` command
    os.environ['PROTOTYPER_DEV'] = 'yes'
    main()
