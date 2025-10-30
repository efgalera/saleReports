from typing import Union, Type

from .sale_report import TextView, JsonView

def get_sale_report_view(name: str) -> Union[Type[TextView], Type[JsonView]]:
        if name == "text":
            from .sale_report import TextView
            return TextView
        
        elif name == "json":
            from .sale_report import JsonView
            return JsonView

        else:
             raise TypeError(f"Type {name} not suported")
