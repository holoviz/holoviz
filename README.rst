jupytercon2017-holoviews-tutorial
=============================

HoloViews with Bokeh tutorial at Jupytercon 2017

This document explains how to get your computer set up for the
tutorial, including how to install the software libraries and data
files that we will be working with.  Because some of the data files
are large, it's best to run through these steps *before* you leave on
your trip, using a good internet connection.


Step 1: Clone the `jupytercon-2017-holoviews-tutorial <https://github.com/ioam/jupytercon2017-holoviews-tutorial/blob/master/README.rst>`_ repository
-----------------------------------------------------------------

- Any Linux, Mac OS X, or Windows computer with a web browser should work.  We recommend Chrome, but typically also test Firefox and Safari.
- Clone this repository, e.g. using ``git clone https://github.com/ioam/jupytercon2017-holoviews-tutorial.git``
- Open a terminal window inside the repository.


You should plan to do a "git pull" on your clone of this repository
sometime after Friday, July 7, in case we need to make any fixes or
improvements in the meantime.


Step 2: Create a conda environment from ``environment.yml``
-----------------------------------------------------------

The easiest way to get an environment set up for the tutorial is
installing it using the ``environment.yml`` we have provided. If you
don't already have it, install `conda <https://www.continuum.io/downloads>`_,
and then create the ``hvtutorial`` environment by executing::

   > conda env create -f environment.yml

When installation is complete you may activate the environment by writing::

   > activate hvtutorial

(for Windows) or::

   $ source activate hvtutorial

(for Linux and Mac). 

Later, when you are ready to exit the environment after the tutorial, you can type::

   > deactivate

If for some reason you want to remove the environment entirely, you can do so by writing::

   > conda env remove --name hvtutorial


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

   (hvtutorial)> cd notebooks
   (hvtutorial)> jupyter notebook --NotebookApp.iopub_data_rate_limit=100000000

A browser window with a Jupyter Notebook instance should now open, letting
you select and execute each notebook. (Increasing the rate limit in
this way is required for the current 5.0 Jupyter version, but should
not be needed in earlier or later Jupyter releases.)


Step 5: Test that everything is working
---------------------------------------

You can see if everything has installed correctly by selecting the
``00-welcome.ipynb`` notebook and doing "Cell/Run All" in the menus.
There may be warnings on some platforms, but you'll know it is working
if you see the HoloViews logo after it runs ``hv.extension()``



Preparing for the Tutorial
--------------------------

If you want to get familiar with HoloViews before the tutorial (which
is not a requirement), you can have a look at our new website at
`holoviews.org <http://holoviews.org/>`_ looking through the getting
started and user guides. If you want to run these examples yourself,
you can get ahold of them by typing this command inside your conda
environment::

    (hvtutorial)> holoviews --install-examples
    (hvtutorial)> cd holoviews-examples

You should then be inside a new folder named "holoviews-examples" in
your current directory.  Now launch a Jupyter notebook server and dive
into the examples::

    (hvtutorial)> jupyter notebook --NotebookApp.iopub_data_rate_limit=100000000 notebooks/00-welcome.ipynb
