#!/bin/bash
python3.11 manage.py migrate && python3.11 manage.py runserver 0.0.0.0:8000