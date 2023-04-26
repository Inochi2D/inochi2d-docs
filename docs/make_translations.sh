#!/bin/sh

for LANG_DIR in en source/locale/*; do
    POLANG=`basename $LANG_DIR`
    echo "Generating translations $POLANG"
    SPHINX_LANGUAGE=$POLANG pipenv run make html
done