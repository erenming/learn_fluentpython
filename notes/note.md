1. 特殊方法`__missing__`： 所有映射类型在处理找不到的键时都会牵扯到`__missing__`方法
2. 字典中的散列表
    - 通过`hash()`计算散列值
    - Python会保证1/3的表元为空，当快要达到阈值时，原有散列表会被复制到一个更大的空间里面
    - 散列算法
    ![xx](https://github.com/erenming/learn_fluentpython/raw/master/notes/images/WX20190225-224311@2x.png)
3. dict的实现及其导致的结果
    - 键必须是可散列的，需满足
        1. 支持`hash()`, 并通过该`__hash__()`得到的散列值不变
        2. 支持`__eq__()`检测相等性
        3. 若`a == b`为真，则`hash(a) == hash(b)`也为真
    - 内存开销大
    - 键查询快
    - 键的次序*取决于*添加顺序
        1. 当往dict里添加新键而又发生冲突的时候，新键可能会被安排存放到另一个位置。
        2. 因此，对于同样的数据源，插入顺序的不同只会影响到数据出现的顺序。而字典本身是相等的
    - 往字典里添加新键可能会改变已有键的顺序
        1. 添加键, 可能会导致字典的扩容。把字典已有元素复制到新表中时，可能会发生冲突，从而导致键的次序改变
4. set的实现及其导致的结果
    - 集合内元素必须是可散列的
    - 集合很耗内存
    - 很高效地判断元素是否存在于集合
    - 元素次序取决于添加顺序
    - 往集合内添加元素，可能会导致集合已有顺序改变
5. 装饰器
    - 能把被装饰的函数替换成其他函数
    - 装饰器在模块加载时立即执行
    - 装饰器最好通过实现`__call__`的类实现
    - 通常，多数装饰器会修改被装饰的函数，它会定义一个内部函数，然后将其返回，替换被装饰的函数
    - 使用`@functools.wraps(func)`把相关的属性复制到被装饰的函数上
    - 标准库中的装饰器
        1. `functools.lru_cache`: 适用于生成n个斐波那契这种慢速递归函数
        2. `functools.singledispatch`: 用于将整体方案分为多个模块。使用`@singleddispatch`的函数会成为泛函数：根据第一个参数的类型，以不同方式执行相同操作的一组函数
6. 变量作用域规则
    - Python不要求声明变量，但是会假定函数定义体中赋值的变量是局部变量，是设计选择
7. 闭包
    ![xx](https://github.com/erenming/learn_fluentpython/raw/master/notes/images/WX20190226-225004@2x.png)
    - 闭包是一种函数，它会保留定义函数时存在的自由变量的绑定（eg, 保存在`avg.__clousure__`中`cell`对象的`cell_contents`属性中）
    - `nonlocal`声明：将变量标记为自由变量
        1. 对于数字、字符串、元组等不可变类型来说，只能读取，不能更新。需要使用`nonlocal`
        2. 对于列表等可变类型，本身会作为自由变量

8. 协议：是一种非正式的接口，只在文档中定义。例如，序列协议只需要`__len__`和`__getitem__`。因此有了鸭子类型，
    某个对象为序列，至是因为它的行为像序列而不一定要是序列类型
9. 抽象基类：使接口更加明确、能验证实现是否复合规定。与鸭子类型代表的特征动态协议相对
10. 解释器需要迭代对象x时，会自动调用iter(x)
    - 检查对象是否实现了`__iter__`方法，如果实现则调用，获取一个迭代器
    - 如果未实现`__iter__`, 但实现了`__getitem__`, Python会创建一个迭代器，尝试按顺序(从索引0开始)获取元素
    - 若尝试失败，则抛出`TypeError`
11. 可迭代对象和迭代器： Python从可迭代对象中获取迭代器
    ![xx](https://github.com/erenming/learn_fluentpython/raw/master/notes/images/WX20190228-134839@2x.png)
    - 可迭代对象
        1. 使用`iter`内置函数可以获取迭代器的对象
        2. 对象实现了`__iter__`方法：每次都实例化一个新的迭代器
        3. 序列
        4. 实现了`__getitem__`且参数从零开始索引
    - 迭代器
        1. 实现了无参数的`__next__`方法，返回序列中的下一个元素；如果没有元素了，则抛出`StopIteration`异常
        2. Python中的迭代器还实现了`__iter__`方法，因此迭代器也是可迭代的
12. 生成器
    - 生成器函数回创建一个生成器对象。
    - 生成器是迭代器： 传入`next()`并在函数体最终返回时抛出`StopIteration`异常，与迭代器协议一致，根据鸭子类型，为迭代器
    - `yield from`: 产出从另一个生成器生成的值
13. 列表的内部实现：`动态数组`。通过已分配的内存大小动态调整数组大小
14. 垃圾回收机制：
    1. 引用计数: 主要的
        - 直接而高效，但是无法处理循环引用
        - every object (even integer) has an extra field called reference count that is increased or decreased when a pointer to the object is copied or deleted
        - If reference counting field reaches zero, CPython automatically calls the object-specific deallocation function.
    2. 分代回收机制：将系统中的内存块根据存活时间划分为不同集合，每个集合为一个“代”，垃圾收集频率随“代”的存活时间增加而降低
        - 主要用于解决循环引用，Python1.5引进，gc模块负责
        - 分三代：新对象为第一代，如果一个对象在一次垃圾回收后仍存活，则升级为老一代。越新垃圾收集越频繁
        - 循环引用：
            1. 循环引用只可能出现在容器对象中
            2. 编码中为避免循环应用，可使用弱引用
            3. 使用`objgraph`包生成引用图
15. `obj.attr`: Python调用特殊方法(`__getattr__`或`__setattr__`)
16. `__new__`: 用于构建实例，返回一个实例。`__init__`: 用于初始化实例
17. 动态属性：应用场景：`a["b"][0]`转换为`a.b[0]`
18. 特性：由方法构成的属性。是类属性，它管理实例属性的存取。
    - 实例属性会覆盖同名类属性
    - 实例属性不会覆盖类特性
    - `obj.attr`先从类`obj.Class`中寻找名为`attr`的特性。若无，才在`obj`实例中寻找
    - 影响属性处理方式的特殊属性
        1. `__class__`: 对象所属类的引用
        2. `__dict__`: 一个映射，储存对象或类的可写属性
        3. `__slots__`: 类可以定义这个属性，限制实例能有哪些属性
        4. `__getattr__`: 仅当获取指定的属性失败，搜索过obj,Class和超类之后调用
        5. `__getattribute__`: 尝试获取指定的属性时总会调用这个方法，特殊属性或方法除外。
        为避免无限递归，要使用`super().__getattribute__(obj, name)`
        6. `__setattr__`: 尝试设置指定的属性时总会调用这个方法