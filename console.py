#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    A classe that creat a CLI
    """
    prompt = '(hbnb): '
    
    def emptyline(self):
        """A method that garanties if an empty line + ENTER
         shouldn’t execute anything
         """
        pass

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True
    
    do_quit = do_EOF

    def do_create(self, arg):
        """A method that creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Ex: $ create BaseModel
        """
        if arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            obj = BaseModel()
            print(obj.id)
            models.storage.new(obj)
            models.storage.save()
        else:
            print("** class doesn't exist **")
    
    def do_show(self, line):
        """A method that prints the string representation of an instance based
        on the class name and id

        Ex: $ show BaseModel 1234-1234-1234.
        """
        lst = [arg for arg in line.split()]
        if len(lst) == 2:
            key = lst[0] + "." + lst[1]
            dictionary_var = models.storage.all()
            if key in dictionary_var:
                print(dictionary_var[key])
            else:
                print("** no instance found **")
        elif len(lst) == 0:
            print("** class name missing **")
        else:
            if "BaseModel" in lst:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """A method that deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        lst = [arg for arg in line.split()]
        if len(lst) == 2:
            key = lst[0] + "." + lst[1]
            dictionary_var = models.storage.all()
            if key in dictionary_var:
                del dictionary_var[key]
                models.storage.save()
            else:
                print("** no instance found **")
        elif len(lst) == 0:
            print("** class name missing **")
        else:
            if "BaseModel" in lst:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """A method that prints all string representation of all instances
        based or not on the class name.

        Ex: $ all BaseModel or $ all.
        """
        class_exist = 0
        lst_strings = []
        dictionary_var = models.storage.all()
        if arg != "":
            for ke in dictionary_var.keys():
                if arg in ke:
                    lst_strings.append(str(dictionary_var[ke]))
                    class_exist = 1
            if not class_exist:
                print("** class doesn't exist **")
        else:
            for ke in dictionary_var.keys():
                lst_strings.append(str(dictionary_var[ke]))
        print(lst_strings)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

