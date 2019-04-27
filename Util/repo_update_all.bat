@echo off

echo.
echo --
echo -- Util Fix Submodules
echo --
echo.
python "Repo/util_fix_submodules.py"

echo.
echo --
echo -- Util Check Submodules
echo --
echo.
python "Repo/util_check_submodules.py"

pause