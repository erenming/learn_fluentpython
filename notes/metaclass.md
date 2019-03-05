1. 一些理念
    - 类元编程是指在运行时创建或定制类的技艺
    - 类是一等对象，可用函数新建类
2. 类工厂函数
    - `type(class_name, bases, attribute_mappings)`：用`type`来创建类
        1. class_name: 类名
        2. bases: 基类元祖
        3. attribute_mappings: 类的属性映射表(dict)

3. 类装饰器：以类对象为参数，返回原来的类或修改后的类
4. 导入时与运行时
    - 导入时会“运行全部顶层代码”，`import`语句会触发任何"运行时"行为
        1. 对于函数，编译函数的定义体，绑定函数对象到对应的全局名称上
        2. 对于类，执行每个类的定义体，甚至嵌套类的定义体。结果是，定义了类的属性和方法，并构建了类对象
    - 垃圾回收时，会调用兑现的`__del__`方法
5. 元类
    - 制作类的工厂类
    - 默认情况下，Python中的类是type类的实例。为避免无限回溯，type是自身的实例
    - 所有类都是type的实例，但是元类**同时还是**type的子类
    - 元类通常可以通过`__init__(cls, name, bases, attr_dict)`方法定制实例
        1. cls: 元类对象
        2. name: 待构建的类名
        3. bases: 基类元组
        4. attr_dict: 属性映射表
    ![xx](https://github.com/erenming/learn_fluentpython/raw/master/notes/images/WX20190305-103306@2x.png)
    - `__prepare__(cls, name, bases)`: 在调用`__new__`之前调用，必须返回一个**映射**
    - 应用场景举例
        1. 验证属性
        2. 一次把装饰器依附到多个方法上
        3. 序列化对象或转换数据
        4. 对象关系映射
        5. 基于对象的持久储存
        6. 动态转换使用其他语言编写的类结构
6. 类作为对象
    - 常见类属性：
        1. `cls.__bases__`: 类的基类元组
        2. `cls.__qualname__`: 类或函数的限定名称，即从模块的全局到类的点分路径。例如`ClassOne.ClassTwo`
        3. `cls.__subclasses__`: 返回一个包括类的直接子类的列表
        4. `__name__`, `__class__`, `__mro__`