import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestParsonalTree_BlackBox(unittest.TestCase):
    def test_Values(self):
        tree_list = ['tree1']
        tree = ParsonalTree(tree_list)
        self.assertEqual('prs', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)

