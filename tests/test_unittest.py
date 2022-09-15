import unittest
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc, secretary_program_start
from parameterized import parameterized
from unittest.mock import patch

class TestFunction(unittest.TestCase):
    def test_check_document_existance(self):
        result = check_document_existance('10006')
        self.assertTrue(result)

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        etalon = 'Геннадий Покемонов'
        result = get_doc_owner_name()
        self.assertEqual(etalon, result)

    def test_get_all_doc_owners_names(self):
        etalon = {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}
        result = get_all_doc_owners_names()
        self.assertGreaterEqual(len(result), len(etalon))

    def test_remove_doc_from_shelf(self):
        doc_num = '5455 028765'
        result_dirs = remove_doc_from_shelf('5455 028765')
        self.assertNotIn(doc_num, result_dirs['1'])

    @patch('builtins.input', lambda *args: '25')
    def test_add_new_shelf(self):
        etalon = ('25', True)
        result = add_new_shelf()
        self.assertEqual(etalon, result)

    def test_append_doc_to_shelf(self):
        directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': ['10006']
        }
        result = append_doc_to_shelf('10006', '3')
        self.assertNotEquals(directories, result)

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc(self):
        etalon = ('10006', True)
        result = delete_doc()
        self.assertEqual(etalon, result)

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_get_doc_shelf(self):
        etalon = '1'
        result = get_doc_shelf()
        self.assertEqual(etalon, result)

    @patch('builtins.input', side_effect=['11-2', '25'])
    def test_move_doc_to_shelf(self, mock_inputs):
        doc_num = '11-2'
        new_shelf = '25'
        result = move_doc_to_shelf()
        shelf_with_docs = result[new_shelf]
        if shelf_with_docs[0]:
            self.assertEqual(doc_num, shelf_with_docs[0])
        else:
            print('Error')

    def test_show_document_info(self):
        document = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        result = show_document_info(document)
        self.assertEqual((document['type'], document['number'], document['name']), result)

    def test_show_all_docs_info(self):
        etalon = 4
        result = show_all_docs_info()
        self.assertEqual(etalon, result)

    @patch('builtins.input', side_effect=['001', 'passport', 'Иван Иван', '2'])
    def test_add_new_doc(self, mock_inputs):
        result = add_new_doc()
        self.assertEqual('2', result)

    @patch('builtins.input', side_effect=['a', '002', 'passport', 'Иван Нави', '3'])
    def test_secretary_program_start1(self, mock_inputs):
        result = secretary_program_start()
        self.assertEqual('3', result)

    @patch('builtins.input', side_effect=['help'])
    def test_secretary_program_start2(self, mock_inputs):
        result = secretary_program_start()
        self.assertFalse(not(result))

    @patch('builtins.input', side_effect=['q'])
    def test_secretary_program_start3(self, mock_inputs):
        result = secretary_program_start()
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['s', '11-2'])
    def test_secretary_program_start4(self, mock_inputs):
        result = secretary_program_start()
        self.assertEquals('25', result)


if __name__ == '__main__':
    unittest.main()
