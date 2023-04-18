#!/usr/bin/python3
""" unittest for the module rectangle """
import io
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle


def extract(obj):
    """ extracts the object to make it comparible """
    return [obj.width, obj.height, obj.x, obj.y, obj.id]


class TestRectangle(unittest.TestCase):
    """ A test case for the Rectangle class
        TODO: number of arguments the abelity to set and get
              id number generation
        """

    def test_basic_rectangle(self):
        """
            test cases for for basic rectangle creation
        """
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3, 4)
        r3 = Rectangle(2, 3, 5, 6)
        r4 = Rectangle(2, 3, 5, 6, 7)
        r5 = Rectangle(4, 5, 6, 7, None)
        self.assertEqual(extract(r1), [2, 3, 0, 0, r1.id])
        self.assertEqual(extract(r2), [2, 3, 4, 0, r2.id])
        self.assertEqual(extract(r3), [2, 3, 5, 6, r3.id])
        self.assertEqual(extract(r4), [2, 3, 5, 6, r4.id])
        self.assertEqual(extract(r5), [4, 5, 6, 7, r5.id])
        r7 = Rectangle(4, 5, 0, 0)
        r7.width = 10
        r7.height = 11
        r7.x = 12
        r7.y = 13
        r7.id = 14
        self.assertEqual(r7.width, 10)
        self.assertEqual(r7.height, 11)
        self.assertEqual(r7.x, 12)
        self.assertEqual(r7.y, 13)
        self.assertEqual(r7.id, 14)
        r8 = Rectangle(1, 1, 0, 0)
        r9 = Rectangle(1, 1, 1, 1)
        r10 = Rectangle(1, 2, 0, 1)
        r11 = Rectangle(2, 2, 0, 0)
        self.assertEqual(extract(r8), [1, 1, 0, 0, r8.id])
        self.assertEqual(extract(r9), [1, 1, 1, 1, r9.id])
        self.assertEqual(extract(r10), [1, 2, 0, 1, r10.id])
        self.assertEqual(extract(r11), [2, 2, 0, 0, r11.id])

        self.assertEqual(issubclass(Rectangle, Base), True)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_validation(self):
        """ test cases for setting vaidations """
        # manualy raised vaule errors
        self.assertRaises(ValueError, Rectangle, 0, 0, 0, 0)
        self.assertRaises(ValueError, Rectangle, 0, 1, 1, 8)
        self.assertRaises(ValueError, Rectangle, 1, 0, 6, 1)
        self.assertRaises(ValueError, Rectangle, 7, 1, -1, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 6, -1)
        self.assertRaises(ValueError, Rectangle, 0, 5, 0, 0)
        self.assertRaises(ValueError, Rectangle, 0, -1, 6, 0)
        self.assertRaises(ValueError, Rectangle, -5, 1, 6, 0)
        self.assertRaises(ValueError, Rectangle, 4, -8, 6, 2)
        self.assertRaises(ValueError, Rectangle, 7, -1, -6, -7)
        self.assertRaises(ValueError, Rectangle, 7, -1, -6, 7)
        self.assertRaises(ValueError, Rectangle, 7, -1, -6, 7)
        self.assertRaises(ValueError, Rectangle, -7, -1, -6, -7)
        self.assertRaises(ValueError, Rectangle, -7, -1, -6, -7)
        # manualy raised type errors
        self.assertRaises(TypeError, Rectangle, 2, "height")
        self.assertRaises(TypeError, Rectangle, (2,), 2)
        self.assertRaises(TypeError, Rectangle, [2], 2, 2, 2)
        self.assertRaises(TypeError, Rectangle, True, 2, {5, 6})
        self.assertRaises(TypeError, Rectangle, 5, 2, {5, 6})
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, None, None)
        self.assertRaises(TypeError, Rectangle, 2.5, 2, 2, 2)
        self.assertRaises(TypeError, Rectangle, 2, {'2': 4}, 2, 2)

    def test_area(self):
        """ tests the area method """
        r5 = Rectangle(4, 5, 6, 7, None)
        r1 = Rectangle(2, 3)
        r8 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r5.area(), 20)
        self.assertEqual(r8.area(), 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assertStdout(self, r1, expected_output, mock_stdout):
        """ enables out put checking """
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """ tests the displayed content """
        r1 = Rectangle(2, 3)
        self.assertStdout(r1, "##\n##\n##\n")
        r2 = Rectangle(3, 2, 2, 2)
        self.assertStdout(r2, "\n\n  ###\n  ###\n")
        r2 = Rectangle(1, 1, 0, 0)
        self.assertStdout(r2, "#\n")

    def test_str(self):
        """ tests the string representation of the Rectangle """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        r3 = Rectangle(3, 4)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), f"[Rectangle] ({r2.id}) 1/0 - 5/5")
        self.assertEqual(str(r3), f"[Rectangle] ({r3.id}) 0/0 - 3/4")

    def test_update1(self):
        """ tests the update method """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")
        r1.update()
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        self.assertRaises(ValueError, r1.update, 4, -1)
        self.assertRaises(ValueError, r1.update, 4, 0, 2, 0, 0)
        self.assertRaises(ValueError, r1.update, 4, 1, 2, -1, 0)
        self.assertRaises(ValueError, r1.update, 4, 4, 4, -5)
        self.assertRaises(TypeError, r1.update, 4, "4", 4, -5)
        self.assertRaises(TypeError, r1.update, 4, 4, 4, (5,))

    def test_update2(self):
        """ tests the update method with kwargs """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 1/3 - 4/2")
        r1.update(1, 2, x=7, height=8, y=9, width=10)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 1/3 - 2/2")
        r1.update(2, x=7, height=8, y=9, width=10)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 1/3 - 2/2")
        self.assertRaises(ValueError, r1.update, x=4, y=-1)
        self.assertRaises(ValueError, r1.update, height=4, width=1, y=2, x=-1)
        self.assertRaises(ValueError, r1.update, x=0, y=0, width=0, height=0)
        self.assertRaises(ValueError, r1.update, width=4, y=4, x=4, height=-5)
        self.assertRaises(TypeError, r1.update, x=4, y="4", width=4)
        self.assertRaises(TypeError, r1.update, x={"4", 4}, width=4)
        self.assertRaises(TypeError, r1.update, x=4, height=4, width=2.5)

    def test_to_dictionary(self):
        """ tests the to_dictionary method """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})
        r1.update(6, 7)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 3, 'y': 4, 'id': 6, 'height': 2, 'width': 7})
        r1.update(id=8, x=7)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 7, 'y': 4, 'id': 8, 'height': 2, 'width': 7})
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.to_dictionary(),
                         {'x': 0, 'y': 0,
                          'id': r2.id, 'height': 2, 'width': 1})

    def test_to_json_string(self):
        """ test the to_json_stirng method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 8, 3, 9)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary, r2.to_dictionary()])
        self.assertEqual(eval(json_dictionary),
                         [dictionary, r2.to_dictionary()])

        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(eval(json_dictionary), [dictionary])

        json_dictionary = Base.to_json_string([])
        self.assertEqual(eval(json_dictionary), [])

        json_dictionary = Rectangle.to_json_string(None)
        self.assertEqual(eval(json_dictionary), [])

    def test_save_to_file(self):
        """ tests the save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 8, 3, 9)
        dictionary = r1.to_dictionary()
        Base.save_to_file([r1, r2])
        with open("Base.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary),
                             [dictionary, r2.to_dictionary()])

        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [dictionary])

        Base.save_to_file([])
        with open("Base.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [])

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [])

    def test_from_json_string(self):
        """ tests the from_json_string method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 8, 3, 9).to_dictionary()
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.from_json_string(
                          Base.to_json_string([dictionary, r2]))
        self.assertEqual(json_dictionary, [dictionary, r2])

        json_dictionary = Base.from_json_string(
                          Rectangle.to_json_string([dictionary]))
        self.assertEqual(json_dictionary, [dictionary])

        json_dictionary = Rectangle.from_json_string('[]')
        self.assertEqual(json_dictionary, [])

        json_dictionary = Rectangle.from_json_string(None)
        self.assertEqual(json_dictionary, [])

    def test_create(self):
        """ tests the create method """
        r1 = Rectangle(3, 5)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 6)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 7, 8)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 7, 8, 3)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = {'height': 7, 'width': 1, 'id': 7}
        r2 = Rectangle.create(**r1)
        self.assertEqual(r2.to_dictionary(),
                         {'height': 7, 'width': 1, 'id': 7, 'x': 0, 'y': 0})

        r3 = Rectangle.create(height=3, width=4, id=4, x=1, y=5)
        self.assertEqual(r3.to_dictionary(),
                         {'height': 3, 'width': 4, 'id': 4, 'x': 1, 'y': 5})

        d = {'height': -3, 'width': 4, 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(ValueError, Rectangle.create, **d)
        d = {'height': 3, 'width': 4, 'id': 4, 'x': [1], 'y': 5}
        self.assertRaises(TypeError, Rectangle.create, **d)
        d = {'height': [3], 'width': 4, 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(TypeError, Rectangle.create, **d)

    def test_load_from_file(self):
        """ tests the load from file function """
        Base.save_to_file(None)
        r = Rectangle(1, 1)
        f1 = Base.load_from_file()
        self.assertEqual(f1, [])
        r7 = Rectangle(2, 2)
        r8 = Rectangle(3, 3, 3, 3)
        r.save_to_file([r7])
        f1 = r.load_from_file()
        self.assertEqual(f1[0].to_dictionary(), r7.to_dictionary())

        r.save_to_file([r7, r8])
        r1 = r.load_from_file()
        self.assertEqual([r1[0].to_dictionary(), r1[1].to_dictionary()],
                         [r7.to_dictionary(), r8.to_dictionary()])

        r.save_to_file([])
        r1 = r.load_from_file()
        self.assertEqual(r1, [])
