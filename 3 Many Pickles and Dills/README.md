# Storing and retrieving multiple objects
As explained in the two previous vignettes, there are ways to store a python object to a string, or to a file.  
When using *dill* we can also store functions.
## Simple, put the objects in another Python object
Typically, this would be a tuple. 
The problem comes when unpickling, since the identity (name) of the pickled object is lost.
### Use a dictionary
So, store the name as a key in the dictionary, and the pickle (or dill) as the content.  
See the examples in  
* `make_jar.py`   
* `open_jar.py`  

When we unpickle, we use the key from the dictionary to create the Python object with the desired name and content, by using the exec() function.





