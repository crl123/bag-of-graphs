import unittest
import make_graphs
import graph_utils

class graph_json(unittest.TestCase):
    def test_graph_json_building(self):
        text = "cusco es grande"
        json_path = "/tmp/sample.json"
        graph = make_graphs.make_structure(text)
        make_graphs.write_json(json_path, graph)

        graph_in_json = graph_utils.load_graph_from_json(json_path)
        print graph_in_json
        nodes_in_json = graph_utils.get_list_nodes(graph_in_json)

        # check that nodes were saved correctly
        self.assertTrue(len(nodes_in_json) == 3)
        for word in text.split(' '):
            self.assertTrue(word in nodes_in_json)
        # check edges
        self.assertTrue(graph_utils.get_list_adj_nodes(graph_in_json, 'cusco')[0] == 'es')

        self.assertTrue(graph_utils.get_list_adj_nodes(graph_in_json, 'es')[0] == 'grande')

if __name__ == '__main__':
    unittest.main()



