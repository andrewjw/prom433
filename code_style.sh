#!/bin/bash

set -e

${PYCODESTYLE:-pycodestyle} bin/ prom433/ tests/
