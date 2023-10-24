# AirBnB_clone

<h3><b>Project Description</b></h3>

<h2>Concepts</h2>
<ul>
<li> Python packages </li>
<li> AirBnB clone </li>
</ul>

![Hbnb-Logo](https://github.com/1CyBeR-J1/AirBnB_clone/assets/99370798/cde822dc-8998-4944-a3ae-2ba839dd2878)

<h5> Background Context </h5>

<h4> Welcome to the AirBnB clone project!</h4>

<h2>Execution</h2>
Shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```


<h3><b>The console</b></h3>
<ul>
<li>create your data model</li>
<li>manage (create, update, destroy, etc) objects via a console / command interpreter</li>
<li>store and persist objects to a file (JSON file)</li>
</ul>
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![Server Side (Backend)](https://github.com/1CyBeR-J1/AirBnB_clone/assets/99370798/634329bf-1fdd-4244-84cb-3901cd776d27)


<h3>Files and Directories</h3>
<ul>
<li>models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.</li>
<li>tests directory will contain all unit tests.</li>
<li>console.py file is the entry point of our command interpreter.</li>
<li>models/base_model.py file is the base class of all our models. It contains common elements:</li>
<ul>
  <li>attributes: id, created_at and updated_at</li>
  <li>methods: save() and to_json()</li>
</ul>
<li>models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.</li>
</ul>


<h3><b>Storage</b></h3>
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:
<ul>
<li>Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)</li>
<li>Provide default value of any attribute</li>
<li>In the future, provide the same model behavior for file storage or database storage</li>
</ul>

<h3><b>How can I store my instances?</b></h3>
That’s a good question. So let’s take a look at this code:

```
class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student("John")
students.append(s)
```

Here, I’m creating a student and store it in a list. But after this program execution, my Student instance doesn’t exist anymore.

```
class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student("John")
students.append(s)
save(students) # save all Student objects to a file
```

Nice!

But how it works?

First, let’s look at ```save(students):```
<ul>
<li>Can I write each Student object to a file => NO, it will be the memory representation of the object. For another program execution, this memory representation can’t be reloaded.</li>
<li>Can I write each ```Student.name``` to a file => YES, but imagine you have other attributes to describe Student? It would start to be become too complex.</li>
</ul>
The best solution is to convert this list of Student objects to a JSON representation.

Why JSON? Because it’s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.

Example:
<ul>
<li>My Python program creates Student objects and saves them to a JSON file</li>
</li>Another Javascript program can read this JSON file and manipulate its own Student class/representation</li>
</ul>

And the ```reload()```? now you know the file is a JSON file representing all Student objects. So ```reload()``` has to read the file, parse the JSON string, and re-create Student objects based on this data-structure.


<h3><b></b>File storage == JSON serialization</b></h3>
For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:
<ul>
<li>convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method <code>my_instance.to_json()</code> to retrieve a dictionary</li>
<li>convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a <code>my_string = JSON.dumps(my_dict)</code> </li>
<li>write this string to a file on disk</li>
</ul>

And the process of deserialization?


The same but in the other way:
<ul>
<li>read a string from a file on disk</li>
<li>convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a <code>my_dict = JSON.loads(my_string)</code></li>
<li>convert this data structure to instance - for us it will be a <code>my_instance = MyObject(my_dict)</code></li>
</ul>


<h3><b>*args, **kwargs</b></h3>
[How To Use Them](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

How do you pass arguments to a function?
```
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
```

But with this function definition, you must call ```my_fct``` with 2 parameters, no more, no less.

Can it be dynamic? Yes you can:

```
def my_fct(*args, **kwargs):
    ...

my_fct("Best", "School")
```

What? What’s *args and **kwargs?
<ul>
<li>*args is a Tuple that contains all arguments</li>
<li>*kwargs is a dictionary that contains all arguments by key/value</li>
</ul>


A dictionary? But why?

So, to make it clear, *args is the list of anonymous arguments, no name, just an order. **kwargs is the dictionary with all named arguments.

Examples:
```
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct() # () - {}
my_fct("Best") # ('Best',) - {}
my_fct("Best", 89) # ('Best', 89) - {}
my_fct(name="Best") # () - {'name': 'Best'}
my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}
<h3><b>Command Interpreter Description</b></h3>
```

Perfect? Of course you can mix both, but the order should be first all anonymous arguments, and after named arguments.

Last example:
```
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}
```


<h3><b></b>datetime</b></h3>

datetime is a Python module to manipulate date, time etc…

In this example, you create an instance of datetime with the current date and time
```
from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # <class 'datetime.datetime'>
print(date_now) # 2017-06-08 20:42:42.170922
```

```date_now``` is an object, so you can manipulate it:
```
from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow) # 2017-06-09 20:42:42.170922
```

… you can also store it:
```
a_dict = { 'my_date': date_now }
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}
```

What? What’s this format when a datetime instance is in a datastructure??? It’s unreadable.

How to make it readable: strftime
```
print(date_now.strftime("%A")) # Thursday
print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Thursday 08 June 2017 at 20:42:42
```


<h3><b></b>Data diagram</b></h3>
![IMG](https://github.com/1CyBeR-J1/AirBnB_clone/assets/99370798/8a9cf601-0f3f-4200-95ae-e42f0be13a23)

<h3><b>Authors</b></h3>
