#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""



import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for command processor.

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "
    cl_list = ["BaseModel", "User", "State", "City", "Amenity",
                    "Place", "Review"]
    cmd_list = {
            "all",
            "show",
            "destroy",
            "count",
            "update"
        }
   
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything"""
        pass

    def do_create(self, inp):
        """Creates a new instance of BaseModel, saves it (to the JSON
        file) and prints the id.

        Args:
            class_name (class): name of current class.
        """
        args = inp.split()
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in HBNBCommand.cl_list:
            print("** class doesn't exist **")
            return False

        return True

        instance = eval(str(args[0]) + '()')
        if not isinstance(instance, BaseModel):
            return
        instance.save()
        print(instance.id)

    def do_show(self, inp):
        """Prints the string representation of an instance based on the class name and id."""
        args = inp.split()

        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in HBNBCommand.cl_list:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        objct = storage.all()
        str_key = str(args[0]) + '.' + str(args[1])
        if str_key not in objct.keys():
            print("** no instance found **")
            return False

        return True

        print(objct[str_key])
   
    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = inp.split()
       
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in HBNBCommand.cl_list:
            print("** class doesn't exist **")
            return False

        return True

        
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objct = storage.all()
        str_key = str(args[0]) + '.' + str(args[1])
        if str_key not in objct.keys():
            print("** no instance found **")
            return False

        return True

        storage.delete(objct[str_key])
        storage.save()

    def do_all(self, inp):
        """Prints all string representation of all instances based or not
        on the class name.
        """
        args = inp.split()
        all_objct = storage.all()
        list_ = []
        if len(args) == 0:
            # print all classes
            for value in all_objct.values():
                list_.append(str(value))
        elif args[0] in self.cl_list:
            # print just arg[0] class instances
            for (key, value) in all_objct.items():
                if args[0] in key:
                    list_.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(list_)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        action = ""
        for argv in line.split(','):
            action = action + argv
        args = shlex.split(act)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in HBNBCommand.cl_list:
            print("** class doesn't exist **")
            return False

        return True
        
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objct = storage.all()
        str_key = str(args[0]) + '.' + str(args[1])
        
        if str_key not in objct.keys():
            print("** no instance found **")
            return False

        return True
        
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True
        
        all_objct = storage.all()
        for key, value in all_objct.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    storage.save()
                return

    def precmd(self, arg):
        """Hook before the command is run. 
        If the self.block_command returns True, the command is not run.Otherwise, it is run."""
        
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if cls[0] in HBNBCommand.cl_list and cmd[0] \
                    in HBNBCommand.cmd_list:
                arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_count(self, class_name):
        """Retrieve the number of instances of a class."""
        count = 0
        all_objct = storage.all()
        
        for key, value in all_objct.items():
            keys_split = key.split('.')
            if keys_split[0] == class_name:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
