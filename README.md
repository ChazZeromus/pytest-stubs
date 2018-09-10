My small set of mypy stubs for pytest

## Installing
1. Since these are just stubs of pytest functions that I need for my project, just pip
   install from master: ```pip install 'git+git://github.com/ChazZeromus/pytest-stubs.git@master#pytest-stubs'```
2. And the rest should just be running `mypy` as usual. Mypy detects `-stubs` packages
   automatically, so you're all set!

## TODO:
- [x] [PEP-0561](https://www.python.org/dev/peps/pep-0561/) specifies that partial stubs (like this one, obviously), should be marked as "partial"
- [ ] Stub everything else?
- [ ] Organize third-party pytest plugins into their own packages
