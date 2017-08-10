#-*- coding: utf-8 -*-
'''
Created on 2017. 8. 10.

@author: user
'''

from deco.MyDeco import HelloBye, Auth

@HelloBye
def test1():
    print "test1() called"
    
@Auth    
def test2():
    print "test2() called"
    
if __name__ == '__main__':
    test1()
    test2()


    