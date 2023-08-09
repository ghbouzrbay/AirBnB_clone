#!/usr/bin/python3
"""A program that contains the entry point of the command interpreter."""


import cmd
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """class for command processor.

    Args:
        cmd (_type_): _description_
    """
    name = "(hbnb) "
    cl_list = ["BaseModel", "User", "State", "City", "Amenity",
                    "Place", "Review"]
    cmd_list = ["create", "show", "all", "destroy", "update", "count"]

    def quit(self, args):
        """Quit command to exit the program"""
        return True

    def EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything"""
        pass

    def create(self, inp):
        """
        Creates a new instance of BaseModel, saves it (to the JSON
        file) and prints the id.

        Args:
            class_name (class): name of current class.
        """
        args = inp.split()
        if not self.class_verification(args):
            return

        instance = eval(str(args[0]) + '()')
        if not isinstance(instance, BaseModel):
            return
        instance.save()
        print(inst.id)

    def show(self, inp):
        """Prints the string representation of an instance based on the class name and id."""
        args = inp.split()

        if not self.class_verification(args):
            return

        if not self.id_verification(args):
            return

        str_key = str(args[0]) + '.' + str(args[1])
        objct = models.storage.all()
        print(objct[str_key])

    @classmethod
    def class_verification(cls, args):
        """Verifies class and checks if it is in the class list.

        Returns:
            bool: True or false depending on status of class.
        """
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in cls.cl_list:
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def id_verification(args):
        """Verifies id of class.

        Returns:
            bool: True or False depending on status of id.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objct = models.storage.all()
        str_key = str(args[0]) + '.' + str(args[1])
        if str_key not in objct.keys():
            print("** no instance found **")
            return False

        return True

    def destroy(self, inp):
        """Deletes an instance based on the class name and id (save thechange into the JSON file)."""
        args = inp.split()
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        str_key = str(args[0]) + '.' + str(args[1])
        objct = models.storage.all()
        models.storage.delete(objct[str_key])
        models.storage.save()

    def all(self, inp):
        """Prints all string representation of all instances based or not on the class name."""
        args = inp.split()
        objct = models.storage.all()
        lists = []
        if len(args) == 0:
            # print all classes
            for value in objct.values():
                lists.append(str(value))
        elif args[0] in self.cl_list:
            # print just arg[0] class instances
            for (key, value) in objct.items():
                if args[0] in key:
                    lists.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(lists)

    def update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        objct = models.storage.all()
        for key, value in objct.items():
            _name = value.__class__.__name__
            _id = value.id
            if _name == args[0] and objct_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    models.storage.save()
                return

    def cmd(self, arg):
        """Hook before the command is run."""
        if '.' in arg and '(' in arg and ')' in arg:
            classe = arg.split('.')
            cmds = classe[1].split('(')
            args = cmds[1].split(')')
            if classe[0] in HBNBCommand.cl_list and cmds[0] \
                    in HBNBCommand.cmd_list:
                arg = cmds[0] + ' ' + classe[0] + ' ' + args[0]
        return arg

    def count(self, class_name):
        """Retrieve the number of instances of a class."""
        _count = 0
        objct = models.storage.all()
        for key, value in objct.items():
            keys_split = key.split('.')
            if keys_split[0] == _name:
                count += 1
        print(count)

    @staticmethod
    def attribute_verification(args):
        """Verifies attributes."""
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
