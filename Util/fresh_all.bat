@echo off

echo --
echo -- Fresh Pip
echo --
python "Repo/fresh_pip.py"

echo --
echo -- Fresh Templates
echo --
python "Repo/fresh_templates.py"

echo --
echo -- Fix Submodules
echo --
python "Repo/util_fixsubmodules.py"

pause