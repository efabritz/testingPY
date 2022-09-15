import unittest

from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc, secretary_program_start
from app import documents
from app import directories

class TestFunction(unittest.TestCase):
    def test_check_document_existance(self):
        etalon = True
        result = check_document_existance('10006')
        self.assertEqual(etalon, result)

    # def test_get_doc_owner_name(self):
    # def test_get_all_doc_owners_names(self):
    # def test_remove_doc_from_shelf(self):
    # def test_add_new_shelf(self):
    # def test_append_doc_to_shelf(self):
    # def test_delete_doc(self):
    # def test_move_doc_to_shelf(self):
    # def test_show_document_info(self):
    # def test_show_all_docs_info(self):
    # def test_add_new_doc(self):
    # def test_secretary_program_start(self):








