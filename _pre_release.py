"""

This file exists for pre-release version tracking. Please do not edit anything in this file unless
you are contributing to the development of InSPy Kit (or this particular sub-package)!

"""

# What stage of pre-release is this?
pr_type = 'pre-alpha'

# What build version of the pre-release is it?
pr_version = '0.1'

# Concatenate the two previous strings into one for easy access to both parts.
version = f'{pr_type}_{pr_version}'

# Dev Note: 'pr_version' should be incremented any time you push changes code that the program uses to run.
#            Therefore; one would not increment this version if:
#                - Pushing new documentation.
#                - Correcting typo in code comments.
#
#             Since this version information focuses on unstable releases ONLY one shouldn't bother
#             incrementing 'pr_version' when changing 'pre_release' to False in _version.py when
#             pushing the final change in a stable application release.
#
#             If you have any comments/questions/concerns/thoughts of any kind please don't hesitate
#             to file an issue on github (https://github.com/tayjaybabee/sub-dom-scan), or contact me
#             via email <t.blackstone@inspyre.tech>
