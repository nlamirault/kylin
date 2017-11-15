Kylin -- EDF Teleinformation Python library
=================================================

.. image:: https://badge.fury.io/py/kylin.png
    :target: http://badge.fury.io/py/kylin

.. image:: https://coveralls.io/repos/nlamirault/kylin/badge.png?branch=master
    :target: https://coveralls.io/r/nlamirault/kylin?branch=master

.. image:: https://gemnasium.com/nlamirault/kylin.png
    :target: https://gemnasium.com/nlamirault/kylin

.. image:: https://gitlab.com/nicolas-lamirault/kylin/badges/master/build.svg
  :target: https://gitlab.com/nicolas-lamirault/kylin/commits/master
  :alt: master build status

.. image:: https://gitlab.com/nicolas-lamirault/kylin/badges/develop/build.svg
  :target: https://gitlab.com/nicolas-lamirault/kylin/develop/master
  :alt: develop build status


This library is to read Teleinfo_ frames

Usage
-------

.. code-block:: python

        import kylin

        teleinfo = kylin.Kylin(timeout=2, verbose=True)
        teleinfo.open()
        teleinfo.readframe()
        teleinfo.close()


Development
-----------

* Unit tests using Tox_

.. code-block:: bash

        $ tox -r

* Code coverage:

.. code-block:: bash

        $ tox -r -ecoverage


Documentation
-------------

Documentation is available at: http://readthedocs.org/docs/kylin/en/latest


Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :)


ChangeLog
---------

A changelog is available ChangeLog_.


Contact
-------

Nicolas Lamirault <nicolas.lamirault@gmail.com>


.. _Teleinfo: http://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf
.. _Tox: http://tox.testrun.org
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org
.. _`the repository`: http://github.com/nlamirault/kylin
.. _ChangeLog: http://github.com/nlamirault/kylin/blob/master/ChangeLog.md
