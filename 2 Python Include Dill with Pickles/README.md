# Include Source Code
Kinda like PHP *include(file_name)*.
Python DOES have import, but it lacks the simplicity of a PHP include.

I was definitely interested in being able to include functions.
For example, the *print_me(expression)* function introduced in _vignette 1_.

## ***pickle to the rescue???***
A Python function is an object, so we should be able to pickle it.

    def func(*args, **kwargs):
        pass

    the_pickle = pickle.dumps(func)

We can the store this pickled_object somewhere.
When we need it, we retrieve it restore it in its pythonic glory:

    my_func = pickle.loads(the_pickle)

Et Voila!

## Wait! ... Wait!! -- We want this in a **file**!!
To use a file with pickle we use *pickle.dump(obj, file_handler)* and *pickle.load(file_handler)*.  

However there is a problem with functions.
Execute *dump_me.py* (no problem) and *load_me.py* (***OOPS!***).

## The answer is ***dill pickles!!!***

### first pip install dill
use *import dill*  
Now try *dilly_dump_me.py* and *dilly_load_me.py*, ***SUCCESS!!!***.
 
