@echo off

python "Repo/warning.py"

echo.
echo --
echo -- Fresh Templates
echo --
echo.
python "Repo/fresh_templates.py"

echo.
echo --
echo -- Fresh Pip
echo --
echo.
python "Repo/fresh_pip.py"

echo.
echo --
echo -- Util Fix Submodules
echo --
echo.
python "Repo/util_fixsubmodules.py"

python "Repo/footer.py"

pause