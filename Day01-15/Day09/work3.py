"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成

Date    : 2019-08-19 11:50:50
Author  : Younth Yang (8593009@qq.com)
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """docstring for Employee"""

    def __init__(self, name):
        super(Employee, self).__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    """docstring for Manager"""

    def get_salary(self):
        return 15000.00


class Programmer(Employee):
    """docstring for Programmer"""

    def __init__(self, name, work_hour = 0):
        super().__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, work_hour):
        self._work_hour = work_hour

    def get_salary(self):
        return 150.00 * self._work_hour


class Salesman(Employee):
    """docstring for Salesman"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._name = name
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [Manager('刘备'), Programmer('诸葛亮'),
            Manager('曹操'), Salesman('荀彧'),
            Salesman('吕布'), Programmer('张辽'),
            Programmer('赵云')]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
