.. image:: https://travis-ci.com/ContinuumIO/anacondaviz.svg?token=kUQH2Y7k6sa4cByGqypY&branch=master
    :target: https://travis-ci.com/ContinuumIO/anacondaviz

.. image:: https://ci.appveyor.com/api/projects/status/2qh9bsiiwv1txxfm/branch/master?svg=true
    :target: https://ci.appveyor.com/project/ContinuumAnalytics/anacondaviz/branch/master

=====================================================
How to solve visualization problems with Python tools
=====================================================

(WIP!) Opinionated guide:

Using HoloViews, Bokeh, Dask, Datashader, etc etc, notebooks, dashboards, ...

Using conda for environment

I.e. here's the stuff you can do, here's the environment we currently
recommend to do it, here's how we recommend to do it, etc etc. This
way works: do you have a better way?

You can see rendered-to-html notebooks on `appveyor
<https://ci.appveyor.com/project/ContinuumAnalytics/anacondaviz/branch/master/artifacts>`_.

Installation
============

Step 1: Clone the `anacondaviz <https://github.com/ContinuumIO/anacondaviz/blob/master/README.rst>`_ repository
-----------------------------------------------------------------

- Any Linux, Mac OS X, or Windows computer with a web browser should work.  We recommend Chrome, but other browsers should also work.
- 16GB of RAM is required for some of the examples, but most will run fine in 4GB.
- Clone this repository, e.g. using ``git clone https://github.com/ContinuumIO/anacondaviz.git``
- Open a terminal window inside the repository.

Step 2: Create a conda environment from ``environment.yml``
-----------------------------------------------------------

If you don't already have it, install `conda
<https://www.continuum.io/downloads>`_, and then create the
``anacondaviz`` environment by executing::

   > conda env create --force -f environment.yml

When installation is complete you may activate the environment by writing::

   > activate anacondaviz

(for Windows) or::

   $ source activate anacondaviz

(for Linux and Mac). 

Later, when you are ready to exit the environment after the tutorial, you can type::

   > deactivate

If for some reason you want to remove the environment entirely, you can do so by writing::

   > conda env remove --name anacondaviz


Step 3: Downloading the sample data
---------------------------

In this tutorial we will be showing you how to work with some fairly
large datasets.  Unfortunately, that also means that you have to
download this data. To make this as easy as possible we have provided
a script that will download the data for you.  Simply execute in the
root of your clone of this repository::

  > python download_sample_data.py


Step 4: Launch Jupyter Notebook
-------------------------------

You can then launch the notebook server and client::

   (anacondaviz)> cd notebooks
   (anacondaviz)> jupyter notebook

A browser window with a Jupyter Notebook instance should now open, letting
you select and execute each notebook.

If you don't see the notebook appear (e.g. on some OS X versions),
you'll need to cut and paste the URL from the console output manually.


Step 5: Test that everything is working
---------------------------------------

You can see if everything has installed correctly by selecting the
``00-welcome.ipynb`` notebook and doing "Cell/Run All" in the menus.
There may be warnings on some platforms, but you'll know it is working
if you see the HoloViews logo after it runs ``hv.extension()``.

