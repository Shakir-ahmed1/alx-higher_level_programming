#!/usr/bin/python3
""" unittest for the module square """
import io
import unittest.mock

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ A test case for the Square class
        TODO: number of arguments the abelity to set and get
              id number generation
        """

    def extract(self, obj, expect):
        self.assertEqual(obj.size, expect[0])
        self.assertEqual(obj.x, expect[1])
        self.assertEqual(obj.y, expect[2])
        self.assertEqual(obj.id, expect[3])

    def test_basic_square(self):
        """
            test cases for:
                correct and incorrect number of arguments with errors
                zero case
                issubclass
                setting and getting no validation
        """
        r1 = Square(2)
        r2 = Square(2, 4)
        r3 = Square(2, 5, 6)
        r4 = Square(2, 5, 6, 7)
        r5 = Square(4, 6, 7, None)
        self.extract(r1, [2, 0, 0, r1.id])
        self.extract(r2, [2, 4, 0, r2.id])
        self.extract(r3, [2, 5, 6, r3.id])
        self.extract(r4, [2, 5, 6, r4.id])
        self.extract(r5, [4, 6, 7, r5.id])
        r7 = Square(5, 0, 0)
        r7.size = 11
        r7.x = 12
        r7.y = 13
        r7.id = 14
        self.assertEqual(r7.size, 11)
        self.assertEqual(r7.x, 12)
        self.assertEqual(r7.y, 13)
        self.assertEqual(r7.id, 14)
        self.assertEqual(r7.size, r7.width)
        self.assertEqual(r7.size, r7.height)
        r8 = Square(1, 0)
        r9 = Square(1, 1)
        r10 = Square(1, 0, 1)
        r11 = Square(2, 0, 0)
        self.extract(r8, [1, 0, 0, r8.id])
        self.extract(r9, [1, 1, 0, r9.id])
        self.extract(r10, [1, 0, 1, r10.id])
        self.extract(r11, [2, 0, 0, r11.id])

        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Square, Rectangle), True)
        self.assertRaises(TypeError, Square)

    def test_square_validation(self):
        """ test cases for:
                setting vaidations
        """
        # manualy raised vaule errors
        self.assertRaises(ValueError, Square, 0, 0, 0)
        self.assertRaises(ValueError, Square, 0, 1, 8)
        self.assertRaises(ValueError, Square, 7, -1, 1)
        self.assertRaises(ValueError, Square, 4, 6, -1)
        self.assertRaises(ValueError, Square, 0, 0, 0)
        self.assertRaises(ValueError, Square, -1, -6, 0)
        self.assertRaises(ValueError, Square, -5, 6, 0)
        self.assertRaises(ValueError, Square, 7, -6, -7)
        self.assertRaises(ValueError, Square, 7, -6, 7)
        self.assertRaises(ValueError, Square, 7, -6, 7)
        self.assertRaises(ValueError, Square, -7 - 6, -7)
        self.assertRaises(ValueError, Square, -7, -6, -7)
        # manualy raised type errors
        self.assertRaises(TypeError, Square, "size")
        self.assertRaises(TypeError, Square, (2,))
        self.assertRaises(TypeError, Square, [2], 2, 2)
        self.assertRaises(TypeError, Square, True, 2, {5, 6})
        self.assertRaises(TypeError, Square, 2, 3, 4, None, None)
        self.assertRaises(TypeError, Square, 2, 2.5, 2, 2)
        self.assertRaises(TypeError, Square, 2, {'2': 4}, 2, 2)

    def test_area(self):
        """ tests the area() method """
        r5 = Square(5, 6, 7, None)
        r1 = Square(3)
        r8 = Square(1, 0, 0)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r5.area(), 25)
        self.assertEqual(r8.area(), 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assertStdout(self, r1, expected_output, mock_stdout):
        """ enables out put checking """
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """ tests the displayed content """
        r1 = Square(2)
        self.assertStdout(r1, "##\n##\n")
        r2 = Square(3, 2, 2)
        self.assertStdout(r2, "\n\n  ###\n  ###\n  ###\n")
        r2 = Square(1, 1, 1)
        self.assertStdout(r2, "\n #\n")

    def test_update1(self):
        """ tests the update method """
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 10")
        r1.update()
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 10")
        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Square] (89) 3/10 - 2")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.height, r1.size)
        self.assertEqual(r1.width, r1.size)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")
        self.assertRaises(ValueError, r1.update, 4, -1)
        self.assertRaises(ValueError, r1.update, 4, 0, 2, 0, 0)
        self.assertRaises(ValueError, r1.update, 4, 1, 2, -1, 0)
        self.assertRaises(ValueError, r1.update, 4, 4, 4, -5)
        self.assertRaises(TypeError, r1.update, 4, "4", 4, -5)
        self.assertRaises(TypeError, r1.update, 4, 4, 4, (5,))

    def test_update2(self):
        """ tests the update method with kwargs """
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 10")
        r1.update(size=1)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 1")
        r1.update(size=1, x=2)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 2/10 - 1")
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 3/1 - 2")
        r1.update(x=1, size=2, y=3)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 2")
        r1.update(1, 3, x=7, y=9, size=10)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 3")
        r1.update(2, x=7, size=8, y=9)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 3")
        self.assertRaises(ValueError, r1.update, x=4, y=-1)
        self.assertRaises(ValueError, r1.update, size=4, y=2, x=-1)
        self.assertRaises(ValueError, r1.update, x=0, y=0, size=0)
        self.assertRaises(ValueError, r1.update, y=4, x=4, size=-5)
        self.assertRaises(TypeError, r1.update, x=4, y="4", size=(4,))
        self.assertRaises(TypeError, r1.update, x={"4", 4}, size=4)
        self.assertRaises(TypeError, r1.update, x=4, size=2.5)
        self.assertRaises(TypeError, r1.update, x=4, size=4, y=[4])

    def test_str(self):
        """ tests the update method
        """
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 10")
        r1.update(size=1)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 10/10 - 1")
        r1.update(size=1, x=2)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 2/10 - 1")
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 3/1 - 2")
        r1.update(x=1, size=2, y=3)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 2")
        r1.update(1, 2, x=7, size=8, y=9)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 2")
        r1.update(2, x=7, y=9, size=10)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 1/3 - 2")
        self.assertRaises(ValueError, r1.update, x=4, y=-1)
        self.assertRaises(ValueError, r1.update, size=1, y=2, x=-1)
        self.assertRaises(ValueError, r1.update, x=0, y=0, size=0)
        self.assertRaises(ValueError, r1.update, y=4, x=4, size=-5)
        self.assertRaises(TypeError, r1.update, x=4, y="4", size=4)
        self.assertRaises(TypeError, r1.update, x={"4", 4}, size=4)

    def test_to_dictionary(self):
        """ tests the to_dictionary method """
        r1 = Square(1, 3, 4)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 3, 'y': 4, 'id': r1.id, 'size': 1})
        r1.update(1980, 11)
        temp = r1.to_dictionary()
        self.assertEqual(temp,
                         {'x': 3, 'y': 4, 'id': r1.id, 'size': 11})
        r1.update(id=1981, x=9)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 9, 'y': 4, 'id': 1981, 'size': 11})
        r2 = Square(1)
        self.assertEqual(r2.to_dictionary(),
                         {'x': 0, 'y': 0, 'id': r2.id, 'size': 1})

    def test_to_json_string(self):
        r1 = Square(10, 7, 2)
        r2 = Square(11, 8, 3)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary, r2.to_dictionary()])
        self.assertEqual(eval(json_dictionary), [dictionary, r2.to_dictionary()])

        json_dictionary = Square.to_json_string([dictionary])
        self.assertEqual(eval(json_dictionary), [dictionary])

        json_dictionary = Square.to_json_string([])
        self.assertEqual(eval(json_dictionary), [])

        json_dictionary = Square.to_json_string(None)
        self.assertEqual(eval(json_dictionary), [])

    def test_save_to_file(self):
        r1 = Square(10, 7, 2)
        r2 = Square(11, 8, 3)
        dictionary = r1.to_dictionary()
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [dictionary, r2.to_dictionary()])

        Square.save_to_file([r1])
        with open("Square.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [dictionary])

        Square.save_to_file([])
        with open("Square.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [])

        Square.save_to_file(None)
        with open("Square.json", "r") as js:
            json_dictionary = js.read()
            self.assertEqual(eval(json_dictionary), [])

    def test_from_json_string(self):
        """ tests the from_json_string method """
        r1 = Square(10, 7, 2)
        r2 = Square(11, 8, 3).to_dictionary()
        dictionary = r1.to_dictionary()
        json_dictionary = Square.from_json_string(str([dictionary, r2]))
        self.assertEqual(json_dictionary, [dictionary, r2])

        json_dictionary = Square.from_json_string(str([dictionary]))
        self.assertEqual(json_dictionary, [dictionary])

        json_dictionary = Square.from_json_string('[]')
        self.assertEqual(json_dictionary, [])

        json_dictionary = Square.from_json_string(None)
        self.assertEqual(json_dictionary, [])

    def test_create(self):
        """ tests the create method """
        r1 = Square(3, 5)
        r1_d = r1.to_dictionary()
        r2 = Square.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Square(3, 5, 6)
        r1_d = r1.to_dictionary()
        r2 = Square.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Square(3, 5, 7, 8)
        r1_d = r1.to_dictionary()
        r2 = Square.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = {'size': 1, 'id': 7}
        r2 = Square.create(**r1)
        self.assertEqual(r2.to_dictionary(),
                         {'size': 1, 'id': 7, 'x': 0, 'y': 0})

        r3 = Square.create(size=4, id=4, x=1, y=5)
        self.assertEqual(r3.to_dictionary(),
                         {'size': 4, 'id': 4, 'x': 1, 'y': 5})

        d = {'size': -4, 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(ValueError, Square.create, **d)
        d = {'size': 4, 'id': 4, 'x': -1, 'y': 5}
        self.assertRaises(ValueError, Square.create, **d)
        d = {'size': [4], 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(TypeError, Square.create, **d)
