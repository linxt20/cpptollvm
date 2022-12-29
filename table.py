class NameProperty:
    def __init__(self, type, value, signed=True):
        # type : LLVM 的类型
        # value: 程序中的地址
        # signed: 是否有符号
        self.type = type
        self.value = value
        self.signed = signed

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_signed(self):
        return self.signed

    def set_signed(self, signed):
        self.signed = signed


class NameTable:
    def __init__(self):
        self.table = [{}]
        self.current_scope_level = 0

    def enterScope(self):
        self.current_scope_level += 1
        self.table.append({})

    def exitScope(self):
        if self.current_scope_level == 0:
            raise BaseException("exitScope error")
        self.table.pop()
        self.current_scope_level -= 1

    def addGlobal(self, name: str, _property: NameProperty):
        if self.table[0].get(name) is not None:
            raise BaseException("global name already exist")
        _property.level = 0
        self.table[0].update({name: _property})

    def addLocal(self, name: str, _property: NameProperty):
        if self.table[self.current_scope_level].get(name) is not None:
            raise BaseException("local name already exist")
        _property.level = self.current_scope_level
        self.table[self.current_scope_level].update({name: _property})

    def getProperty(self, name: str) -> NameProperty:
        for i in range(self.current_scope_level, -1, -1):
            if self.table[i].get(name) is not None:
                return self.table[i].get(name)
        raise BaseException("name not exist")

    def setProperty(self, name: str, value):
        for i in range(self.current_scope_level, -1, -1):
            if self.table[i].get(name) is not None:
                _property = self.table[i].get(name)
                _property.set_value(value)
                self.table[i].update({name: _property})
                return
        raise BaseException("name not exist")
