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
 
# How to use the examples given
* First, try *dump_me.py*.  
    * this creates *my_func.pkl*
    * it reads it bacj just fine
* Then *load_me.py*
    * this fails, as it can not retrieve the function
* We repeat the exercise with *dump_me2.py* and *load_me2.py*
    * Same issue
* *dill* to the rescue.
    * run *dilly_dump_me* which creates *print_me.dill*
    * this now sucessfully retrieves the *print_me* function
