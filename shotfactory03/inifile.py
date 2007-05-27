"""
Very simple .ini file manipulator for Opera

>>> ini = IniFile()
>>> ini.lines = []
>>> ini.set('User Prefs', 'Run', 1)
>>> ini.lines
['[User Prefs]\\n', 'Run=1\\n']
>>> ini.set('User Prefs', 'Show Upgrade Dialog', 0)
>>> ini.lines
['[User Prefs]\\n', 'Run=1\\n', 'Show Upgrade Dialog=0\\n']
>>> ini.set('User Prefs', 'Run', 0)
>>> ini.lines
['[User Prefs]\\n', 'Run=0\\n', 'Show Upgrade Dialog=0\\n']
>>> ini.auto_detect_crlf()
>>> ini.crlf
'\\n'
>>> ini.lines.insert(0, '# Comment\\r\\n')
>>> ini.auto_detect_crlf()
>>> ini.crlf
'\\r\\n'
"""

class IniFile:

    def __init__(self, filename=None):
        self.filename = filename
        if filename is None:
            self.lines = []
        else:
            self.lines = file(filename).readlines()
        self.auto_detect_crlf()

    def save(self, filename=None):
        if filename is None:
            filename = self.filename
        if filename is None:
            raise NameError
        open(self.filename).write(''.join(self.lines))

    def auto_detect_crlf(self):
        if self.lines:
            line = self.lines[0]
        else:
            line = '\n'
        self.crlf = line[-1:]
        if line[-2:] == '\r\n':
            self.crlf = line[-2:]

    def set(self, section, key, value):
        key_value_line = '%s=%s%s' % (key, value, self.crlf)
        start, stop = self.find_section(section)
        if start is None:
            # Section not found, append section at the end
            if self.lines and self.lines[-1].strip() == '':
                self.lines.append(self.crlf) # Blank line
            self.lines.append('[%s]%s' % (section, self.crlf))
            self.lines.append(key_value_line)
        else:
            # Find the key line in the section
            index = self.find_key(start, stop, key)
            if index is None:
                # Not found, insert at end of section
                self.lines.insert(stop, key_value_line)
            else:
                # Replace key line with new value
                self.lines[index] = key_value_line

    def find_section(self, section):
        start = None
        for index, line in enumerate(self.lines):
            if line.strip() == '[%s]' % section:
                start = index
            if start is not None and line.strip() == '':
                return start, index
        return start, len(self.lines)

    def find_key(self, start, stop, key):
        for index in range(start, stop):
            if self.lines[index].startswith(key + '='):
                return index


if __name__ == '__main__':
    import doctest
    doctest.testmod()
