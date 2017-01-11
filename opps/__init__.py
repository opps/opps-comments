# this is a namespace package
# http://stackoverflow.com/questions/24347094/python-setuptools-init-py-does-not-call-declare-namespace
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
