#!/bin/bash

MCUP_ENTRY_PACKAGE="mcup.mcup"

if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

python3 -m "$MCUP_ENTRY_PACKAGE" "$@"