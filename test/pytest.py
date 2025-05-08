#!/usr/bin/env python3
import unittest
import os


class TestHometools(unittest.TestCase):
    def test_cli(self):
        from subprocess import Popen, PIPE
        p = Popen('plotsr -h'.split(), stdout=PIPE, stderr=PIPE)
        out = p.communicate()
        assert 'error' not in out[1].decode()

    def test_pdf_out(self):
        from subprocess import Popen, PIPE
        import os
        from glob import glob

        # get the directory where pytest.py lives
        ##pytest_dir = os.path.abspath(os.path.dirname(__file__))
        ##os.chdir(os.path.join(pytest_dir, 'test_data'))  ###
        #syri = os.path.join(pytest_dir, 'test_data', 'syri.out')
        #genomes = os.path.join(pytest_dir, 'test_data', 'genomes.txt')

        output = 'plotsr.pdf'

        try:
            os.remove(output)
        except OSError as e:
            pass

        #command = f'plotsr --sr {syri} --genomes {genomes} -o {output}'.split()
        command = f'plotsr --sr syri.out --genomes genomes.txt -o {output}'.split()
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        out = p.communicate()
        assert os.path.isfile(output)
        os.remove(output)
        for f in glob(f"*log"):
            try:
                os.remove(f)
            except OSError as e:
                if e.errno != 2:  # 2 is the error number when no such file or directory is present https://docs.python.org/2/library/errno.html
                    raise

    def test_png_out(self):
        from subprocess import Popen, PIPE
        import os
        from glob import glob

        # get the directory where pytest.py lives
        ##pytest_dir = os.path.abspath(os.path.dirname(__file__))
        ##os.chdir(os.path.join(pytest_dir, 'test_data'))  ###
        #syri = os.path.join(pytest_dir, 'test_data', 'syri.out')
        #genomes = os.path.join(pytest_dir, 'test_data', 'genomes.txt')

        output = 'plotsr.png'

        try:
            os.remove(output)
        except OSError as e:
            pass

        #command = f'plotsr --sr {syri} --genomes {genomes} -o {output}'.split()
        command = f'plotsr --sr syri.out --genomes genomes.txt -o {output}'.split()
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        out = p.communicate()

        assert os.path.isfile(output)
        os.remove(output)
        for f in glob(f"*log"):
            try:
                os.remove(f)
            except OSError as e:
                if e.errno != 2:  # 2 is the error number when no such file or directory is present https://docs.python.org/2/library/errno.html
                    raise


if __name__ == '__main__':
    #os.chdir('test/test_data/')
    pytest_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_data'))###
    os.chdir(pytest_dir)###
    unittest.main(verbosity=3)
