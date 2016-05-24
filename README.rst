Probedock Python unittest
=========================

Probe Dock probe for Python's unittest module


Compatibility
-------------

* Python 3.4+
* Not tested on Python 2.7, if you try it, please report any bug


Installation
------------

For now, no package is available on pip. This will come.

Until then, you need to install the base probedock package manually :

    * go to `Probedock Python <https://github.com/probedock/probedock-python>`_ and download the package
    * run `python3 setup.py` in the directory where you downloaded the files, which will install the base library
    * download the package here
    * run `python3 setup.py` in the directory where you downloaded the files.


Usage
-----

You can use this test result reporter as a simple drop in replacement for the standard TextTestResult reporter by adding to your tests :
::

    if __name__ == "__main__":
        unittest.main(testRunner=TextTestRunner(resultclass=ProbedockTestResult)


Configuration
-------------

For information about how to configure the probe, please see `Probedock Python <https://github.com/probedock/probedock-python>`_


Contributing
------------

When contributing new features and bug fixes, please add a `changelog <CHANGELOG.rst>`_ entry with your name and what you did


License
-------

Probe Dock Py Unittest is licensed under the `MIT License <http://opensource.org/licenses/MIT>`_.
See `LICENSE.txt <LICENSE.md>`_ for the full license.
