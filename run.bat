@echo off
title SlimeBot

:Menu
echo ========================================
echo ===              XD                  ===
echo ========================================
echo.
echo 1.Slime with Huanglong+Yoda
echo 2.RaidJump
echo.

@CHOICE /n /c:123 /m "Enter: "%1
if %ERRORLEVEL% == 1 goto 1
if %ERRORLEVEL% == 2 goto 2

:1
@py -u %cd%\slimeHuanglong+Yoda.py %*
goto Menu

:2
@py -u %cd%\raidJump.py %*
goto Menu
pause