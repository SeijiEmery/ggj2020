#!/usr/bin/env bash
dub run
when-changed source/**.d source/*.d -c "clear; dub run"
