#!/bin/bash

source backend/venv/bin/activate
PYTHONPATH=$(pwd) pytest backend/tests/test_reservas.py
