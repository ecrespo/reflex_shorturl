#!/usr/bin/env bash

source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -f frontend.zip
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
