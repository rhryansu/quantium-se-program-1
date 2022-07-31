. ./venv/bin/activate

python3 -m pytest test_dash_app.py

PYTEST_EXIT_CODE=$?
if [ $PYTEST_EXIT_CODE -eq 0 ]; then
    exit 0
else
  exit 1
fi