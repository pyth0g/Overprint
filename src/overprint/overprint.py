class OverPrint:
    def __init__(self) -> None:
        pass

    last_nrows = None
    def _csi(values: list) -> None:
        csi_up = f"\x1B[{OverPrint.last_nrows}A"
        csi_clr= "\x1B[0K"
                
        if OverPrint.last_nrows is None:
            print('\n'*(len(values)-1))
            csi_up = f"\x1B[{len(values)}A"
        else:
            if OverPrint.last_nrows > len(values):
                print(f'{csi_up}{csi_clr}')
                for r in range(1,OverPrint.last_nrows): print(f'{csi_clr}')
                
        OverPrint.last_nrows = len(values)
        print(f'{csi_up}{values[0]}{csi_clr}')
        for r in range(1, len(values)): print(f'{values[r]}{csi_clr}')

def print(*values: object,sep: str = " ",nl_sep: str = "\n") -> None:
    last_str = ""
    for value in values:
        if len(values) > 1:
            last_str += str(value) + str(sep) if value != values[-1] else str(value)
            OverPrint._csi(last_str.split(nl_sep))
        else:
            OverPrint._csi(str(value).split(nl_sep))