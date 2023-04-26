@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

set SOURCEDIR=source
set BUILDDIR=build

python -m sphinx.cmd.build >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

python -m sphinx.cmd.build -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
python -m sphinx.cmd.build -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
