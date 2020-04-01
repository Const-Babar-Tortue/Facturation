#!/bin/sh

blueprint_src=api.apib
output=../docs/index.html
template=default
theme=cyborg

aglio -i "$blueprint_src" -o "$output" --theme-template=$template --theme-variables=$theme
