# The Python pickle module - what is it good for
The pickle module, included in a standard Python install, is used serialize and unserialize Python objects.

## Very Simple example
Since it is a module, we start our code with  

    import pickle

To pickle an object, we use *pickle.dump(the_object)*, and to unpickle *pickle.loads(the_pickle)*.  

        the_pickle = pickle.dumps("Hello Pickle Jar")
        new_string = pickle.loads(the_pickle)
        print(new_string)

Here is a python program in *very_simple_pickle.py*.
Note that we use a print_me function in addition to print, as it gives more clarity in the output as to what is being done.

## Persistent data storage
A pickled object can easily be stored in the file system, or in a database.  By reading it back and unpickling, we have the original object back.

Now, why would we want to do that?  I first encountered *pickle* when I was playing with some Neural Net exercise.  

The MNIST dataset of handwritten characters needed to to transformed to be compatible with my Neural Network model. The transformed data, both training and test, was pickled to a file, which was then available to test several NN instantiations. 

The second occasion, which refreshed my memory, was an exercise as part of the [Python course by Bernd Klein](https://python-course.eu/python-tutorial/), where the numpy library is introduced. 

We play with simple persistent storage in the [2 Python Include Vignette](https://github.com/drmagu/Vignettes-of-Python/tree/master/2%20Python%20Include%20Dill%20with%20Pickles) area.
