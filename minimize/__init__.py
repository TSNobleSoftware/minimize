import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("minimize").version
except pkg_resources.DistributionNotFound:
    pass

# Other relevant module code goes here
