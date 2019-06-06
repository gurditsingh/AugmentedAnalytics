class DataTypeUtisl:

    @staticmethod
    def dtypes(x):
        if type(x) == pd.Series:
            types = x.dtype
            if types == ('O' or "string" or "unicode"):
                return 'obj'
            elif types == ("int64" or "uint8" or "uint16" or "uint32" or "uint64" or "int8" or "int32" or "int16"):
                return 'int'
            elif types == ('float64' or 'float16' or 'float32' or 'float128'):
                return 'float'
            elif types == 'bool':
                return 'bool'
            else:
                return 'date'
        else:
            dfs = x.dtypes
            for f in (dfs.index.tolist()):
                dfs[f] = str(dfs[f])
                if "int" in dfs[f]:
                    dfs[f] = 'int'
                elif "float" in dfs[f]:
                    dfs[f] = "float"
                elif "bool" in dfs[f]:
                    dfs[f] = "bool"
                elif "O" in dfs[f] or "obj" in dfs[f]:
                    dfs[f] = "obj"
                elif "date" in dfs[f]:
                    dfs[f] = "date"
                else:
                    dfs[f] = "obj"
            return dfs