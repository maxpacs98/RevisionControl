#!/bin/bash
REV=$(git describe --tags --long --dirty --always)
python hello.py "${REV}"
