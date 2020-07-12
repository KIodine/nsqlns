import unittest
import itertools

import nsqlns

print(f"testing `nsqlns` version {nsqlns.__version__}")

class NSQLNSTestCase(unittest.TestCase):
    def setUp(self):
        self.root_node = nsqlns.NsqlNamespace("root", delim=":")
        self.leaf_node = nsqlns.NsqlNamespace("leaf", delim=">")
        return
    
    def tearDown(self):
        self.root_node = None
        self.leaf_node = None
        return

    def test_node2str(self):
        self.assertEqual(str(self.root_node), "root")
        return
    
    def test_concat_same(self):
        tmp_node = self.root_node/self.leaf_node
        self.assertTrue(isinstance(tmp_node, nsqlns.NsqlNamespace))
        self.assertEqual(str(tmp_node), "root:leaf")
        return
    
    def test_concat_str(self):
        tmp_node = self.root_node/"leaf"
        self.assertTrue(isinstance(tmp_node, nsqlns.NsqlNamespace))
        self.assertEqual(str(tmp_node), "root:leaf")
        return

    def test_concat_other(self):
        with self.assertRaises(TypeError):
            self.root_node/0xBEEF
        return

    def test_sub_delim(self):
        temp_name = "ground"
        preforged = self.root_node/self.leaf_node
        temp_node = nsqlns.NsqlNamespace(temp_name)
        
        test_node = preforged/temp_node
        self.assertEqual(str(test_node), "root:leaf>ground")
        
        test_str = preforged>temp_name
        self.assertEqual(str(test_str), "root:leaf>ground")
        
        return

    def test_gen_str(self):
        ns_str = self.root_node>"leaf"
        self.assertTrue(isinstance(ns_str, str))
        self.assertEqual(ns_str, "root:leaf")
        
        ns_str = self.root_node>self.leaf_node
        self.assertTrue(isinstance(ns_str, str))
        self.assertEqual(ns_str, "root:leaf")

        with self.assertRaises(TypeError):
            self.root_node>0xDEAD
        return


class NSQLNSTestCaseComplex(unittest.TestCase):
    # Nothing to prepare/clean.
    def test_long_concat(self):
        # A!B@C#D$E%F^G[&]
        nodes = [
            nsqlns.NsqlNamespace(node_str, delim=node_delim)
            for (node_str, node_delim) in zip(
                "ABCDEFG", "!@#$%^&"
            )
        ]
        reducer = nsqlns.NsqlNamespace.__truediv__
        tmp_node = nodes[0]
        
        for nd in nodes[1:]:
            tmp_node = reducer(tmp_node, nd)
        
        self.assertEqual(str(tmp_node), r"A!B@C#D$E%F^G")
        return


# ---
centeral_suite = unittest.TestSuite()
loader  = unittest.TestLoader()

cases = [
    NSQLNSTestCase,
    NSQLNSTestCaseComplex
]
suites = map(loader.loadTestsFromTestCase, cases)
centeral_suite.addTests(suites)

#suite   = loader.loadTestsFromTestCase(NSQLNSTestCase)

txt_runner = unittest.TextTestRunner(verbosity=2)
txt_runner.run(centeral_suite)
