#!/usr/bin/python3
"""All the test_cases for the city model class"""
import os
import json
import pep8
import models
import unittest
from models.engine.file_storage import FileStorage


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        obj = FileStorage()
        self.assertIsNotNone(obj.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = FileStorage()
        self.assertTrue(hasattr(obj, "_FileStorage__file_path"))
        self.assertTrue(hasattr(obj, "_FileStorage__objects"))
        self.assertEqual(len(obj.__dict__), 0)

    def test_new_method(self):
        """Checking if the new method is working all fine"""
        fl_obj = FileStorage()
        fl_obj._FileStorage__objects.clear()
        # check if the dictionary __objects has been cleared.
        self.assertEqual(fl_obj._FileStorage__objects, {})
        obj = models.user.User()
        obj.name = "victor"
        FileStorage().new(obj)
        if(self.assertNotEqual(fl_obj._FileStorage__objects, {})):
            key = "User." + obj.id
            self.assertIn(key, fl_obj._FileStorage__objects)

    def test_save_method(self):
        """Checking for file saving and saving format"""
        self.assertTrue(os.path.isfile("./models/engine/file.json"))
        self.assertTrue(os.path.getsize("./models/engine/file.json"), 0)

        obj = models.user.User()
        obj.name = "Tommy"
        FileStorage().save()

        with open("./models/engine/file.json", mode="r") as json_file:
            total_reads = sum(1 for _ in json_file)
        self.assertGreater(total_reads, 0)
        self.assertGreater(os.path.getsize("./models/engine/file.json"), 0)

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/engine/file_storage.py',
                 './tests/test_models/test_file_storage.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_reload_method(self):
        """Testing for the reload methods functionality"""
        obj = models.city.City()
        obj.name = "Birmingham"
        FileStorage().save()
        self.assertGreater(os.path.getsize("./models/engine/file.json"), 0)
        with open("./models/engine/file.json", mode="r") as json_file:
            red = json_file.read()
            if red:
                dicts = json.loads(red)
                self.assertEqual(type(dicts), dict)
                test_dic = dicts[f"{type(obj).__name__}.{obj.id}"]
                self.assertIn('name', test_dic)
                self.assertEqual("Birmingham", test_dic['name'])
