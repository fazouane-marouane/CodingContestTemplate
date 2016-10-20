from subprocess import Popen, PIPE
import difflib
import itertools
import re
import os
from os import linesep

def SingleRun(script, inputFilename, expectedFilename):
    p = Popen(['python3', script], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    with open(inputFilename, 'r') as f:
        input = ''.join(f.readlines())
    output, err = p.communicate(input)
    rc = p.returncode
    with open(expectedFilename, 'r') as f:
        expected = ''.join(f.readlines()).splitlines(True)
        actual = output.splitlines(True)
        diff = difflib.unified_diff(expected, actual, fromfile='expected', tofile='actual')
        return ''.join(diff)

def GroupBy(iter, keyselector):
    keys = {keyselector(x) for x in iter }
    return { key: [value for value in iter if keyselector(value) == key] for key in keys }

def GetSampleFiles(basePath):
    matcher = re.compile(r'(input|output)(\d+)\.txt')
    files = [(f, matcher.match(f).group(1), matcher.match(f).group(2)) for f in os.listdir('{0}/samples'.format(basePath))]
    sampleFiles = [{f[1]: f[0] for f in values} for key, values in GroupBy(files, lambda f: f[2]).items()]
    return sampleFiles

def RunCompare(problem):
    for sample in GetSampleFiles(problem):
        input = '{0}/samples/{1}'.format(problem, sample['input'])
        output = '{0}/samples/{1}'.format(problem, sample['output'])
        print('input: {input}, expected: {expected}'.format(input=input, expected=output))
        diff = SingleRun('{0}/main.py'.format(problem), input, output)
        print('diff: {0}'.format(diff))

RunCompare('Towers')
