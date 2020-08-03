@echo off
@echo.
@echo Starting development mail server...
@echo.
python -m smtpd -n -c DebuggingServer localhost:8025