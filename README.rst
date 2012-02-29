About
=====
**sphinx-build-qt** is a simple 
`PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_ GUI for 
the ``sphinx-build`` program from the 
`Python Sphinx <http://sphinx.pocoo.org>`_ project. Version ``0.2`` can 
build an entire project or individual files. 

.. image:: https://github.com/vkvn/sphinx-build-qt/blob/master/images/screenshot-0.2.png

Requirements
------------

Users
.....
* Python Sphinx
* PyQt4

Developers
..........
To follow this tutorial you will need

* Qt Designer
* PyQt4 including the development tools (for pyuic4)
* Python Sphinx

.. note::
    
    The tutorial delivered at PyCon Ireland 2011 can be found in the **pycon** 
    branch.

For Ubuntu and derivatives
...........................
Use Synaptic package manager or ``sudo apt-get install packagename``

* qt4-designer
* python-qt4 
* pyqt4-dev-tools
* python-sphinx

For Windows
...........
The PyQt4 package from Riverbank computing contains Qt Designer 
and the required scripts
http://www.riverbankcomputing.co.uk/software/pyqt/download

You can use easy_install or pip to install python-sphinx

For Mac
.......
Sorry, I have no idea how you can get all these installed.
You wouldn't need to add anything to PATH I believe as they should be there
by default (/usr/bin or /usr/local/bin)

Files
-----
* src/sphinx-build-qt.py - main application
* src/ui_dialog.py - Python code of dialog.ui generated using pyuic4
* ui/dialog.ui - the dialog interface designed using Qt Designer (XML format)

The ``docs`` directory contains an example sphinx project

The ``source`` directory is used as source in the dialog and ``build\html`` is
used for the output.

