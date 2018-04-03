import collections
from model_v7 import Validated

class EnityMeta(type):
    """元类，用以创建带有验证字段的业务实体"""

    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._filed_name = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._filed_name.append(key)


class Entity(metaclass=EnityMeta):
    @classmethod
    def field_names(cls):
        for name in cls._filed_name:
            yield name