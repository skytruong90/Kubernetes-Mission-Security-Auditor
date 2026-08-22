import unittest
from pathlib import Path
from k8s_audit import audit
class Tests(unittest.TestCase):
    def test_reference(self): self.assertTrue(audit(Path('examples/deployment.yaml').read_text())['passed'])
    def test_empty_fails(self): self.assertFalse(audit('')['passed'])
if __name__=='__main__': unittest.main()
