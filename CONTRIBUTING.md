= Contributing to prom433 =

Welcome! Thank you for thinking about contributing to prom433! We'd love to merge your code changes into the project, and to discuss any improvements or bugs you might have found. Feel free to create PRs or Issues and we'll happily help you to get changes ready merge. The details in this document will help make this process a little smoother, so thank you for taking the time to read it.

= Pull Requests and Commits =

Please keep pull requests as small and as specific as possible, and avoid combining unrelated changes into one PR. We use Python Semantic Release, which uses the [Angular Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits). Please try to follow this to make the automatic change log generation and release process smoother.

= Code Changes =

Please make sure to run `code_style.sh` and `run_tests.sh` and fix any issues before committing any changes. We aim to keep the output from `pycodestyle` clean.

For smaller changes, such as adding a new metric feel free to just submit the PR. If your change involves a more substantial change, please discuss in an issue first just to avoid extra rework.

If you add a new command line option, please include an update to the `README.md` file as part of the PR.
