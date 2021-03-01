.. oase documentation master file, created by
   sphinx-quickstart on Mon Jun  3 10:32:06 2019.
   You can adapt this file completely to your liking, but it should at
   least contain the root `toctree` directive.

.. sectnum::

.. raw:: html

   <font size="+8">Welcome to oase's documentation! (Dev)</font>


.. toctree::
   :maxdepth: 4
   :caption: Contents:

.. contents::

.. include:: ../../README.rst


#################
Kalman Filter
#################

.. include:: ./ekf_guide.rst

**************
Kalman Class
**************
.. autoclass:: oase.oase.Kalman
   :members:
   :special-members: __getitem__

*****************
Supporting Class
*****************

Filter Data Events
====================

.. autoclass:: oase.oase.Event
   :members:

.. autoclass:: oase.oase.Reset
   :members:

.. autoclass:: oase.oase.Control
   :members:

.. autoclass:: oase.oase.Observation
   :members:

EventPlot Class
====================
.. autoclass:: oase.oase.EventPlot
   :members:


###################
Accessory Modules
###################

*****************
Utility Module
*****************

.. automodule:: oase.utility
   :members:

*****************
Model Module
*****************

.. automodule:: oase.model
   :members:

*****************
Roshelper Module
*****************

.. automodule:: oase.roshelper
   :members:


#########################
Experimental Modules
#########################

.. automodule:: oase.gslam
   :members:

####################
Indices and tables
####################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
