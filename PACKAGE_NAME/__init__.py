import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(PACKAGE_NAME).version
except pkg_resources.DistributionNotFound:
    pass

# Other relevant module code goes here
