from __future__ import unicode_literals, print_function
import unittest
import json
from crawler.model import MongoModel 

class testModel(unittest.TestCase):
    
    def test_insert_into_mongo(self):
        client = MongoModel('test', 'test')
        data = {'test': 'test_insert'}
        client.mongo_add(data)

    def test_count_word_from_documents(self):
        """get input from list of document
        output object dict like word with total
        example :
        input = ["lorem ipsum we", "we want something new"]
        output = {'lorem': 1, "ipsum" : 1, 'we':2}

        """

        input = ["lorem ipsum we", "we want something new"]
        utils = Utils()
        data = utils.count_words(input)
        print(data)
        self.assertEqual(data['lorem'], 1)

    
if __name__ == '__main__':
    unittest.main()
