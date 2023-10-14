#!/usr/bin/python3
"""Module for the console with entry point of the cmd interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """the command interpreter"""

    classes = {"BaseModel": BaseModel}

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """exit on end of file"""
        return True

    def do_quit(self, line):
        """exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER does nothing"""
        pass

    def do_create(self, arg):
        """creates a new instance, saves it and prints the id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_inst = storage.classes()[arg]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints string repr of an instance base on class name"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            w_arg = arg.split(' ')
            if w_arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(w_arg) < 2:
                print("** instance id missing **")
            else:
                inst = "{}.{}".format(w_arg[0], w_arg[1])
                if inst not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[inst])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            w_arg = arg.split(' ')
            if w_arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(w_arg) < 2:
                print("** instance id missing **")
            else:
                inst = "{}.{}".format(w_arg[0], w_arg[1])
                if inst not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[inst]
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if arg:
            w_arg = arg.split(" ")
            if w_arg[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                inst = [str(obj) for key, obj in storage.all().
                        items()if type(obj).__name__ == w_arg[0]]
                print(inst)
        else:
            inst = [str(obj) for key, obj in storage.all().items()]
            print(inst)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            w_arg =arg.split(' ')
            if w_arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(w_arg) < 2:
                print("** instance id missing **")
            else:
                inst = "{}.{}".format(w_arg[0], w_arg[1])
                if inst not in storage.all():
                    print("** no instance found **")
                elif len(w_arg) < 3:
                    print("** attribute name missing **")
                elif len(w_arg) < 4:
                    print("** value missing **")
                else: 
                    obj = storage.all()[inst]
                    attr_name = w_arg[2]
                    attr_value = w_arg[3]
                    if hasattr(obj, attr_name):
                        attr_value = type(getattr(obj,
                            attr_name))(attr_value)
                        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
