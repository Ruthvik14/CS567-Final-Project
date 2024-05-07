from __future__ import print_function
try:
    from importlib import reload
except ImportError:
    try:
        from imp import reload
    except ImportError:
        pass
import copy
import traceback
import inspect
import re
import sys
import time
import glob
import struct
import random
import subprocess
import os.path
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
from database import init_db, add_item, update_item, delete_item, get_item, get_items, add_category, get_categories
init_db()
# END STANDALONE CODE
class sut(object):
    def act0(self):
        '''
        str0 = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        '''
        self.__test.append(('''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard0,self.act0))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_str[0] is not None: self.noLongerNone('''self.p_str[0]''')
            if self.__useCould and self.p_str[0] is not None: self.noLongerUsed('''self.p_str[0]''')
            self.p_str_used[0]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard0(self):
        return (((self.p_str_used[0]) or (self.p_str[0] is None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        '''
        str1 = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        '''
        self.__test.append(('''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard1,self.act1))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_str[1] is not None: self.noLongerNone('''self.p_str[1]''')
            if self.__useCould and self.p_str[1] is not None: self.noLongerUsed('''self.p_str[1]''')
            self.p_str_used[1]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard1(self):
        return (((self.p_str_used[1]) or (self.p_str[1] is None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        '''
        str2 = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        '''
        self.__test.append(('''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard2,self.act2))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_str[2] is not None: self.noLongerNone('''self.p_str[2]''')
            if self.__useCould and self.p_str[2] is not None: self.noLongerUsed('''self.p_str[2]''')
            self.p_str_used[2]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard2(self):
        return (((self.p_str_used[2]) or (self.p_str[2] is None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        '''
        str3 = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        '''
        self.__test.append(('''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard3,self.act3))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_str[3] is not None: self.noLongerNone('''self.p_str[3]''')
            if self.__useCould and self.p_str[3] is not None: self.noLongerUsed('''self.p_str[3]''')
            self.p_str_used[3]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard3(self):
        return (((self.p_str_used[3]) or (self.p_str[3] is None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        '''
        str4 = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        '''
        self.__test.append(('''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard4,self.act4))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_str[4] is not None: self.noLongerNone('''self.p_str[4]''')
            if self.__useCould and self.p_str[4] is not None: self.noLongerUsed('''self.p_str[4]''')
            self.p_str_used[4]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard4(self):
        return (((self.p_str_used[4]) or (self.p_str[4] is None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        '''
        int0 = 100, 20, 30, 150, 50
        '''
        self.__test.append(('''self.p_int[0] = 100, 20, 30, 150, 50 ''',self.guard5,self.act5))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_int[0] = 100, 20, 30, 150, 50 '''))
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_int[0] = 100, 20, 30, 150, 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_int[0] is not None: self.noLongerNone('''self.p_int[0]''')
            if self.__useCould and self.p_int[0] is not None: self.noLongerUsed('''self.p_int[0]''')
            self.p_int_used[0]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard5(self):
        return (((self.p_int_used[0]) or (self.p_int[0] is None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        '''
        int1 = 100, 20, 30, 150, 50
        '''
        self.__test.append(('''self.p_int[1] = 100, 20, 30, 150, 50 ''',self.guard6,self.act6))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_int[1] = 100, 20, 30, 150, 50 '''))
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_int[1] = 100, 20, 30, 150, 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_int[1] is not None: self.noLongerNone('''self.p_int[1]''')
            if self.__useCould and self.p_int[1] is not None: self.noLongerUsed('''self.p_int[1]''')
            self.p_int_used[1]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard6(self):
        return (((self.p_int_used[1]) or (self.p_int[1] is None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        '''
        int2 = 100, 20, 30, 150, 50
        '''
        self.__test.append(('''self.p_int[2] = 100, 20, 30, 150, 50 ''',self.guard7,self.act7))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_int[2] = 100, 20, 30, 150, 50 '''))
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_int[2] = 100, 20, 30, 150, 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_int[2] is not None: self.noLongerNone('''self.p_int[2]''')
            if self.__useCould and self.p_int[2] is not None: self.noLongerUsed('''self.p_int[2]''')
            self.p_int_used[2]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard7(self):
        return (((self.p_int_used[2]) or (self.p_int[2] is None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        '''
        int3 = 100, 20, 30, 150, 50
        '''
        self.__test.append(('''self.p_int[3] = 100, 20, 30, 150, 50 ''',self.guard8,self.act8))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_int[3] = 100, 20, 30, 150, 50 '''))
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_int[3] = 100, 20, 30, 150, 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_int[3] is not None: self.noLongerNone('''self.p_int[3]''')
            if self.__useCould and self.p_int[3] is not None: self.noLongerUsed('''self.p_int[3]''')
            self.p_int_used[3]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard8(self):
        return (((self.p_int_used[3]) or (self.p_int[3] is None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        '''
        int4 = 100, 20, 30, 150, 50
        '''
        self.__test.append(('''self.p_int[4] = 100, 20, 30, 150, 50 ''',self.guard9,self.act9))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_int[4] = 100, 20, 30, 150, 50 '''))
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_int[4] = 100, 20, 30, 150, 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_int[4] is not None: self.noLongerNone('''self.p_int[4]''')
            if self.__useCould and self.p_int[4] is not None: self.noLongerUsed('''self.p_int[4]''')
            self.p_int_used[4]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard9(self):
        return (((self.p_int_used[4]) or (self.p_int[4] is None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        '''
        category0 = "Electronics", "Apparel"
        '''
        self.__test.append(('''self.p_category[0] = "Electronics", "Apparel" ''',self.guard10,self.act10))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_category[0] = "Electronics", "Apparel" '''))
            try: __bV['''self.p_category[0]'''] = repr(self.p_category[0]); print(self.prettyName('''self.p_category[0]''') + ' =', __bV['''self.p_category[0]'''], ':',type(self.p_category[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_category[0] = "Electronics", "Apparel"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_category[0] is not None: self.noLongerNone('''self.p_category[0]''')
            if self.__useCould and self.p_category[0] is not None: self.noLongerUsed('''self.p_category[0]''')
            self.p_category_used[0]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_category[0])
                    if __aV != __bV['''self.p_category[0]''']: print('=>',self.prettyName('''self.p_category[0]''') + ' =',__aV, ':',type(self.p_category[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard10(self):
        return (((self.p_category_used[0]) or (self.p_category[0] is None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        '''
        category1 = "Electronics", "Apparel"
        '''
        self.__test.append(('''self.p_category[1] = "Electronics", "Apparel" ''',self.guard11,self.act11))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_category[1] = "Electronics", "Apparel" '''))
            try: __bV['''self.p_category[1]'''] = repr(self.p_category[1]); print(self.prettyName('''self.p_category[1]''') + ' =', __bV['''self.p_category[1]'''], ':',type(self.p_category[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_category[1] = "Electronics", "Apparel"
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_category[1] is not None: self.noLongerNone('''self.p_category[1]''')
            if self.__useCould and self.p_category[1] is not None: self.noLongerUsed('''self.p_category[1]''')
            self.p_category_used[1]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_category[1])
                    if __aV != __bV['''self.p_category[1]''']: print('=>',self.prettyName('''self.p_category[1]''') + ' =',__aV, ':',type(self.p_category[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard11(self):
        return (((self.p_category_used[1]) or (self.p_category[1] is None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        '''
        item0 = {0..4}  # Using indices to refer to items by position
        '''
        self.__test.append(('''self.p_item[0] = {0..4}  # Using indices to refer to items by position ''',self.guard12,self.act12))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_item[0] = {0..4}  # Using indices to refer to items by position '''))
            try: __bV['''self.p_item[0]'''] = repr(self.p_item[0]); print(self.prettyName('''self.p_item[0]''') + ' =', __bV['''self.p_item[0]'''], ':',type(self.p_item[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_item[0] = random.randint(0,4)  # Using indices to refer to items by position
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_item[0] is not None: self.noLongerNone('''self.p_item[0]''')
            if self.__useCould and self.p_item[0] is not None: self.noLongerUsed('''self.p_item[0]''')
            self.p_item_used[0]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_item[0])
                    if __aV != __bV['''self.p_item[0]''']: print('=>',self.prettyName('''self.p_item[0]''') + ' =',__aV, ':',type(self.p_item[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard12(self):
        return (((self.p_item_used[0]) or (self.p_item[0] is None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        '''
        item1 = {0..4}  # Using indices to refer to items by position
        '''
        self.__test.append(('''self.p_item[1] = {0..4}  # Using indices to refer to items by position ''',self.guard13,self.act13))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_item[1] = {0..4}  # Using indices to refer to items by position '''))
            try: __bV['''self.p_item[1]'''] = repr(self.p_item[1]); print(self.prettyName('''self.p_item[1]''') + ' =', __bV['''self.p_item[1]'''], ':',type(self.p_item[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_item[1] = random.randint(0,4) # Using indices to refer to items by position
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_item[1] is not None: self.noLongerNone('''self.p_item[1]''')
            if self.__useCould and self.p_item[1] is not None: self.noLongerUsed('''self.p_item[1]''')
            self.p_item_used[1]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_item[1])
                    if __aV != __bV['''self.p_item[1]''']: print('=>',self.prettyName('''self.p_item[1]''') + ' =',__aV, ':',type(self.p_item[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard13(self):
        return (((self.p_item_used[1]) or (self.p_item[1] is None) or (self.__relaxUsedRestriction)))
    
    def act14(self):
        '''
        item2 = {0..4}  # Using indices to refer to items by position
        '''
        self.__test.append(('''self.p_item[2] = {0..4}  # Using indices to refer to items by position ''',self.guard14,self.act14))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.p_item[2] = {0..4}  # Using indices to refer to items by position '''))
            try: __bV['''self.p_item[2]'''] = repr(self.p_item[2]); print(self.prettyName('''self.p_item[2]''') + ' =', __bV['''self.p_item[2]'''], ':',type(self.p_item[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.p_item[2] = random.randint(0,4)  # Using indices to refer to items by position
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            if self.__useCould and self.p_item[2] is not None: self.noLongerNone('''self.p_item[2]''')
            if self.__useCould and self.p_item[2] is not None: self.noLongerUsed('''self.p_item[2]''')
            self.p_item_used[2]=False
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_item[2])
                    if __aV != __bV['''self.p_item[2]''']: print('=>',self.prettyName('''self.p_item[2]''') + ' =',__aV, ':',type(self.p_item[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard14(self):
        return (((self.p_item_used[2]) or (self.p_item[2] is None) or (self.__relaxUsedRestriction)))
    
    def act15(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard15,self.act15))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard15(self):
        return True
    
    def act16(self):
        '''
        add_category(category0)
        '''
        self.__test.append(('''add_category(self.p_category[0]) ''',self.guard16,self.act16))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_category(self.p_category[0]) '''))
            try: __bV['''self.p_category[0]'''] = repr(self.p_category[0]); print(self.prettyName('''self.p_category[0]''') + ' =', __bV['''self.p_category[0]'''], ':',type(self.p_category[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_category(self.p_category[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_category_used[0]=True
            self.nowUsed('''self.p_category[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_category[0])
                    if __aV != __bV['''self.p_category[0]''']: print('=>',self.prettyName('''self.p_category[0]''') + ' =',__aV, ':',type(self.p_category[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard16(self):
        return (self.p_category[0] is not None)
    
    def act17(self):
        '''
        add_category(category1)
        '''
        self.__test.append(('''add_category(self.p_category[1]) ''',self.guard17,self.act17))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_category(self.p_category[1]) '''))
            try: __bV['''self.p_category[1]'''] = repr(self.p_category[1]); print(self.prettyName('''self.p_category[1]''') + ' =', __bV['''self.p_category[1]'''], ':',type(self.p_category[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_category(self.p_category[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_category_used[1]=True
            self.nowUsed('''self.p_category[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_category[1])
                    if __aV != __bV['''self.p_category[1]''']: print('=>',self.prettyName('''self.p_category[1]''') + ' =',__aV, ':',type(self.p_category[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard17(self):
        return (self.p_category[1] is not None)
    
    def act18(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard18,self.act18))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard18(self):
        return True
    
    def act19(self):
        '''
        choice = {0..4}
        '''
        self.__test.append(('''choice = {0..4} ''',self.guard19,self.act19))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''choice = {0..4} '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            choice = random.randint(0,4)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard19(self):
        return True
    
    def act20(self):
        '''
        add_item(str0, int0, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard20,self.act20))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard20(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None)
    
    def act21(self):
        '''
        add_item(str0, int0, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard21,self.act21))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard21(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None) and (self.p_int[1] is not None)
    
    def act22(self):
        '''
        add_item(str0, int0, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard22,self.act22))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard22(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None) and (self.p_int[2] is not None)
    
    def act23(self):
        '''
        add_item(str0, int0, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard23,self.act23))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard23(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None) and (self.p_int[3] is not None)
    
    def act24(self):
        '''
        add_item(str0, int0, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard24,self.act24))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard24(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None) and (self.p_int[4] is not None)
    
    def act25(self):
        '''
        add_item(str0, int1, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard25,self.act25))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard25(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None) and (self.p_int[0] is not None)
    
    def act26(self):
        '''
        add_item(str0, int1, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard26,self.act26))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard26(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None)
    
    def act27(self):
        '''
        add_item(str0, int1, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard27,self.act27))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard27(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None) and (self.p_int[2] is not None)
    
    def act28(self):
        '''
        add_item(str0, int1, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard28,self.act28))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard28(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None) and (self.p_int[3] is not None)
    
    def act29(self):
        '''
        add_item(str0, int1, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard29,self.act29))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard29(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None) and (self.p_int[4] is not None)
    
    def act30(self):
        '''
        add_item(str0, int2, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard30,self.act30))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard30(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None) and (self.p_int[0] is not None)
    
    def act31(self):
        '''
        add_item(str0, int2, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard31,self.act31))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard31(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None) and (self.p_int[1] is not None)
    
    def act32(self):
        '''
        add_item(str0, int2, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard32,self.act32))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard32(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None)
    
    def act33(self):
        '''
        add_item(str0, int2, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard33,self.act33))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard33(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None) and (self.p_int[3] is not None)
    
    def act34(self):
        '''
        add_item(str0, int2, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard34,self.act34))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard34(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None) and (self.p_int[4] is not None)
    
    def act35(self):
        '''
        add_item(str0, int3, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard35,self.act35))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard35(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None) and (self.p_int[0] is not None)
    
    def act36(self):
        '''
        add_item(str0, int3, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard36,self.act36))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard36(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None) and (self.p_int[1] is not None)
    
    def act37(self):
        '''
        add_item(str0, int3, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard37,self.act37))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard37(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None) and (self.p_int[2] is not None)
    
    def act38(self):
        '''
        add_item(str0, int3, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard38,self.act38))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard38(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None)
    
    def act39(self):
        '''
        add_item(str0, int3, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard39,self.act39))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard39(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None) and (self.p_int[4] is not None)
    
    def act40(self):
        '''
        add_item(str0, int4, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard40,self.act40))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard40(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None) and (self.p_int[0] is not None)
    
    def act41(self):
        '''
        add_item(str0, int4, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard41,self.act41))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard41(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None) and (self.p_int[1] is not None)
    
    def act42(self):
        '''
        add_item(str0, int4, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard42,self.act42))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard42(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None) and (self.p_int[2] is not None)
    
    def act43(self):
        '''
        add_item(str0, int4, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard43,self.act43))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard43(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None) and (self.p_int[3] is not None)
    
    def act44(self):
        '''
        add_item(str0, int4, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard44,self.act44))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard44(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None)
    
    def act45(self):
        '''
        add_item(str1, int0, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard45,self.act45))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard45(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None)
    
    def act46(self):
        '''
        add_item(str1, int0, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard46,self.act46))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard46(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None) and (self.p_int[1] is not None)
    
    def act47(self):
        '''
        add_item(str1, int0, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard47,self.act47))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard47(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None) and (self.p_int[2] is not None)
    
    def act48(self):
        '''
        add_item(str1, int0, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard48,self.act48))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard48(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None) and (self.p_int[3] is not None)
    
    def act49(self):
        '''
        add_item(str1, int0, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard49,self.act49))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard49(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None) and (self.p_int[4] is not None)
    
    def act50(self):
        '''
        add_item(str1, int1, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard50,self.act50))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard50(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None) and (self.p_int[0] is not None)
    
    def act51(self):
        '''
        add_item(str1, int1, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard51,self.act51))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard51(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None)
    
    def act52(self):
        '''
        add_item(str1, int1, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard52,self.act52))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard52(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None) and (self.p_int[2] is not None)
    
    def act53(self):
        '''
        add_item(str1, int1, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard53,self.act53))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard53(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None) and (self.p_int[3] is not None)
    
    def act54(self):
        '''
        add_item(str1, int1, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard54,self.act54))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard54(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None) and (self.p_int[4] is not None)
    
    def act55(self):
        '''
        add_item(str1, int2, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard55,self.act55))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard55(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None) and (self.p_int[0] is not None)
    
    def act56(self):
        '''
        add_item(str1, int2, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard56,self.act56))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard56(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None) and (self.p_int[1] is not None)
    
    def act57(self):
        '''
        add_item(str1, int2, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard57,self.act57))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard57(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None)
    
    def act58(self):
        '''
        add_item(str1, int2, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard58,self.act58))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard58(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None) and (self.p_int[3] is not None)
    
    def act59(self):
        '''
        add_item(str1, int2, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard59,self.act59))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard59(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None) and (self.p_int[4] is not None)
    
    def act60(self):
        '''
        add_item(str1, int3, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard60,self.act60))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard60(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None) and (self.p_int[0] is not None)
    
    def act61(self):
        '''
        add_item(str1, int3, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard61,self.act61))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard61(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None) and (self.p_int[1] is not None)
    
    def act62(self):
        '''
        add_item(str1, int3, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard62,self.act62))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard62(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None) and (self.p_int[2] is not None)
    
    def act63(self):
        '''
        add_item(str1, int3, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard63,self.act63))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard63(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None)
    
    def act64(self):
        '''
        add_item(str1, int3, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard64,self.act64))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard64(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None) and (self.p_int[4] is not None)
    
    def act65(self):
        '''
        add_item(str1, int4, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard65,self.act65))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard65(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None) and (self.p_int[0] is not None)
    
    def act66(self):
        '''
        add_item(str1, int4, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard66,self.act66))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard66(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None) and (self.p_int[1] is not None)
    
    def act67(self):
        '''
        add_item(str1, int4, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard67,self.act67))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard67(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None) and (self.p_int[2] is not None)
    
    def act68(self):
        '''
        add_item(str1, int4, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard68,self.act68))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard68(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None) and (self.p_int[3] is not None)
    
    def act69(self):
        '''
        add_item(str1, int4, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard69,self.act69))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard69(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None)
    
    def act70(self):
        '''
        add_item(str2, int0, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard70,self.act70))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard70(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None)
    
    def act71(self):
        '''
        add_item(str2, int0, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard71,self.act71))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard71(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None) and (self.p_int[1] is not None)
    
    def act72(self):
        '''
        add_item(str2, int0, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard72,self.act72))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard72(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None) and (self.p_int[2] is not None)
    
    def act73(self):
        '''
        add_item(str2, int0, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard73,self.act73))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard73(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None) and (self.p_int[3] is not None)
    
    def act74(self):
        '''
        add_item(str2, int0, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard74,self.act74))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard74(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None) and (self.p_int[4] is not None)
    
    def act75(self):
        '''
        add_item(str2, int1, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard75,self.act75))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard75(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None) and (self.p_int[0] is not None)
    
    def act76(self):
        '''
        add_item(str2, int1, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard76,self.act76))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard76(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None)
    
    def act77(self):
        '''
        add_item(str2, int1, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard77,self.act77))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard77(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None) and (self.p_int[2] is not None)
    
    def act78(self):
        '''
        add_item(str2, int1, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard78,self.act78))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard78(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None) and (self.p_int[3] is not None)
    
    def act79(self):
        '''
        add_item(str2, int1, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard79,self.act79))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard79(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None) and (self.p_int[4] is not None)
    
    def act80(self):
        '''
        add_item(str2, int2, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard80,self.act80))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard80(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None) and (self.p_int[0] is not None)
    
    def act81(self):
        '''
        add_item(str2, int2, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard81,self.act81))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard81(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None) and (self.p_int[1] is not None)
    
    def act82(self):
        '''
        add_item(str2, int2, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard82,self.act82))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard82(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None)
    
    def act83(self):
        '''
        add_item(str2, int2, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard83,self.act83))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard83(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None) and (self.p_int[3] is not None)
    
    def act84(self):
        '''
        add_item(str2, int2, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard84,self.act84))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard84(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None) and (self.p_int[4] is not None)
    
    def act85(self):
        '''
        add_item(str2, int3, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard85,self.act85))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard85(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None) and (self.p_int[0] is not None)
    
    def act86(self):
        '''
        add_item(str2, int3, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard86,self.act86))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard86(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None) and (self.p_int[1] is not None)
    
    def act87(self):
        '''
        add_item(str2, int3, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard87,self.act87))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard87(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None) and (self.p_int[2] is not None)
    
    def act88(self):
        '''
        add_item(str2, int3, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard88,self.act88))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard88(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None)
    
    def act89(self):
        '''
        add_item(str2, int3, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard89,self.act89))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard89(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None) and (self.p_int[4] is not None)
    
    def act90(self):
        '''
        add_item(str2, int4, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard90,self.act90))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard90(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None) and (self.p_int[0] is not None)
    
    def act91(self):
        '''
        add_item(str2, int4, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard91,self.act91))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard91(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None) and (self.p_int[1] is not None)
    
    def act92(self):
        '''
        add_item(str2, int4, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard92,self.act92))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard92(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None) and (self.p_int[2] is not None)
    
    def act93(self):
        '''
        add_item(str2, int4, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard93,self.act93))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard93(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None) and (self.p_int[3] is not None)
    
    def act94(self):
        '''
        add_item(str2, int4, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard94,self.act94))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard94(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None)
    
    def act95(self):
        '''
        add_item(str3, int0, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard95,self.act95))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard95(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None)
    
    def act96(self):
        '''
        add_item(str3, int0, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard96,self.act96))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard96(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None) and (self.p_int[1] is not None)
    
    def act97(self):
        '''
        add_item(str3, int0, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard97,self.act97))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard97(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None) and (self.p_int[2] is not None)
    
    def act98(self):
        '''
        add_item(str3, int0, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard98,self.act98))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard98(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None) and (self.p_int[3] is not None)
    
    def act99(self):
        '''
        add_item(str3, int0, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard99,self.act99))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard99(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None) and (self.p_int[4] is not None)
    
    def act100(self):
        '''
        add_item(str3, int1, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard100,self.act100))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard100(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None) and (self.p_int[0] is not None)
    
    def act101(self):
        '''
        add_item(str3, int1, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard101,self.act101))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard101(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None)
    
    def act102(self):
        '''
        add_item(str3, int1, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard102,self.act102))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard102(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None) and (self.p_int[2] is not None)
    
    def act103(self):
        '''
        add_item(str3, int1, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard103,self.act103))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard103(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None) and (self.p_int[3] is not None)
    
    def act104(self):
        '''
        add_item(str3, int1, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard104,self.act104))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard104(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None) and (self.p_int[4] is not None)
    
    def act105(self):
        '''
        add_item(str3, int2, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard105,self.act105))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard105(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None) and (self.p_int[0] is not None)
    
    def act106(self):
        '''
        add_item(str3, int2, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard106,self.act106))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard106(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None) and (self.p_int[1] is not None)
    
    def act107(self):
        '''
        add_item(str3, int2, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard107,self.act107))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard107(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None)
    
    def act108(self):
        '''
        add_item(str3, int2, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard108,self.act108))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard108(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None) and (self.p_int[3] is not None)
    
    def act109(self):
        '''
        add_item(str3, int2, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard109,self.act109))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard109(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None) and (self.p_int[4] is not None)
    
    def act110(self):
        '''
        add_item(str3, int3, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard110,self.act110))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard110(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None) and (self.p_int[0] is not None)
    
    def act111(self):
        '''
        add_item(str3, int3, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard111,self.act111))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard111(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None) and (self.p_int[1] is not None)
    
    def act112(self):
        '''
        add_item(str3, int3, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard112,self.act112))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard112(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None) and (self.p_int[2] is not None)
    
    def act113(self):
        '''
        add_item(str3, int3, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard113,self.act113))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard113(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None)
    
    def act114(self):
        '''
        add_item(str3, int3, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard114,self.act114))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard114(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None) and (self.p_int[4] is not None)
    
    def act115(self):
        '''
        add_item(str3, int4, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard115,self.act115))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard115(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None) and (self.p_int[0] is not None)
    
    def act116(self):
        '''
        add_item(str3, int4, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard116,self.act116))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard116(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None) and (self.p_int[1] is not None)
    
    def act117(self):
        '''
        add_item(str3, int4, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard117,self.act117))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard117(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None) and (self.p_int[2] is not None)
    
    def act118(self):
        '''
        add_item(str3, int4, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard118,self.act118))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard118(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None) and (self.p_int[3] is not None)
    
    def act119(self):
        '''
        add_item(str3, int4, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard119,self.act119))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard119(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None)
    
    def act120(self):
        '''
        add_item(str4, int0, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard120,self.act120))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard120(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None)
    
    def act121(self):
        '''
        add_item(str4, int0, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard121,self.act121))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard121(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None) and (self.p_int[1] is not None)
    
    def act122(self):
        '''
        add_item(str4, int0, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard122,self.act122))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard122(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None) and (self.p_int[2] is not None)
    
    def act123(self):
        '''
        add_item(str4, int0, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard123,self.act123))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard123(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None) and (self.p_int[3] is not None)
    
    def act124(self):
        '''
        add_item(str4, int0, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard124,self.act124))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard124(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None) and (self.p_int[4] is not None)
    
    def act125(self):
        '''
        add_item(str4, int1, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard125,self.act125))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard125(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None) and (self.p_int[0] is not None)
    
    def act126(self):
        '''
        add_item(str4, int1, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard126,self.act126))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard126(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None)
    
    def act127(self):
        '''
        add_item(str4, int1, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard127,self.act127))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard127(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None) and (self.p_int[2] is not None)
    
    def act128(self):
        '''
        add_item(str4, int1, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard128,self.act128))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard128(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None) and (self.p_int[3] is not None)
    
    def act129(self):
        '''
        add_item(str4, int1, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard129,self.act129))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard129(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None) and (self.p_int[4] is not None)
    
    def act130(self):
        '''
        add_item(str4, int2, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard130,self.act130))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard130(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None) and (self.p_int[0] is not None)
    
    def act131(self):
        '''
        add_item(str4, int2, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard131,self.act131))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard131(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None) and (self.p_int[1] is not None)
    
    def act132(self):
        '''
        add_item(str4, int2, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard132,self.act132))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard132(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None)
    
    def act133(self):
        '''
        add_item(str4, int2, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard133,self.act133))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard133(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None) and (self.p_int[3] is not None)
    
    def act134(self):
        '''
        add_item(str4, int2, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard134,self.act134))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard134(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None) and (self.p_int[4] is not None)
    
    def act135(self):
        '''
        add_item(str4, int3, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard135,self.act135))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard135(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None) and (self.p_int[0] is not None)
    
    def act136(self):
        '''
        add_item(str4, int3, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard136,self.act136))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard136(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None) and (self.p_int[1] is not None)
    
    def act137(self):
        '''
        add_item(str4, int3, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard137,self.act137))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard137(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None) and (self.p_int[2] is not None)
    
    def act138(self):
        '''
        add_item(str4, int3, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard138,self.act138))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard138(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None)
    
    def act139(self):
        '''
        add_item(str4, int3, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard139,self.act139))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard139(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None) and (self.p_int[4] is not None)
    
    def act140(self):
        '''
        add_item(str4, int4, int0, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard140,self.act140))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard140(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None) and (self.p_int[0] is not None)
    
    def act141(self):
        '''
        add_item(str4, int4, int1, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard141,self.act141))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard141(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None) and (self.p_int[1] is not None)
    
    def act142(self):
        '''
        add_item(str4, int4, int2, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard142,self.act142))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard142(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None) and (self.p_int[2] is not None)
    
    def act143(self):
        '''
        add_item(str4, int4, int3, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard143,self.act143))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard143(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None) and (self.p_int[3] is not None)
    
    def act144(self):
        '''
        add_item(str4, int4, int4, 1)  # Using default category ID for simplicity
        '''
        self.__test.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard144,self.act144))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard144(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None)
    
    def act145(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard145,self.act145))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard145(self):
        return True
    
    def act146(self):
        '''
        choice = {0..4}
        '''
        self.__test.append(('''choice = {0..4} ''',self.guard146,self.act146))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''choice = {0..4} '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            choice = random.randint(0,4)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard146(self):
        return True
    
    def act147(self):
        '''
        update_item(str0, quantity=int0)
        '''
        self.__test.append(('''update_item(self.p_str[0], quantity=self.p_int[0]) ''',self.guard147,self.act147))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], quantity=self.p_int[0]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], quantity=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard147(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None)
    
    def act148(self):
        '''
        update_item(str0, quantity=int1)
        '''
        self.__test.append(('''update_item(self.p_str[0], quantity=self.p_int[1]) ''',self.guard148,self.act148))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], quantity=self.p_int[1]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], quantity=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard148(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None)
    
    def act149(self):
        '''
        update_item(str0, quantity=int2)
        '''
        self.__test.append(('''update_item(self.p_str[0], quantity=self.p_int[2]) ''',self.guard149,self.act149))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], quantity=self.p_int[2]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], quantity=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard149(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None)
    
    def act150(self):
        '''
        update_item(str0, quantity=int3)
        '''
        self.__test.append(('''update_item(self.p_str[0], quantity=self.p_int[3]) ''',self.guard150,self.act150))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], quantity=self.p_int[3]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], quantity=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard150(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None)
    
    def act151(self):
        '''
        update_item(str0, quantity=int4)
        '''
        self.__test.append(('''update_item(self.p_str[0], quantity=self.p_int[4]) ''',self.guard151,self.act151))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], quantity=self.p_int[4]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], quantity=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard151(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None)
    
    def act152(self):
        '''
        update_item(str1, quantity=int0)
        '''
        self.__test.append(('''update_item(self.p_str[1], quantity=self.p_int[0]) ''',self.guard152,self.act152))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], quantity=self.p_int[0]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], quantity=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard152(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None)
    
    def act153(self):
        '''
        update_item(str1, quantity=int1)
        '''
        self.__test.append(('''update_item(self.p_str[1], quantity=self.p_int[1]) ''',self.guard153,self.act153))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], quantity=self.p_int[1]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], quantity=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard153(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None)
    
    def act154(self):
        '''
        update_item(str1, quantity=int2)
        '''
        self.__test.append(('''update_item(self.p_str[1], quantity=self.p_int[2]) ''',self.guard154,self.act154))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], quantity=self.p_int[2]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], quantity=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard154(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None)
    
    def act155(self):
        '''
        update_item(str1, quantity=int3)
        '''
        self.__test.append(('''update_item(self.p_str[1], quantity=self.p_int[3]) ''',self.guard155,self.act155))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], quantity=self.p_int[3]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], quantity=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard155(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None)
    
    def act156(self):
        '''
        update_item(str1, quantity=int4)
        '''
        self.__test.append(('''update_item(self.p_str[1], quantity=self.p_int[4]) ''',self.guard156,self.act156))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], quantity=self.p_int[4]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], quantity=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard156(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None)
    
    def act157(self):
        '''
        update_item(str2, quantity=int0)
        '''
        self.__test.append(('''update_item(self.p_str[2], quantity=self.p_int[0]) ''',self.guard157,self.act157))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], quantity=self.p_int[0]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], quantity=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard157(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None)
    
    def act158(self):
        '''
        update_item(str2, quantity=int1)
        '''
        self.__test.append(('''update_item(self.p_str[2], quantity=self.p_int[1]) ''',self.guard158,self.act158))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], quantity=self.p_int[1]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], quantity=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard158(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None)
    
    def act159(self):
        '''
        update_item(str2, quantity=int2)
        '''
        self.__test.append(('''update_item(self.p_str[2], quantity=self.p_int[2]) ''',self.guard159,self.act159))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], quantity=self.p_int[2]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], quantity=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard159(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None)
    
    def act160(self):
        '''
        update_item(str2, quantity=int3)
        '''
        self.__test.append(('''update_item(self.p_str[2], quantity=self.p_int[3]) ''',self.guard160,self.act160))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], quantity=self.p_int[3]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], quantity=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard160(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None)
    
    def act161(self):
        '''
        update_item(str2, quantity=int4)
        '''
        self.__test.append(('''update_item(self.p_str[2], quantity=self.p_int[4]) ''',self.guard161,self.act161))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], quantity=self.p_int[4]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], quantity=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard161(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None)
    
    def act162(self):
        '''
        update_item(str3, quantity=int0)
        '''
        self.__test.append(('''update_item(self.p_str[3], quantity=self.p_int[0]) ''',self.guard162,self.act162))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], quantity=self.p_int[0]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], quantity=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard162(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None)
    
    def act163(self):
        '''
        update_item(str3, quantity=int1)
        '''
        self.__test.append(('''update_item(self.p_str[3], quantity=self.p_int[1]) ''',self.guard163,self.act163))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], quantity=self.p_int[1]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], quantity=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard163(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None)
    
    def act164(self):
        '''
        update_item(str3, quantity=int2)
        '''
        self.__test.append(('''update_item(self.p_str[3], quantity=self.p_int[2]) ''',self.guard164,self.act164))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], quantity=self.p_int[2]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], quantity=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard164(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None)
    
    def act165(self):
        '''
        update_item(str3, quantity=int3)
        '''
        self.__test.append(('''update_item(self.p_str[3], quantity=self.p_int[3]) ''',self.guard165,self.act165))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], quantity=self.p_int[3]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], quantity=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard165(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None)
    
    def act166(self):
        '''
        update_item(str3, quantity=int4)
        '''
        self.__test.append(('''update_item(self.p_str[3], quantity=self.p_int[4]) ''',self.guard166,self.act166))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], quantity=self.p_int[4]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], quantity=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard166(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None)
    
    def act167(self):
        '''
        update_item(str4, quantity=int0)
        '''
        self.__test.append(('''update_item(self.p_str[4], quantity=self.p_int[0]) ''',self.guard167,self.act167))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], quantity=self.p_int[0]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], quantity=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard167(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None)
    
    def act168(self):
        '''
        update_item(str4, quantity=int1)
        '''
        self.__test.append(('''update_item(self.p_str[4], quantity=self.p_int[1]) ''',self.guard168,self.act168))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], quantity=self.p_int[1]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], quantity=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard168(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None)
    
    def act169(self):
        '''
        update_item(str4, quantity=int2)
        '''
        self.__test.append(('''update_item(self.p_str[4], quantity=self.p_int[2]) ''',self.guard169,self.act169))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], quantity=self.p_int[2]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], quantity=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard169(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None)
    
    def act170(self):
        '''
        update_item(str4, quantity=int3)
        '''
        self.__test.append(('''update_item(self.p_str[4], quantity=self.p_int[3]) ''',self.guard170,self.act170))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], quantity=self.p_int[3]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], quantity=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard170(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None)
    
    def act171(self):
        '''
        update_item(str4, quantity=int4)
        '''
        self.__test.append(('''update_item(self.p_str[4], quantity=self.p_int[4]) ''',self.guard171,self.act171))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], quantity=self.p_int[4]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], quantity=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard171(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None)
    
    def act172(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard172,self.act172))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard172(self):
        return True
    
    def act173(self):
        '''
        choice = {0..4}
        '''
        self.__test.append(('''choice = {0..4} ''',self.guard173,self.act173))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''choice = {0..4} '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            choice = random.randint(0,4)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard173(self):
        return True
    
    def act174(self):
        '''
        update_item(str0, price=int0)
        '''
        self.__test.append(('''update_item(self.p_str[0], price=self.p_int[0]) ''',self.guard174,self.act174))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], price=self.p_int[0]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], price=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard174(self):
        return (self.p_str[0] is not None) and (self.p_int[0] is not None)
    
    def act175(self):
        '''
        update_item(str0, price=int1)
        '''
        self.__test.append(('''update_item(self.p_str[0], price=self.p_int[1]) ''',self.guard175,self.act175))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], price=self.p_int[1]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], price=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard175(self):
        return (self.p_str[0] is not None) and (self.p_int[1] is not None)
    
    def act176(self):
        '''
        update_item(str0, price=int2)
        '''
        self.__test.append(('''update_item(self.p_str[0], price=self.p_int[2]) ''',self.guard176,self.act176))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], price=self.p_int[2]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], price=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard176(self):
        return (self.p_str[0] is not None) and (self.p_int[2] is not None)
    
    def act177(self):
        '''
        update_item(str0, price=int3)
        '''
        self.__test.append(('''update_item(self.p_str[0], price=self.p_int[3]) ''',self.guard177,self.act177))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], price=self.p_int[3]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], price=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard177(self):
        return (self.p_str[0] is not None) and (self.p_int[3] is not None)
    
    def act178(self):
        '''
        update_item(str0, price=int4)
        '''
        self.__test.append(('''update_item(self.p_str[0], price=self.p_int[4]) ''',self.guard178,self.act178))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[0], price=self.p_int[4]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[0], price=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard178(self):
        return (self.p_str[0] is not None) and (self.p_int[4] is not None)
    
    def act179(self):
        '''
        update_item(str1, price=int0)
        '''
        self.__test.append(('''update_item(self.p_str[1], price=self.p_int[0]) ''',self.guard179,self.act179))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], price=self.p_int[0]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], price=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard179(self):
        return (self.p_str[1] is not None) and (self.p_int[0] is not None)
    
    def act180(self):
        '''
        update_item(str1, price=int1)
        '''
        self.__test.append(('''update_item(self.p_str[1], price=self.p_int[1]) ''',self.guard180,self.act180))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], price=self.p_int[1]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], price=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard180(self):
        return (self.p_str[1] is not None) and (self.p_int[1] is not None)
    
    def act181(self):
        '''
        update_item(str1, price=int2)
        '''
        self.__test.append(('''update_item(self.p_str[1], price=self.p_int[2]) ''',self.guard181,self.act181))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], price=self.p_int[2]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], price=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard181(self):
        return (self.p_str[1] is not None) and (self.p_int[2] is not None)
    
    def act182(self):
        '''
        update_item(str1, price=int3)
        '''
        self.__test.append(('''update_item(self.p_str[1], price=self.p_int[3]) ''',self.guard182,self.act182))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], price=self.p_int[3]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], price=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard182(self):
        return (self.p_str[1] is not None) and (self.p_int[3] is not None)
    
    def act183(self):
        '''
        update_item(str1, price=int4)
        '''
        self.__test.append(('''update_item(self.p_str[1], price=self.p_int[4]) ''',self.guard183,self.act183))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[1], price=self.p_int[4]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[1], price=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard183(self):
        return (self.p_str[1] is not None) and (self.p_int[4] is not None)
    
    def act184(self):
        '''
        update_item(str2, price=int0)
        '''
        self.__test.append(('''update_item(self.p_str[2], price=self.p_int[0]) ''',self.guard184,self.act184))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], price=self.p_int[0]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], price=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard184(self):
        return (self.p_str[2] is not None) and (self.p_int[0] is not None)
    
    def act185(self):
        '''
        update_item(str2, price=int1)
        '''
        self.__test.append(('''update_item(self.p_str[2], price=self.p_int[1]) ''',self.guard185,self.act185))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], price=self.p_int[1]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], price=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard185(self):
        return (self.p_str[2] is not None) and (self.p_int[1] is not None)
    
    def act186(self):
        '''
        update_item(str2, price=int2)
        '''
        self.__test.append(('''update_item(self.p_str[2], price=self.p_int[2]) ''',self.guard186,self.act186))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], price=self.p_int[2]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], price=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard186(self):
        return (self.p_str[2] is not None) and (self.p_int[2] is not None)
    
    def act187(self):
        '''
        update_item(str2, price=int3)
        '''
        self.__test.append(('''update_item(self.p_str[2], price=self.p_int[3]) ''',self.guard187,self.act187))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], price=self.p_int[3]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], price=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard187(self):
        return (self.p_str[2] is not None) and (self.p_int[3] is not None)
    
    def act188(self):
        '''
        update_item(str2, price=int4)
        '''
        self.__test.append(('''update_item(self.p_str[2], price=self.p_int[4]) ''',self.guard188,self.act188))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[2], price=self.p_int[4]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[2], price=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard188(self):
        return (self.p_str[2] is not None) and (self.p_int[4] is not None)
    
    def act189(self):
        '''
        update_item(str3, price=int0)
        '''
        self.__test.append(('''update_item(self.p_str[3], price=self.p_int[0]) ''',self.guard189,self.act189))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], price=self.p_int[0]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], price=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard189(self):
        return (self.p_str[3] is not None) and (self.p_int[0] is not None)
    
    def act190(self):
        '''
        update_item(str3, price=int1)
        '''
        self.__test.append(('''update_item(self.p_str[3], price=self.p_int[1]) ''',self.guard190,self.act190))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], price=self.p_int[1]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], price=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard190(self):
        return (self.p_str[3] is not None) and (self.p_int[1] is not None)
    
    def act191(self):
        '''
        update_item(str3, price=int2)
        '''
        self.__test.append(('''update_item(self.p_str[3], price=self.p_int[2]) ''',self.guard191,self.act191))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], price=self.p_int[2]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], price=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard191(self):
        return (self.p_str[3] is not None) and (self.p_int[2] is not None)
    
    def act192(self):
        '''
        update_item(str3, price=int3)
        '''
        self.__test.append(('''update_item(self.p_str[3], price=self.p_int[3]) ''',self.guard192,self.act192))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], price=self.p_int[3]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], price=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard192(self):
        return (self.p_str[3] is not None) and (self.p_int[3] is not None)
    
    def act193(self):
        '''
        update_item(str3, price=int4)
        '''
        self.__test.append(('''update_item(self.p_str[3], price=self.p_int[4]) ''',self.guard193,self.act193))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[3], price=self.p_int[4]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[3], price=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard193(self):
        return (self.p_str[3] is not None) and (self.p_int[4] is not None)
    
    def act194(self):
        '''
        update_item(str4, price=int0)
        '''
        self.__test.append(('''update_item(self.p_str[4], price=self.p_int[0]) ''',self.guard194,self.act194))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], price=self.p_int[0]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[0]'''] = repr(self.p_int[0]); print(self.prettyName('''self.p_int[0]''') + ' =', __bV['''self.p_int[0]'''], ':',type(self.p_int[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], price=self.p_int[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[0]=True
            self.nowUsed('''self.p_int[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[0])
                    if __aV != __bV['''self.p_int[0]''']: print('=>',self.prettyName('''self.p_int[0]''') + ' =',__aV, ':',type(self.p_int[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard194(self):
        return (self.p_str[4] is not None) and (self.p_int[0] is not None)
    
    def act195(self):
        '''
        update_item(str4, price=int1)
        '''
        self.__test.append(('''update_item(self.p_str[4], price=self.p_int[1]) ''',self.guard195,self.act195))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], price=self.p_int[1]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[1]'''] = repr(self.p_int[1]); print(self.prettyName('''self.p_int[1]''') + ' =', __bV['''self.p_int[1]'''], ':',type(self.p_int[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], price=self.p_int[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[1]=True
            self.nowUsed('''self.p_int[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[1])
                    if __aV != __bV['''self.p_int[1]''']: print('=>',self.prettyName('''self.p_int[1]''') + ' =',__aV, ':',type(self.p_int[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard195(self):
        return (self.p_str[4] is not None) and (self.p_int[1] is not None)
    
    def act196(self):
        '''
        update_item(str4, price=int2)
        '''
        self.__test.append(('''update_item(self.p_str[4], price=self.p_int[2]) ''',self.guard196,self.act196))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], price=self.p_int[2]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[2]'''] = repr(self.p_int[2]); print(self.prettyName('''self.p_int[2]''') + ' =', __bV['''self.p_int[2]'''], ':',type(self.p_int[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], price=self.p_int[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[2]=True
            self.nowUsed('''self.p_int[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[2])
                    if __aV != __bV['''self.p_int[2]''']: print('=>',self.prettyName('''self.p_int[2]''') + ' =',__aV, ':',type(self.p_int[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard196(self):
        return (self.p_str[4] is not None) and (self.p_int[2] is not None)
    
    def act197(self):
        '''
        update_item(str4, price=int3)
        '''
        self.__test.append(('''update_item(self.p_str[4], price=self.p_int[3]) ''',self.guard197,self.act197))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], price=self.p_int[3]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[3]'''] = repr(self.p_int[3]); print(self.prettyName('''self.p_int[3]''') + ' =', __bV['''self.p_int[3]'''], ':',type(self.p_int[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], price=self.p_int[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[3]=True
            self.nowUsed('''self.p_int[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[3])
                    if __aV != __bV['''self.p_int[3]''']: print('=>',self.prettyName('''self.p_int[3]''') + ' =',__aV, ':',type(self.p_int[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard197(self):
        return (self.p_str[4] is not None) and (self.p_int[3] is not None)
    
    def act198(self):
        '''
        update_item(str4, price=int4)
        '''
        self.__test.append(('''update_item(self.p_str[4], price=self.p_int[4]) ''',self.guard198,self.act198))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''update_item(self.p_str[4], price=self.p_int[4]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
            try: __bV['''self.p_int[4]'''] = repr(self.p_int[4]); print(self.prettyName('''self.p_int[4]''') + ' =', __bV['''self.p_int[4]'''], ':',type(self.p_int[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            update_item(self.p_str[4], price=self.p_int[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            self.p_int_used[4]=True
            self.nowUsed('''self.p_int[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
                try:
                    __aV = repr(self.p_int[4])
                    if __aV != __bV['''self.p_int[4]''']: print('=>',self.prettyName('''self.p_int[4]''') + ' =',__aV, ':',type(self.p_int[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard198(self):
        return (self.p_str[4] is not None) and (self.p_int[4] is not None)
    
    def act199(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard199,self.act199))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard199(self):
        return True
    
    def act200(self):
        '''
        choice = {0..4}
        '''
        self.__test.append(('''choice = {0..4} ''',self.guard200,self.act200))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''choice = {0..4} '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            choice = random.randint(0,4)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard200(self):
        return True
    
    def act201(self):
        '''
        delete_item(str0)
        '''
        self.__test.append(('''delete_item(self.p_str[0]) ''',self.guard201,self.act201))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''delete_item(self.p_str[0]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            delete_item(self.p_str[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard201(self):
        return (self.p_str[0] is not None)
    
    def act202(self):
        '''
        delete_item(str1)
        '''
        self.__test.append(('''delete_item(self.p_str[1]) ''',self.guard202,self.act202))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''delete_item(self.p_str[1]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            delete_item(self.p_str[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard202(self):
        return (self.p_str[1] is not None)
    
    def act203(self):
        '''
        delete_item(str2)
        '''
        self.__test.append(('''delete_item(self.p_str[2]) ''',self.guard203,self.act203))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''delete_item(self.p_str[2]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            delete_item(self.p_str[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard203(self):
        return (self.p_str[2] is not None)
    
    def act204(self):
        '''
        delete_item(str3)
        '''
        self.__test.append(('''delete_item(self.p_str[3]) ''',self.guard204,self.act204))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''delete_item(self.p_str[3]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            delete_item(self.p_str[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard204(self):
        return (self.p_str[3] is not None)
    
    def act205(self):
        '''
        delete_item(str4)
        '''
        self.__test.append(('''delete_item(self.p_str[4]) ''',self.guard205,self.act205))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''delete_item(self.p_str[4]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            delete_item(self.p_str[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard205(self):
        return (self.p_str[4] is not None)
    
    def act206(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard206,self.act206))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard206(self):
        return True
    
    def act207(self):
        '''
        item = get_item(str0)
        '''
        self.__test.append(('''item = get_item(self.p_str[0]) ''',self.guard207,self.act207))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''item = get_item(self.p_str[0]) '''))
            try: __bV['''self.p_str[0]'''] = repr(self.p_str[0]); print(self.prettyName('''self.p_str[0]''') + ' =', __bV['''self.p_str[0]'''], ':',type(self.p_str[0]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            item = get_item(self.p_str[0])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[0]=True
            self.nowUsed('''self.p_str[0]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[0])
                    if __aV != __bV['''self.p_str[0]''']: print('=>',self.prettyName('''self.p_str[0]''') + ' =',__aV, ':',type(self.p_str[0]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard207(self):
        return (self.p_str[0] is not None)
    
    def act208(self):
        '''
        item = get_item(str1)
        '''
        self.__test.append(('''item = get_item(self.p_str[1]) ''',self.guard208,self.act208))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''item = get_item(self.p_str[1]) '''))
            try: __bV['''self.p_str[1]'''] = repr(self.p_str[1]); print(self.prettyName('''self.p_str[1]''') + ' =', __bV['''self.p_str[1]'''], ':',type(self.p_str[1]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            item = get_item(self.p_str[1])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[1]=True
            self.nowUsed('''self.p_str[1]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[1])
                    if __aV != __bV['''self.p_str[1]''']: print('=>',self.prettyName('''self.p_str[1]''') + ' =',__aV, ':',type(self.p_str[1]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard208(self):
        return (self.p_str[1] is not None)
    
    def act209(self):
        '''
        item = get_item(str2)
        '''
        self.__test.append(('''item = get_item(self.p_str[2]) ''',self.guard209,self.act209))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''item = get_item(self.p_str[2]) '''))
            try: __bV['''self.p_str[2]'''] = repr(self.p_str[2]); print(self.prettyName('''self.p_str[2]''') + ' =', __bV['''self.p_str[2]'''], ':',type(self.p_str[2]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            item = get_item(self.p_str[2])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[2]=True
            self.nowUsed('''self.p_str[2]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[2])
                    if __aV != __bV['''self.p_str[2]''']: print('=>',self.prettyName('''self.p_str[2]''') + ' =',__aV, ':',type(self.p_str[2]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard209(self):
        return (self.p_str[2] is not None)
    
    def act210(self):
        '''
        item = get_item(str3)
        '''
        self.__test.append(('''item = get_item(self.p_str[3]) ''',self.guard210,self.act210))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''item = get_item(self.p_str[3]) '''))
            try: __bV['''self.p_str[3]'''] = repr(self.p_str[3]); print(self.prettyName('''self.p_str[3]''') + ' =', __bV['''self.p_str[3]'''], ':',type(self.p_str[3]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            item = get_item(self.p_str[3])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[3]=True
            self.nowUsed('''self.p_str[3]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[3])
                    if __aV != __bV['''self.p_str[3]''']: print('=>',self.prettyName('''self.p_str[3]''') + ' =',__aV, ':',type(self.p_str[3]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard210(self):
        return (self.p_str[3] is not None)
    
    def act211(self):
        '''
        item = get_item(str4)
        '''
        self.__test.append(('''item = get_item(self.p_str[4]) ''',self.guard211,self.act211))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''item = get_item(self.p_str[4]) '''))
            try: __bV['''self.p_str[4]'''] = repr(self.p_str[4]); print(self.prettyName('''self.p_str[4]''') + ' =', __bV['''self.p_str[4]'''], ':',type(self.p_str[4]))
            except: pass
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            item = get_item(self.p_str[4])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            self.p_str_used[4]=True
            self.nowUsed('''self.p_str[4]''')
            try: test_after_each(self)
            except: pass
            if self.__verboseActions:
                try:
                    __aV = repr(self.p_str[4])
                    if __aV != __bV['''self.p_str[4]''']: print('=>',self.prettyName('''self.p_str[4]''') + ' =',__aV, ':',type(self.p_str[4]))
                except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard211(self):
        return (self.p_str[4] is not None)
    
    def act212(self):
        '''
        %action%
        '''
        self.__test.append(('''%action% ''',self.guard212,self.act212))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''%action% '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            action
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard212(self):
        return True
    
    def act213(self):
        '''
        items = get_items()
        '''
        self.__test.append(('''items = get_items() ''',self.guard213,self.act213))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''items = get_items() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            items = get_items()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard213(self):
        return True
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__importModules = []
        self.__features = []
        self.__replayBacktrack = False
        self.__cov = coverage.coverage(branch=True, source=self.moduleLocations(),    omit='sut.py'    )
        self.__cov._warn_no_data = False
        self.__collectCov = True
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
        self.__oldCovData = None
        self.__useCould = False
        self.__actionCould = True
        self.verboseActionCould = False
        self.__test = []
        self.__failure = None
        self.__warning = None
        self.__raised = None
        self.__refRaised = None
        self.__poolsNone = set([])
        self.__poolsUsed = set([])
        self.__disabledByNone = set([])
        self.__disabledByUsed = set([])
        self.p_str = {}
        self.p_str_used = {}
        self.p_str[0] = None
        self.p_str_used[0] = True
        self.p_str[1] = None
        self.p_str_used[1] = True
        self.p_str[2] = None
        self.p_str_used[2] = True
        self.p_str[3] = None
        self.p_str_used[3] = True
        self.p_str[4] = None
        self.p_str_used[4] = True
        self.p_int = {}
        self.p_int_used = {}
        self.p_int[0] = None
        self.p_int_used[0] = True
        self.p_int[1] = None
        self.p_int_used[1] = True
        self.p_int[2] = None
        self.p_int_used[2] = True
        self.p_int[3] = None
        self.p_int_used[3] = True
        self.p_int[4] = None
        self.p_int_used[4] = True
        self.p_item = {}
        self.p_item_used = {}
        self.p_item[0] = None
        self.p_item_used[0] = True
        self.p_item[1] = None
        self.p_item_used[1] = True
        self.p_item[2] = None
        self.p_item_used[2] = True
        self.p_category = {}
        self.p_category_used = {}
        self.p_category[0] = None
        self.p_category_used[0] = True
        self.p_category[1] = None
        self.p_category_used[1] = True
    # BEGIN INITIALIZATION CODE
    # END INITIALIZATION CODE
        self.__SUTName = """database"""
        self.__actions = []
        self.__names = {}
        self.__poolPrefix = "self.p_"
        self.__names["<<RESTART>>"] = ("<<RESTART>>", lambda x: True, lambda x: self.restart())
        self.__actionClass = {}
        self.__swarmConfig = None
        self.__actionClasses = []
        self.__essentialClasses = []
        self.__actionClasses.append('''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__actionClasses.append('''<int> := 100, 20, 30, 150, 50 ''')
        self.__actionClasses.append('''<category> := "Electronics", "Apparel" ''')
        self.__actionClasses.append('''<item> := {0..4}  # Using indices to refer to items by position ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''add_category(<category>) ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''choice := {0..4} ''')
        self.__actionClasses.append('''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''choice := {0..4} ''')
        self.__actionClasses.append('''update_item(<str>, quantity=<int>) ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''choice := {0..4} ''')
        self.__actionClasses.append('''update_item(<str>, price=<int>) ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''choice := {0..4} ''')
        self.__actionClasses.append('''delete_item(<str>) ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''item := get_item(<str>) ''')
        self.__actionClasses.append('''<action> ''')
        self.__actionClasses.append('''items := get_items() ''')
        self.__dependencies = {}
        self.__dependencies['''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = []
        self.__dependencies['''<int> := 100, 20, 30, 150, 50 '''] = []
        self.__dependencies['''<category> := "Electronics", "Apparel" '''] = []
        self.__dependencies['''<item> := {0..4}  # Using indices to refer to items by position '''] = []
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''add_category(<category>) '''] = []
        self.__dependencies['''add_category(<category>) '''].append(['<category> := "Electronics", "Apparel" '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''choice := {0..4} '''] = []
        self.__dependencies['''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''] = []
        self.__dependencies['''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''].append(['<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '])
        self.__dependencies['''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''].append(['<int> := 100, 20, 30, 150, 50 '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''choice := {0..4} '''] = []
        self.__dependencies['''update_item(<str>, quantity=<int>) '''] = []
        self.__dependencies['''update_item(<str>, quantity=<int>) '''].append(['<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '])
        self.__dependencies['''update_item(<str>, quantity=<int>) '''].append(['<int> := 100, 20, 30, 150, 50 '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''choice := {0..4} '''] = []
        self.__dependencies['''update_item(<str>, price=<int>) '''] = []
        self.__dependencies['''update_item(<str>, price=<int>) '''].append(['<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '])
        self.__dependencies['''update_item(<str>, price=<int>) '''].append(['<int> := 100, 20, 30, 150, 50 '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''choice := {0..4} '''] = []
        self.__dependencies['''delete_item(<str>) '''] = []
        self.__dependencies['''delete_item(<str>) '''].append(['<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''item := get_item(<str>) '''] = []
        self.__dependencies['''item := get_item(<str>) '''].append(['<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '])
        self.__dependencies['''<action> '''] = []
        self.__dependencies['''items := get_items() '''] = []
        self.__orderings = {}
        self.__okExcepts = {}
        self.__preCode = {}
        self.__refCode = {}
        self.__propCode = {}
        self.__orderings["<<RESTART>>"] = -1
        self.__log = None
        self.__enumerateEnabled = False
        self.__verboseActions = False
        self.__verbosePrintOpaque = True
        self.__logAction = self.logPrint
        self.__relaxUsedRestriction = False
        self.__doReload = True
        self.__assumptionViolated = None
        self.__noReassigns = False
        self.__safeSafelyMode = False
        self.__simplifyCache = {}
        self.__fastPoolStates = True
        self.__pools = []
        self.__poolUsers = {}
        self.__poolInitializers = {}
        self.__psize = {}
        self.__consts = []
        self.__opaque = []
        self.__abstraction = {}
        self.__psize["str"] = 5
        self.__pools.append("self.p_str")
        self.__psize["int"] = 5
        self.__pools.append("self.p_int")
        self.__psize["item"] = 3
        self.__pools.append("self.p_item")
        self.__psize["category"] = 2
        self.__pools.append("self.p_category")
        self.__poolUsers['''self.p_category[0]'''] = set([])
        self.__poolUsers['''self.p_category[0]'''].add('''add_category(self.p_category[0]) ''')
        self.__poolUsers['''self.p_category[1]'''] = set([])
        self.__poolUsers['''self.p_category[1]'''].add('''add_category(self.p_category[1]) ''')
        self.__poolUsers['''self.p_str[0]'''] = set([])
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''update_item(self.p_str[0], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''delete_item(self.p_str[0]) ''')
        self.__poolUsers['''self.p_str[0]'''].add('''item = get_item(self.p_str[0]) ''')
        self.__poolUsers['''self.p_int[0]'''] = set([])
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[0], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[1], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[2], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[3], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[4], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[0], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[1], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[2], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[3], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[0]'''].add('''update_item(self.p_str[4], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_int[1]'''] = set([])
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[0], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[2], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[3], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[4], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[0], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[1], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[2], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[3], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[1]'''].add('''update_item(self.p_str[4], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_int[2]'''] = set([])
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[0], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[1], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[3], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[4], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[0], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[1], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[2], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[3], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[2]'''].add('''update_item(self.p_str[4], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_int[3]'''] = set([])
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[0], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[1], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[2], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[4], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[0], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[1], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[2], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[3], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[3]'''].add('''update_item(self.p_str[4], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_int[4]'''] = set([])
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[0], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[1], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[2], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[3], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[0], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[1], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[2], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[3], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_int[4]'''].add('''update_item(self.p_str[4], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[1]'''] = set([])
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''update_item(self.p_str[1], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''delete_item(self.p_str[1]) ''')
        self.__poolUsers['''self.p_str[1]'''].add('''item = get_item(self.p_str[1]) ''')
        self.__poolUsers['''self.p_str[2]'''] = set([])
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''update_item(self.p_str[2], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''delete_item(self.p_str[2]) ''')
        self.__poolUsers['''self.p_str[2]'''].add('''item = get_item(self.p_str[2]) ''')
        self.__poolUsers['''self.p_str[3]'''] = set([])
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''update_item(self.p_str[3], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''delete_item(self.p_str[3]) ''')
        self.__poolUsers['''self.p_str[3]'''].add('''item = get_item(self.p_str[3]) ''')
        self.__poolUsers['''self.p_str[4]'''] = set([])
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], quantity=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], price=self.p_int[0]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], price=self.p_int[1]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], price=self.p_int[2]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], price=self.p_int[3]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''update_item(self.p_str[4], price=self.p_int[4]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''delete_item(self.p_str[4]) ''')
        self.__poolUsers['''self.p_str[4]'''].add('''item = get_item(self.p_str[4]) ''')
        self.__poolInitializers['''self.p_str[0]'''] = set([])
        self.__poolInitializers['''self.p_str[0]'''].add('''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__poolInitializers['''self.p_str[1]'''] = set([])
        self.__poolInitializers['''self.p_str[1]'''].add('''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__poolInitializers['''self.p_str[2]'''] = set([])
        self.__poolInitializers['''self.p_str[2]'''].add('''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__poolInitializers['''self.p_str[3]'''] = set([])
        self.__poolInitializers['''self.p_str[3]'''].add('''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__poolInitializers['''self.p_str[4]'''] = set([])
        self.__poolInitializers['''self.p_str[4]'''].add('''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''')
        self.__poolInitializers['''self.p_int[0]'''] = set([])
        self.__poolInitializers['''self.p_int[0]'''].add('''self.p_int[0] = 100, 20, 30, 150, 50 ''')
        self.__poolInitializers['''self.p_int[1]'''] = set([])
        self.__poolInitializers['''self.p_int[1]'''].add('''self.p_int[1] = 100, 20, 30, 150, 50 ''')
        self.__poolInitializers['''self.p_int[2]'''] = set([])
        self.__poolInitializers['''self.p_int[2]'''].add('''self.p_int[2] = 100, 20, 30, 150, 50 ''')
        self.__poolInitializers['''self.p_int[3]'''] = set([])
        self.__poolInitializers['''self.p_int[3]'''].add('''self.p_int[3] = 100, 20, 30, 150, 50 ''')
        self.__poolInitializers['''self.p_int[4]'''] = set([])
        self.__poolInitializers['''self.p_int[4]'''].add('''self.p_int[4] = 100, 20, 30, 150, 50 ''')
        self.__poolInitializers['''self.p_category[0]'''] = set([])
        self.__poolInitializers['''self.p_category[0]'''].add('''self.p_category[0] = "Electronics", "Apparel" ''')
        self.__poolInitializers['''self.p_category[1]'''] = set([])
        self.__poolInitializers['''self.p_category[1]'''].add('''self.p_category[1] = "Electronics", "Apparel" ''')
        self.__poolInitializers['''self.p_item[0]'''] = set([])
        self.__poolInitializers['''self.p_item[0]'''].add('''self.p_item[0] = {0..4}  # Using indices to refer to items by position ''')
        self.__poolInitializers['''self.p_item[1]'''] = set([])
        self.__poolInitializers['''self.p_item[1]'''].add('''self.p_item[1] = {0..4}  # Using indices to refer to items by position ''')
        self.__poolInitializers['''self.p_item[2]'''] = set([])
        self.__poolInitializers['''self.p_item[2]'''].add('''self.p_item[2] = {0..4}  # Using indices to refer to items by position ''')
        if self.__useCould: self.computeInitialEnabled()
        
        self.__actions.append(('''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard0,self.act0))
        self.__names['''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ('''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard0,self.act0)
        self.__actionClass['''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = '''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''
        self.__orderings['''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = 1
        self.__okExcepts['''self.p_str[0] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ''''''
        
        self.__actions.append(('''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard1,self.act1))
        self.__names['''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ('''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard1,self.act1)
        self.__actionClass['''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = '''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''
        self.__orderings['''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = 2
        self.__okExcepts['''self.p_str[1] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ''''''
        
        self.__actions.append(('''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard2,self.act2))
        self.__names['''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ('''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard2,self.act2)
        self.__actionClass['''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = '''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''
        self.__orderings['''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = 3
        self.__okExcepts['''self.p_str[2] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ''''''
        
        self.__actions.append(('''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard3,self.act3))
        self.__names['''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ('''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard3,self.act3)
        self.__actionClass['''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = '''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''
        self.__orderings['''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = 4
        self.__okExcepts['''self.p_str[3] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ''''''
        
        self.__actions.append(('''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard4,self.act4))
        self.__names['''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ('''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" ''',self.guard4,self.act4)
        self.__actionClass['''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = '''<str> := "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''
        self.__orderings['''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = 5
        self.__okExcepts['''self.p_str[4] = "Keyboard", "Mouse", "Monitor", "Laptop", "Camera" '''] = ''''''
        
        self.__actions.append(('''self.p_int[0] = 100, 20, 30, 150, 50 ''',self.guard5,self.act5))
        self.__names['''self.p_int[0] = 100, 20, 30, 150, 50 '''] = ('''self.p_int[0] = 100, 20, 30, 150, 50 ''',self.guard5,self.act5)
        self.__actionClass['''self.p_int[0] = 100, 20, 30, 150, 50 '''] = '''<int> := 100, 20, 30, 150, 50 '''
        self.__orderings['''self.p_int[0] = 100, 20, 30, 150, 50 '''] = 6
        self.__okExcepts['''self.p_int[0] = 100, 20, 30, 150, 50 '''] = ''''''
        
        self.__actions.append(('''self.p_int[1] = 100, 20, 30, 150, 50 ''',self.guard6,self.act6))
        self.__names['''self.p_int[1] = 100, 20, 30, 150, 50 '''] = ('''self.p_int[1] = 100, 20, 30, 150, 50 ''',self.guard6,self.act6)
        self.__actionClass['''self.p_int[1] = 100, 20, 30, 150, 50 '''] = '''<int> := 100, 20, 30, 150, 50 '''
        self.__orderings['''self.p_int[1] = 100, 20, 30, 150, 50 '''] = 7
        self.__okExcepts['''self.p_int[1] = 100, 20, 30, 150, 50 '''] = ''''''
        
        self.__actions.append(('''self.p_int[2] = 100, 20, 30, 150, 50 ''',self.guard7,self.act7))
        self.__names['''self.p_int[2] = 100, 20, 30, 150, 50 '''] = ('''self.p_int[2] = 100, 20, 30, 150, 50 ''',self.guard7,self.act7)
        self.__actionClass['''self.p_int[2] = 100, 20, 30, 150, 50 '''] = '''<int> := 100, 20, 30, 150, 50 '''
        self.__orderings['''self.p_int[2] = 100, 20, 30, 150, 50 '''] = 8
        self.__okExcepts['''self.p_int[2] = 100, 20, 30, 150, 50 '''] = ''''''
        
        self.__actions.append(('''self.p_int[3] = 100, 20, 30, 150, 50 ''',self.guard8,self.act8))
        self.__names['''self.p_int[3] = 100, 20, 30, 150, 50 '''] = ('''self.p_int[3] = 100, 20, 30, 150, 50 ''',self.guard8,self.act8)
        self.__actionClass['''self.p_int[3] = 100, 20, 30, 150, 50 '''] = '''<int> := 100, 20, 30, 150, 50 '''
        self.__orderings['''self.p_int[3] = 100, 20, 30, 150, 50 '''] = 9
        self.__okExcepts['''self.p_int[3] = 100, 20, 30, 150, 50 '''] = ''''''
        
        self.__actions.append(('''self.p_int[4] = 100, 20, 30, 150, 50 ''',self.guard9,self.act9))
        self.__names['''self.p_int[4] = 100, 20, 30, 150, 50 '''] = ('''self.p_int[4] = 100, 20, 30, 150, 50 ''',self.guard9,self.act9)
        self.__actionClass['''self.p_int[4] = 100, 20, 30, 150, 50 '''] = '''<int> := 100, 20, 30, 150, 50 '''
        self.__orderings['''self.p_int[4] = 100, 20, 30, 150, 50 '''] = 10
        self.__okExcepts['''self.p_int[4] = 100, 20, 30, 150, 50 '''] = ''''''
        
        self.__actions.append(('''self.p_category[0] = "Electronics", "Apparel" ''',self.guard10,self.act10))
        self.__names['''self.p_category[0] = "Electronics", "Apparel" '''] = ('''self.p_category[0] = "Electronics", "Apparel" ''',self.guard10,self.act10)
        self.__actionClass['''self.p_category[0] = "Electronics", "Apparel" '''] = '''<category> := "Electronics", "Apparel" '''
        self.__orderings['''self.p_category[0] = "Electronics", "Apparel" '''] = 11
        self.__okExcepts['''self.p_category[0] = "Electronics", "Apparel" '''] = ''''''
        
        self.__actions.append(('''self.p_category[1] = "Electronics", "Apparel" ''',self.guard11,self.act11))
        self.__names['''self.p_category[1] = "Electronics", "Apparel" '''] = ('''self.p_category[1] = "Electronics", "Apparel" ''',self.guard11,self.act11)
        self.__actionClass['''self.p_category[1] = "Electronics", "Apparel" '''] = '''<category> := "Electronics", "Apparel" '''
        self.__orderings['''self.p_category[1] = "Electronics", "Apparel" '''] = 12
        self.__okExcepts['''self.p_category[1] = "Electronics", "Apparel" '''] = ''''''
        
        self.__actions.append(('''self.p_item[0] = {0..4}  # Using indices to refer to items by position ''',self.guard12,self.act12))
        self.__names['''self.p_item[0] = {0..4}  # Using indices to refer to items by position '''] = ('''self.p_item[0] = {0..4}  # Using indices to refer to items by position ''',self.guard12,self.act12)
        self.__actionClass['''self.p_item[0] = {0..4}  # Using indices to refer to items by position '''] = '''<item> := {0..4}  # Using indices to refer to items by position '''
        self.__orderings['''self.p_item[0] = {0..4}  # Using indices to refer to items by position '''] = 13
        self.__okExcepts['''self.p_item[0] = {0..4}  # Using indices to refer to items by position '''] = ''''''
        
        self.__actions.append(('''self.p_item[1] = {0..4}  # Using indices to refer to items by position ''',self.guard13,self.act13))
        self.__names['''self.p_item[1] = {0..4}  # Using indices to refer to items by position '''] = ('''self.p_item[1] = {0..4}  # Using indices to refer to items by position ''',self.guard13,self.act13)
        self.__actionClass['''self.p_item[1] = {0..4}  # Using indices to refer to items by position '''] = '''<item> := {0..4}  # Using indices to refer to items by position '''
        self.__orderings['''self.p_item[1] = {0..4}  # Using indices to refer to items by position '''] = 14
        self.__okExcepts['''self.p_item[1] = {0..4}  # Using indices to refer to items by position '''] = ''''''
        
        self.__actions.append(('''self.p_item[2] = {0..4}  # Using indices to refer to items by position ''',self.guard14,self.act14))
        self.__names['''self.p_item[2] = {0..4}  # Using indices to refer to items by position '''] = ('''self.p_item[2] = {0..4}  # Using indices to refer to items by position ''',self.guard14,self.act14)
        self.__actionClass['''self.p_item[2] = {0..4}  # Using indices to refer to items by position '''] = '''<item> := {0..4}  # Using indices to refer to items by position '''
        self.__orderings['''self.p_item[2] = {0..4}  # Using indices to refer to items by position '''] = 15
        self.__okExcepts['''self.p_item[2] = {0..4}  # Using indices to refer to items by position '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard15,self.act15))
        self.__names['''%action% '''] = ('''%action% ''',self.guard15,self.act15)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 16
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''add_category(self.p_category[0]) ''',self.guard16,self.act16))
        self.__names['''add_category(self.p_category[0]) '''] = ('''add_category(self.p_category[0]) ''',self.guard16,self.act16)
        self.__actionClass['''add_category(self.p_category[0]) '''] = '''add_category(<category>) '''
        self.__orderings['''add_category(self.p_category[0]) '''] = 17
        self.__okExcepts['''add_category(self.p_category[0]) '''] = ''''''
        
        self.__actions.append(('''add_category(self.p_category[1]) ''',self.guard17,self.act17))
        self.__names['''add_category(self.p_category[1]) '''] = ('''add_category(self.p_category[1]) ''',self.guard17,self.act17)
        self.__actionClass['''add_category(self.p_category[1]) '''] = '''add_category(<category>) '''
        self.__orderings['''add_category(self.p_category[1]) '''] = 18
        self.__okExcepts['''add_category(self.p_category[1]) '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard18,self.act18))
        self.__names['''%action% '''] = ('''%action% ''',self.guard18,self.act18)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 19
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''choice = {0..4} ''',self.guard19,self.act19))
        self.__names['''choice = {0..4} '''] = ('''choice = {0..4} ''',self.guard19,self.act19)
        self.__actionClass['''choice = {0..4} '''] = '''choice := {0..4} '''
        self.__orderings['''choice = {0..4} '''] = 20
        self.__okExcepts['''choice = {0..4} '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard20,self.act20))
        self.__names['''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard20,self.act20)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 21
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard21,self.act21))
        self.__names['''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard21,self.act21)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 22
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard22,self.act22))
        self.__names['''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard22,self.act22)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 23
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard23,self.act23))
        self.__names['''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard23,self.act23)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 24
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard24,self.act24))
        self.__names['''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard24,self.act24)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 25
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard25,self.act25))
        self.__names['''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard25,self.act25)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 26
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard26,self.act26))
        self.__names['''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard26,self.act26)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 27
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard27,self.act27))
        self.__names['''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard27,self.act27)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 28
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard28,self.act28))
        self.__names['''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard28,self.act28)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 29
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard29,self.act29))
        self.__names['''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard29,self.act29)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 30
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard30,self.act30))
        self.__names['''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard30,self.act30)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 31
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard31,self.act31))
        self.__names['''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard31,self.act31)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 32
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard32,self.act32))
        self.__names['''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard32,self.act32)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 33
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard33,self.act33))
        self.__names['''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard33,self.act33)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 34
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard34,self.act34))
        self.__names['''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard34,self.act34)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 35
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard35,self.act35))
        self.__names['''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard35,self.act35)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 36
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard36,self.act36))
        self.__names['''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard36,self.act36)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 37
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard37,self.act37))
        self.__names['''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard37,self.act37)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 38
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard38,self.act38))
        self.__names['''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard38,self.act38)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 39
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard39,self.act39))
        self.__names['''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard39,self.act39)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 40
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard40,self.act40))
        self.__names['''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard40,self.act40)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 41
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard41,self.act41))
        self.__names['''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard41,self.act41)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 42
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard42,self.act42))
        self.__names['''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard42,self.act42)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 43
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard43,self.act43))
        self.__names['''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard43,self.act43)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 44
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard44,self.act44))
        self.__names['''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard44,self.act44)
        self.__actionClass['''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 45
        self.__okExcepts['''add_item(self.p_str[0], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard45,self.act45))
        self.__names['''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard45,self.act45)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 46
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard46,self.act46))
        self.__names['''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard46,self.act46)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 47
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard47,self.act47))
        self.__names['''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard47,self.act47)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 48
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard48,self.act48))
        self.__names['''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard48,self.act48)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 49
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard49,self.act49))
        self.__names['''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard49,self.act49)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 50
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard50,self.act50))
        self.__names['''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard50,self.act50)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 51
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard51,self.act51))
        self.__names['''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard51,self.act51)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 52
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard52,self.act52))
        self.__names['''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard52,self.act52)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 53
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard53,self.act53))
        self.__names['''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard53,self.act53)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 54
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard54,self.act54))
        self.__names['''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard54,self.act54)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 55
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard55,self.act55))
        self.__names['''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard55,self.act55)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 56
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard56,self.act56))
        self.__names['''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard56,self.act56)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 57
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard57,self.act57))
        self.__names['''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard57,self.act57)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 58
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard58,self.act58))
        self.__names['''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard58,self.act58)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 59
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard59,self.act59))
        self.__names['''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard59,self.act59)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 60
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard60,self.act60))
        self.__names['''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard60,self.act60)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 61
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard61,self.act61))
        self.__names['''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard61,self.act61)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 62
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard62,self.act62))
        self.__names['''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard62,self.act62)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 63
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard63,self.act63))
        self.__names['''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard63,self.act63)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 64
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard64,self.act64))
        self.__names['''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard64,self.act64)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 65
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard65,self.act65))
        self.__names['''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard65,self.act65)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 66
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard66,self.act66))
        self.__names['''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard66,self.act66)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 67
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard67,self.act67))
        self.__names['''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard67,self.act67)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 68
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard68,self.act68))
        self.__names['''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard68,self.act68)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 69
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard69,self.act69))
        self.__names['''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard69,self.act69)
        self.__actionClass['''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 70
        self.__okExcepts['''add_item(self.p_str[1], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard70,self.act70))
        self.__names['''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard70,self.act70)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 71
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard71,self.act71))
        self.__names['''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard71,self.act71)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 72
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard72,self.act72))
        self.__names['''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard72,self.act72)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 73
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard73,self.act73))
        self.__names['''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard73,self.act73)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 74
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard74,self.act74))
        self.__names['''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard74,self.act74)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 75
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard75,self.act75))
        self.__names['''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard75,self.act75)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 76
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard76,self.act76))
        self.__names['''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard76,self.act76)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 77
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard77,self.act77))
        self.__names['''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard77,self.act77)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 78
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard78,self.act78))
        self.__names['''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard78,self.act78)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 79
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard79,self.act79))
        self.__names['''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard79,self.act79)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 80
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard80,self.act80))
        self.__names['''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard80,self.act80)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 81
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard81,self.act81))
        self.__names['''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard81,self.act81)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 82
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard82,self.act82))
        self.__names['''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard82,self.act82)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 83
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard83,self.act83))
        self.__names['''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard83,self.act83)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 84
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard84,self.act84))
        self.__names['''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard84,self.act84)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 85
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard85,self.act85))
        self.__names['''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard85,self.act85)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 86
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard86,self.act86))
        self.__names['''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard86,self.act86)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 87
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard87,self.act87))
        self.__names['''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard87,self.act87)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 88
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard88,self.act88))
        self.__names['''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard88,self.act88)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 89
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard89,self.act89))
        self.__names['''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard89,self.act89)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 90
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard90,self.act90))
        self.__names['''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard90,self.act90)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 91
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard91,self.act91))
        self.__names['''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard91,self.act91)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 92
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard92,self.act92))
        self.__names['''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard92,self.act92)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 93
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard93,self.act93))
        self.__names['''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard93,self.act93)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 94
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard94,self.act94))
        self.__names['''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard94,self.act94)
        self.__actionClass['''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 95
        self.__okExcepts['''add_item(self.p_str[2], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard95,self.act95))
        self.__names['''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard95,self.act95)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 96
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard96,self.act96))
        self.__names['''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard96,self.act96)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 97
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard97,self.act97))
        self.__names['''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard97,self.act97)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 98
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard98,self.act98))
        self.__names['''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard98,self.act98)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 99
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard99,self.act99))
        self.__names['''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard99,self.act99)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 100
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard100,self.act100))
        self.__names['''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard100,self.act100)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 101
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard101,self.act101))
        self.__names['''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard101,self.act101)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 102
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard102,self.act102))
        self.__names['''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard102,self.act102)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 103
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard103,self.act103))
        self.__names['''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard103,self.act103)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 104
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard104,self.act104))
        self.__names['''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard104,self.act104)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 105
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard105,self.act105))
        self.__names['''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard105,self.act105)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 106
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard106,self.act106))
        self.__names['''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard106,self.act106)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 107
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard107,self.act107))
        self.__names['''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard107,self.act107)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 108
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard108,self.act108))
        self.__names['''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard108,self.act108)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 109
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard109,self.act109))
        self.__names['''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard109,self.act109)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 110
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard110,self.act110))
        self.__names['''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard110,self.act110)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 111
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard111,self.act111))
        self.__names['''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard111,self.act111)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 112
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard112,self.act112))
        self.__names['''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard112,self.act112)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 113
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard113,self.act113))
        self.__names['''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard113,self.act113)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 114
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard114,self.act114))
        self.__names['''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard114,self.act114)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 115
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard115,self.act115))
        self.__names['''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard115,self.act115)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 116
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard116,self.act116))
        self.__names['''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard116,self.act116)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 117
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard117,self.act117))
        self.__names['''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard117,self.act117)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 118
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard118,self.act118))
        self.__names['''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard118,self.act118)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 119
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard119,self.act119))
        self.__names['''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard119,self.act119)
        self.__actionClass['''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 120
        self.__okExcepts['''add_item(self.p_str[3], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard120,self.act120))
        self.__names['''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard120,self.act120)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 121
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[0], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard121,self.act121))
        self.__names['''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard121,self.act121)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 122
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[0], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard122,self.act122))
        self.__names['''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard122,self.act122)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 123
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[0], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard123,self.act123))
        self.__names['''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard123,self.act123)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 124
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[0], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard124,self.act124))
        self.__names['''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard124,self.act124)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 125
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[0], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard125,self.act125))
        self.__names['''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard125,self.act125)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 126
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[1], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard126,self.act126))
        self.__names['''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard126,self.act126)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 127
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[1], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard127,self.act127))
        self.__names['''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard127,self.act127)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 128
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[1], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard128,self.act128))
        self.__names['''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard128,self.act128)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 129
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[1], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard129,self.act129))
        self.__names['''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard129,self.act129)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 130
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[1], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard130,self.act130))
        self.__names['''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard130,self.act130)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 131
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[2], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard131,self.act131))
        self.__names['''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard131,self.act131)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 132
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[2], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard132,self.act132))
        self.__names['''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard132,self.act132)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 133
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[2], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard133,self.act133))
        self.__names['''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard133,self.act133)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 134
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[2], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard134,self.act134))
        self.__names['''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard134,self.act134)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 135
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[2], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard135,self.act135))
        self.__names['''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard135,self.act135)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 136
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[3], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard136,self.act136))
        self.__names['''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard136,self.act136)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 137
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[3], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard137,self.act137))
        self.__names['''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard137,self.act137)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 138
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[3], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard138,self.act138))
        self.__names['''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard138,self.act138)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 139
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[3], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard139,self.act139))
        self.__names['''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard139,self.act139)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 140
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[3], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard140,self.act140))
        self.__names['''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity ''',self.guard140,self.act140)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = 141
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[4], self.p_int[0], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard141,self.act141))
        self.__names['''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity ''',self.guard141,self.act141)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = 142
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[4], self.p_int[1], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard142,self.act142))
        self.__names['''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity ''',self.guard142,self.act142)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = 143
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[4], self.p_int[2], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard143,self.act143))
        self.__names['''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity ''',self.guard143,self.act143)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = 144
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[4], self.p_int[3], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard144,self.act144))
        self.__names['''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ('''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity ''',self.guard144,self.act144)
        self.__actionClass['''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = '''add_item(<str>, <int>, <int>, 1)  # Using default category ID for simplicity '''
        self.__orderings['''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = 145
        self.__okExcepts['''add_item(self.p_str[4], self.p_int[4], self.p_int[4], 1)  # Using default category ID for simplicity '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard145,self.act145))
        self.__names['''%action% '''] = ('''%action% ''',self.guard145,self.act145)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 146
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''choice = {0..4} ''',self.guard146,self.act146))
        self.__names['''choice = {0..4} '''] = ('''choice = {0..4} ''',self.guard146,self.act146)
        self.__actionClass['''choice = {0..4} '''] = '''choice := {0..4} '''
        self.__orderings['''choice = {0..4} '''] = 147
        self.__okExcepts['''choice = {0..4} '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], quantity=self.p_int[0]) ''',self.guard147,self.act147))
        self.__names['''update_item(self.p_str[0], quantity=self.p_int[0]) '''] = ('''update_item(self.p_str[0], quantity=self.p_int[0]) ''',self.guard147,self.act147)
        self.__actionClass['''update_item(self.p_str[0], quantity=self.p_int[0]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[0], quantity=self.p_int[0]) '''] = 148
        self.__okExcepts['''update_item(self.p_str[0], quantity=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], quantity=self.p_int[1]) ''',self.guard148,self.act148))
        self.__names['''update_item(self.p_str[0], quantity=self.p_int[1]) '''] = ('''update_item(self.p_str[0], quantity=self.p_int[1]) ''',self.guard148,self.act148)
        self.__actionClass['''update_item(self.p_str[0], quantity=self.p_int[1]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[0], quantity=self.p_int[1]) '''] = 149
        self.__okExcepts['''update_item(self.p_str[0], quantity=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], quantity=self.p_int[2]) ''',self.guard149,self.act149))
        self.__names['''update_item(self.p_str[0], quantity=self.p_int[2]) '''] = ('''update_item(self.p_str[0], quantity=self.p_int[2]) ''',self.guard149,self.act149)
        self.__actionClass['''update_item(self.p_str[0], quantity=self.p_int[2]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[0], quantity=self.p_int[2]) '''] = 150
        self.__okExcepts['''update_item(self.p_str[0], quantity=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], quantity=self.p_int[3]) ''',self.guard150,self.act150))
        self.__names['''update_item(self.p_str[0], quantity=self.p_int[3]) '''] = ('''update_item(self.p_str[0], quantity=self.p_int[3]) ''',self.guard150,self.act150)
        self.__actionClass['''update_item(self.p_str[0], quantity=self.p_int[3]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[0], quantity=self.p_int[3]) '''] = 151
        self.__okExcepts['''update_item(self.p_str[0], quantity=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], quantity=self.p_int[4]) ''',self.guard151,self.act151))
        self.__names['''update_item(self.p_str[0], quantity=self.p_int[4]) '''] = ('''update_item(self.p_str[0], quantity=self.p_int[4]) ''',self.guard151,self.act151)
        self.__actionClass['''update_item(self.p_str[0], quantity=self.p_int[4]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[0], quantity=self.p_int[4]) '''] = 152
        self.__okExcepts['''update_item(self.p_str[0], quantity=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], quantity=self.p_int[0]) ''',self.guard152,self.act152))
        self.__names['''update_item(self.p_str[1], quantity=self.p_int[0]) '''] = ('''update_item(self.p_str[1], quantity=self.p_int[0]) ''',self.guard152,self.act152)
        self.__actionClass['''update_item(self.p_str[1], quantity=self.p_int[0]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[1], quantity=self.p_int[0]) '''] = 153
        self.__okExcepts['''update_item(self.p_str[1], quantity=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], quantity=self.p_int[1]) ''',self.guard153,self.act153))
        self.__names['''update_item(self.p_str[1], quantity=self.p_int[1]) '''] = ('''update_item(self.p_str[1], quantity=self.p_int[1]) ''',self.guard153,self.act153)
        self.__actionClass['''update_item(self.p_str[1], quantity=self.p_int[1]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[1], quantity=self.p_int[1]) '''] = 154
        self.__okExcepts['''update_item(self.p_str[1], quantity=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], quantity=self.p_int[2]) ''',self.guard154,self.act154))
        self.__names['''update_item(self.p_str[1], quantity=self.p_int[2]) '''] = ('''update_item(self.p_str[1], quantity=self.p_int[2]) ''',self.guard154,self.act154)
        self.__actionClass['''update_item(self.p_str[1], quantity=self.p_int[2]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[1], quantity=self.p_int[2]) '''] = 155
        self.__okExcepts['''update_item(self.p_str[1], quantity=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], quantity=self.p_int[3]) ''',self.guard155,self.act155))
        self.__names['''update_item(self.p_str[1], quantity=self.p_int[3]) '''] = ('''update_item(self.p_str[1], quantity=self.p_int[3]) ''',self.guard155,self.act155)
        self.__actionClass['''update_item(self.p_str[1], quantity=self.p_int[3]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[1], quantity=self.p_int[3]) '''] = 156
        self.__okExcepts['''update_item(self.p_str[1], quantity=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], quantity=self.p_int[4]) ''',self.guard156,self.act156))
        self.__names['''update_item(self.p_str[1], quantity=self.p_int[4]) '''] = ('''update_item(self.p_str[1], quantity=self.p_int[4]) ''',self.guard156,self.act156)
        self.__actionClass['''update_item(self.p_str[1], quantity=self.p_int[4]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[1], quantity=self.p_int[4]) '''] = 157
        self.__okExcepts['''update_item(self.p_str[1], quantity=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], quantity=self.p_int[0]) ''',self.guard157,self.act157))
        self.__names['''update_item(self.p_str[2], quantity=self.p_int[0]) '''] = ('''update_item(self.p_str[2], quantity=self.p_int[0]) ''',self.guard157,self.act157)
        self.__actionClass['''update_item(self.p_str[2], quantity=self.p_int[0]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[2], quantity=self.p_int[0]) '''] = 158
        self.__okExcepts['''update_item(self.p_str[2], quantity=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], quantity=self.p_int[1]) ''',self.guard158,self.act158))
        self.__names['''update_item(self.p_str[2], quantity=self.p_int[1]) '''] = ('''update_item(self.p_str[2], quantity=self.p_int[1]) ''',self.guard158,self.act158)
        self.__actionClass['''update_item(self.p_str[2], quantity=self.p_int[1]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[2], quantity=self.p_int[1]) '''] = 159
        self.__okExcepts['''update_item(self.p_str[2], quantity=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], quantity=self.p_int[2]) ''',self.guard159,self.act159))
        self.__names['''update_item(self.p_str[2], quantity=self.p_int[2]) '''] = ('''update_item(self.p_str[2], quantity=self.p_int[2]) ''',self.guard159,self.act159)
        self.__actionClass['''update_item(self.p_str[2], quantity=self.p_int[2]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[2], quantity=self.p_int[2]) '''] = 160
        self.__okExcepts['''update_item(self.p_str[2], quantity=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], quantity=self.p_int[3]) ''',self.guard160,self.act160))
        self.__names['''update_item(self.p_str[2], quantity=self.p_int[3]) '''] = ('''update_item(self.p_str[2], quantity=self.p_int[3]) ''',self.guard160,self.act160)
        self.__actionClass['''update_item(self.p_str[2], quantity=self.p_int[3]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[2], quantity=self.p_int[3]) '''] = 161
        self.__okExcepts['''update_item(self.p_str[2], quantity=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], quantity=self.p_int[4]) ''',self.guard161,self.act161))
        self.__names['''update_item(self.p_str[2], quantity=self.p_int[4]) '''] = ('''update_item(self.p_str[2], quantity=self.p_int[4]) ''',self.guard161,self.act161)
        self.__actionClass['''update_item(self.p_str[2], quantity=self.p_int[4]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[2], quantity=self.p_int[4]) '''] = 162
        self.__okExcepts['''update_item(self.p_str[2], quantity=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], quantity=self.p_int[0]) ''',self.guard162,self.act162))
        self.__names['''update_item(self.p_str[3], quantity=self.p_int[0]) '''] = ('''update_item(self.p_str[3], quantity=self.p_int[0]) ''',self.guard162,self.act162)
        self.__actionClass['''update_item(self.p_str[3], quantity=self.p_int[0]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[3], quantity=self.p_int[0]) '''] = 163
        self.__okExcepts['''update_item(self.p_str[3], quantity=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], quantity=self.p_int[1]) ''',self.guard163,self.act163))
        self.__names['''update_item(self.p_str[3], quantity=self.p_int[1]) '''] = ('''update_item(self.p_str[3], quantity=self.p_int[1]) ''',self.guard163,self.act163)
        self.__actionClass['''update_item(self.p_str[3], quantity=self.p_int[1]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[3], quantity=self.p_int[1]) '''] = 164
        self.__okExcepts['''update_item(self.p_str[3], quantity=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], quantity=self.p_int[2]) ''',self.guard164,self.act164))
        self.__names['''update_item(self.p_str[3], quantity=self.p_int[2]) '''] = ('''update_item(self.p_str[3], quantity=self.p_int[2]) ''',self.guard164,self.act164)
        self.__actionClass['''update_item(self.p_str[3], quantity=self.p_int[2]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[3], quantity=self.p_int[2]) '''] = 165
        self.__okExcepts['''update_item(self.p_str[3], quantity=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], quantity=self.p_int[3]) ''',self.guard165,self.act165))
        self.__names['''update_item(self.p_str[3], quantity=self.p_int[3]) '''] = ('''update_item(self.p_str[3], quantity=self.p_int[3]) ''',self.guard165,self.act165)
        self.__actionClass['''update_item(self.p_str[3], quantity=self.p_int[3]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[3], quantity=self.p_int[3]) '''] = 166
        self.__okExcepts['''update_item(self.p_str[3], quantity=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], quantity=self.p_int[4]) ''',self.guard166,self.act166))
        self.__names['''update_item(self.p_str[3], quantity=self.p_int[4]) '''] = ('''update_item(self.p_str[3], quantity=self.p_int[4]) ''',self.guard166,self.act166)
        self.__actionClass['''update_item(self.p_str[3], quantity=self.p_int[4]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[3], quantity=self.p_int[4]) '''] = 167
        self.__okExcepts['''update_item(self.p_str[3], quantity=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], quantity=self.p_int[0]) ''',self.guard167,self.act167))
        self.__names['''update_item(self.p_str[4], quantity=self.p_int[0]) '''] = ('''update_item(self.p_str[4], quantity=self.p_int[0]) ''',self.guard167,self.act167)
        self.__actionClass['''update_item(self.p_str[4], quantity=self.p_int[0]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[4], quantity=self.p_int[0]) '''] = 168
        self.__okExcepts['''update_item(self.p_str[4], quantity=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], quantity=self.p_int[1]) ''',self.guard168,self.act168))
        self.__names['''update_item(self.p_str[4], quantity=self.p_int[1]) '''] = ('''update_item(self.p_str[4], quantity=self.p_int[1]) ''',self.guard168,self.act168)
        self.__actionClass['''update_item(self.p_str[4], quantity=self.p_int[1]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[4], quantity=self.p_int[1]) '''] = 169
        self.__okExcepts['''update_item(self.p_str[4], quantity=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], quantity=self.p_int[2]) ''',self.guard169,self.act169))
        self.__names['''update_item(self.p_str[4], quantity=self.p_int[2]) '''] = ('''update_item(self.p_str[4], quantity=self.p_int[2]) ''',self.guard169,self.act169)
        self.__actionClass['''update_item(self.p_str[4], quantity=self.p_int[2]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[4], quantity=self.p_int[2]) '''] = 170
        self.__okExcepts['''update_item(self.p_str[4], quantity=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], quantity=self.p_int[3]) ''',self.guard170,self.act170))
        self.__names['''update_item(self.p_str[4], quantity=self.p_int[3]) '''] = ('''update_item(self.p_str[4], quantity=self.p_int[3]) ''',self.guard170,self.act170)
        self.__actionClass['''update_item(self.p_str[4], quantity=self.p_int[3]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[4], quantity=self.p_int[3]) '''] = 171
        self.__okExcepts['''update_item(self.p_str[4], quantity=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], quantity=self.p_int[4]) ''',self.guard171,self.act171))
        self.__names['''update_item(self.p_str[4], quantity=self.p_int[4]) '''] = ('''update_item(self.p_str[4], quantity=self.p_int[4]) ''',self.guard171,self.act171)
        self.__actionClass['''update_item(self.p_str[4], quantity=self.p_int[4]) '''] = '''update_item(<str>, quantity=<int>) '''
        self.__orderings['''update_item(self.p_str[4], quantity=self.p_int[4]) '''] = 172
        self.__okExcepts['''update_item(self.p_str[4], quantity=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard172,self.act172))
        self.__names['''%action% '''] = ('''%action% ''',self.guard172,self.act172)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 173
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''choice = {0..4} ''',self.guard173,self.act173))
        self.__names['''choice = {0..4} '''] = ('''choice = {0..4} ''',self.guard173,self.act173)
        self.__actionClass['''choice = {0..4} '''] = '''choice := {0..4} '''
        self.__orderings['''choice = {0..4} '''] = 174
        self.__okExcepts['''choice = {0..4} '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], price=self.p_int[0]) ''',self.guard174,self.act174))
        self.__names['''update_item(self.p_str[0], price=self.p_int[0]) '''] = ('''update_item(self.p_str[0], price=self.p_int[0]) ''',self.guard174,self.act174)
        self.__actionClass['''update_item(self.p_str[0], price=self.p_int[0]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[0], price=self.p_int[0]) '''] = 175
        self.__okExcepts['''update_item(self.p_str[0], price=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], price=self.p_int[1]) ''',self.guard175,self.act175))
        self.__names['''update_item(self.p_str[0], price=self.p_int[1]) '''] = ('''update_item(self.p_str[0], price=self.p_int[1]) ''',self.guard175,self.act175)
        self.__actionClass['''update_item(self.p_str[0], price=self.p_int[1]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[0], price=self.p_int[1]) '''] = 176
        self.__okExcepts['''update_item(self.p_str[0], price=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], price=self.p_int[2]) ''',self.guard176,self.act176))
        self.__names['''update_item(self.p_str[0], price=self.p_int[2]) '''] = ('''update_item(self.p_str[0], price=self.p_int[2]) ''',self.guard176,self.act176)
        self.__actionClass['''update_item(self.p_str[0], price=self.p_int[2]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[0], price=self.p_int[2]) '''] = 177
        self.__okExcepts['''update_item(self.p_str[0], price=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], price=self.p_int[3]) ''',self.guard177,self.act177))
        self.__names['''update_item(self.p_str[0], price=self.p_int[3]) '''] = ('''update_item(self.p_str[0], price=self.p_int[3]) ''',self.guard177,self.act177)
        self.__actionClass['''update_item(self.p_str[0], price=self.p_int[3]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[0], price=self.p_int[3]) '''] = 178
        self.__okExcepts['''update_item(self.p_str[0], price=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[0], price=self.p_int[4]) ''',self.guard178,self.act178))
        self.__names['''update_item(self.p_str[0], price=self.p_int[4]) '''] = ('''update_item(self.p_str[0], price=self.p_int[4]) ''',self.guard178,self.act178)
        self.__actionClass['''update_item(self.p_str[0], price=self.p_int[4]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[0], price=self.p_int[4]) '''] = 179
        self.__okExcepts['''update_item(self.p_str[0], price=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], price=self.p_int[0]) ''',self.guard179,self.act179))
        self.__names['''update_item(self.p_str[1], price=self.p_int[0]) '''] = ('''update_item(self.p_str[1], price=self.p_int[0]) ''',self.guard179,self.act179)
        self.__actionClass['''update_item(self.p_str[1], price=self.p_int[0]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[1], price=self.p_int[0]) '''] = 180
        self.__okExcepts['''update_item(self.p_str[1], price=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], price=self.p_int[1]) ''',self.guard180,self.act180))
        self.__names['''update_item(self.p_str[1], price=self.p_int[1]) '''] = ('''update_item(self.p_str[1], price=self.p_int[1]) ''',self.guard180,self.act180)
        self.__actionClass['''update_item(self.p_str[1], price=self.p_int[1]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[1], price=self.p_int[1]) '''] = 181
        self.__okExcepts['''update_item(self.p_str[1], price=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], price=self.p_int[2]) ''',self.guard181,self.act181))
        self.__names['''update_item(self.p_str[1], price=self.p_int[2]) '''] = ('''update_item(self.p_str[1], price=self.p_int[2]) ''',self.guard181,self.act181)
        self.__actionClass['''update_item(self.p_str[1], price=self.p_int[2]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[1], price=self.p_int[2]) '''] = 182
        self.__okExcepts['''update_item(self.p_str[1], price=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], price=self.p_int[3]) ''',self.guard182,self.act182))
        self.__names['''update_item(self.p_str[1], price=self.p_int[3]) '''] = ('''update_item(self.p_str[1], price=self.p_int[3]) ''',self.guard182,self.act182)
        self.__actionClass['''update_item(self.p_str[1], price=self.p_int[3]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[1], price=self.p_int[3]) '''] = 183
        self.__okExcepts['''update_item(self.p_str[1], price=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[1], price=self.p_int[4]) ''',self.guard183,self.act183))
        self.__names['''update_item(self.p_str[1], price=self.p_int[4]) '''] = ('''update_item(self.p_str[1], price=self.p_int[4]) ''',self.guard183,self.act183)
        self.__actionClass['''update_item(self.p_str[1], price=self.p_int[4]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[1], price=self.p_int[4]) '''] = 184
        self.__okExcepts['''update_item(self.p_str[1], price=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], price=self.p_int[0]) ''',self.guard184,self.act184))
        self.__names['''update_item(self.p_str[2], price=self.p_int[0]) '''] = ('''update_item(self.p_str[2], price=self.p_int[0]) ''',self.guard184,self.act184)
        self.__actionClass['''update_item(self.p_str[2], price=self.p_int[0]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[2], price=self.p_int[0]) '''] = 185
        self.__okExcepts['''update_item(self.p_str[2], price=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], price=self.p_int[1]) ''',self.guard185,self.act185))
        self.__names['''update_item(self.p_str[2], price=self.p_int[1]) '''] = ('''update_item(self.p_str[2], price=self.p_int[1]) ''',self.guard185,self.act185)
        self.__actionClass['''update_item(self.p_str[2], price=self.p_int[1]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[2], price=self.p_int[1]) '''] = 186
        self.__okExcepts['''update_item(self.p_str[2], price=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], price=self.p_int[2]) ''',self.guard186,self.act186))
        self.__names['''update_item(self.p_str[2], price=self.p_int[2]) '''] = ('''update_item(self.p_str[2], price=self.p_int[2]) ''',self.guard186,self.act186)
        self.__actionClass['''update_item(self.p_str[2], price=self.p_int[2]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[2], price=self.p_int[2]) '''] = 187
        self.__okExcepts['''update_item(self.p_str[2], price=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], price=self.p_int[3]) ''',self.guard187,self.act187))
        self.__names['''update_item(self.p_str[2], price=self.p_int[3]) '''] = ('''update_item(self.p_str[2], price=self.p_int[3]) ''',self.guard187,self.act187)
        self.__actionClass['''update_item(self.p_str[2], price=self.p_int[3]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[2], price=self.p_int[3]) '''] = 188
        self.__okExcepts['''update_item(self.p_str[2], price=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[2], price=self.p_int[4]) ''',self.guard188,self.act188))
        self.__names['''update_item(self.p_str[2], price=self.p_int[4]) '''] = ('''update_item(self.p_str[2], price=self.p_int[4]) ''',self.guard188,self.act188)
        self.__actionClass['''update_item(self.p_str[2], price=self.p_int[4]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[2], price=self.p_int[4]) '''] = 189
        self.__okExcepts['''update_item(self.p_str[2], price=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], price=self.p_int[0]) ''',self.guard189,self.act189))
        self.__names['''update_item(self.p_str[3], price=self.p_int[0]) '''] = ('''update_item(self.p_str[3], price=self.p_int[0]) ''',self.guard189,self.act189)
        self.__actionClass['''update_item(self.p_str[3], price=self.p_int[0]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[3], price=self.p_int[0]) '''] = 190
        self.__okExcepts['''update_item(self.p_str[3], price=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], price=self.p_int[1]) ''',self.guard190,self.act190))
        self.__names['''update_item(self.p_str[3], price=self.p_int[1]) '''] = ('''update_item(self.p_str[3], price=self.p_int[1]) ''',self.guard190,self.act190)
        self.__actionClass['''update_item(self.p_str[3], price=self.p_int[1]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[3], price=self.p_int[1]) '''] = 191
        self.__okExcepts['''update_item(self.p_str[3], price=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], price=self.p_int[2]) ''',self.guard191,self.act191))
        self.__names['''update_item(self.p_str[3], price=self.p_int[2]) '''] = ('''update_item(self.p_str[3], price=self.p_int[2]) ''',self.guard191,self.act191)
        self.__actionClass['''update_item(self.p_str[3], price=self.p_int[2]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[3], price=self.p_int[2]) '''] = 192
        self.__okExcepts['''update_item(self.p_str[3], price=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], price=self.p_int[3]) ''',self.guard192,self.act192))
        self.__names['''update_item(self.p_str[3], price=self.p_int[3]) '''] = ('''update_item(self.p_str[3], price=self.p_int[3]) ''',self.guard192,self.act192)
        self.__actionClass['''update_item(self.p_str[3], price=self.p_int[3]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[3], price=self.p_int[3]) '''] = 193
        self.__okExcepts['''update_item(self.p_str[3], price=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[3], price=self.p_int[4]) ''',self.guard193,self.act193))
        self.__names['''update_item(self.p_str[3], price=self.p_int[4]) '''] = ('''update_item(self.p_str[3], price=self.p_int[4]) ''',self.guard193,self.act193)
        self.__actionClass['''update_item(self.p_str[3], price=self.p_int[4]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[3], price=self.p_int[4]) '''] = 194
        self.__okExcepts['''update_item(self.p_str[3], price=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], price=self.p_int[0]) ''',self.guard194,self.act194))
        self.__names['''update_item(self.p_str[4], price=self.p_int[0]) '''] = ('''update_item(self.p_str[4], price=self.p_int[0]) ''',self.guard194,self.act194)
        self.__actionClass['''update_item(self.p_str[4], price=self.p_int[0]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[4], price=self.p_int[0]) '''] = 195
        self.__okExcepts['''update_item(self.p_str[4], price=self.p_int[0]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], price=self.p_int[1]) ''',self.guard195,self.act195))
        self.__names['''update_item(self.p_str[4], price=self.p_int[1]) '''] = ('''update_item(self.p_str[4], price=self.p_int[1]) ''',self.guard195,self.act195)
        self.__actionClass['''update_item(self.p_str[4], price=self.p_int[1]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[4], price=self.p_int[1]) '''] = 196
        self.__okExcepts['''update_item(self.p_str[4], price=self.p_int[1]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], price=self.p_int[2]) ''',self.guard196,self.act196))
        self.__names['''update_item(self.p_str[4], price=self.p_int[2]) '''] = ('''update_item(self.p_str[4], price=self.p_int[2]) ''',self.guard196,self.act196)
        self.__actionClass['''update_item(self.p_str[4], price=self.p_int[2]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[4], price=self.p_int[2]) '''] = 197
        self.__okExcepts['''update_item(self.p_str[4], price=self.p_int[2]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], price=self.p_int[3]) ''',self.guard197,self.act197))
        self.__names['''update_item(self.p_str[4], price=self.p_int[3]) '''] = ('''update_item(self.p_str[4], price=self.p_int[3]) ''',self.guard197,self.act197)
        self.__actionClass['''update_item(self.p_str[4], price=self.p_int[3]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[4], price=self.p_int[3]) '''] = 198
        self.__okExcepts['''update_item(self.p_str[4], price=self.p_int[3]) '''] = ''''''
        
        self.__actions.append(('''update_item(self.p_str[4], price=self.p_int[4]) ''',self.guard198,self.act198))
        self.__names['''update_item(self.p_str[4], price=self.p_int[4]) '''] = ('''update_item(self.p_str[4], price=self.p_int[4]) ''',self.guard198,self.act198)
        self.__actionClass['''update_item(self.p_str[4], price=self.p_int[4]) '''] = '''update_item(<str>, price=<int>) '''
        self.__orderings['''update_item(self.p_str[4], price=self.p_int[4]) '''] = 199
        self.__okExcepts['''update_item(self.p_str[4], price=self.p_int[4]) '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard199,self.act199))
        self.__names['''%action% '''] = ('''%action% ''',self.guard199,self.act199)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 200
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''choice = {0..4} ''',self.guard200,self.act200))
        self.__names['''choice = {0..4} '''] = ('''choice = {0..4} ''',self.guard200,self.act200)
        self.__actionClass['''choice = {0..4} '''] = '''choice := {0..4} '''
        self.__orderings['''choice = {0..4} '''] = 201
        self.__okExcepts['''choice = {0..4} '''] = ''''''
        
        self.__actions.append(('''delete_item(self.p_str[0]) ''',self.guard201,self.act201))
        self.__names['''delete_item(self.p_str[0]) '''] = ('''delete_item(self.p_str[0]) ''',self.guard201,self.act201)
        self.__actionClass['''delete_item(self.p_str[0]) '''] = '''delete_item(<str>) '''
        self.__orderings['''delete_item(self.p_str[0]) '''] = 202
        self.__okExcepts['''delete_item(self.p_str[0]) '''] = ''''''
        
        self.__actions.append(('''delete_item(self.p_str[1]) ''',self.guard202,self.act202))
        self.__names['''delete_item(self.p_str[1]) '''] = ('''delete_item(self.p_str[1]) ''',self.guard202,self.act202)
        self.__actionClass['''delete_item(self.p_str[1]) '''] = '''delete_item(<str>) '''
        self.__orderings['''delete_item(self.p_str[1]) '''] = 203
        self.__okExcepts['''delete_item(self.p_str[1]) '''] = ''''''
        
        self.__actions.append(('''delete_item(self.p_str[2]) ''',self.guard203,self.act203))
        self.__names['''delete_item(self.p_str[2]) '''] = ('''delete_item(self.p_str[2]) ''',self.guard203,self.act203)
        self.__actionClass['''delete_item(self.p_str[2]) '''] = '''delete_item(<str>) '''
        self.__orderings['''delete_item(self.p_str[2]) '''] = 204
        self.__okExcepts['''delete_item(self.p_str[2]) '''] = ''''''
        
        self.__actions.append(('''delete_item(self.p_str[3]) ''',self.guard204,self.act204))
        self.__names['''delete_item(self.p_str[3]) '''] = ('''delete_item(self.p_str[3]) ''',self.guard204,self.act204)
        self.__actionClass['''delete_item(self.p_str[3]) '''] = '''delete_item(<str>) '''
        self.__orderings['''delete_item(self.p_str[3]) '''] = 205
        self.__okExcepts['''delete_item(self.p_str[3]) '''] = ''''''
        
        self.__actions.append(('''delete_item(self.p_str[4]) ''',self.guard205,self.act205))
        self.__names['''delete_item(self.p_str[4]) '''] = ('''delete_item(self.p_str[4]) ''',self.guard205,self.act205)
        self.__actionClass['''delete_item(self.p_str[4]) '''] = '''delete_item(<str>) '''
        self.__orderings['''delete_item(self.p_str[4]) '''] = 206
        self.__okExcepts['''delete_item(self.p_str[4]) '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard206,self.act206))
        self.__names['''%action% '''] = ('''%action% ''',self.guard206,self.act206)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 207
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''item = get_item(self.p_str[0]) ''',self.guard207,self.act207))
        self.__names['''item = get_item(self.p_str[0]) '''] = ('''item = get_item(self.p_str[0]) ''',self.guard207,self.act207)
        self.__actionClass['''item = get_item(self.p_str[0]) '''] = '''item := get_item(<str>) '''
        self.__orderings['''item = get_item(self.p_str[0]) '''] = 208
        self.__okExcepts['''item = get_item(self.p_str[0]) '''] = ''''''
        
        self.__actions.append(('''item = get_item(self.p_str[1]) ''',self.guard208,self.act208))
        self.__names['''item = get_item(self.p_str[1]) '''] = ('''item = get_item(self.p_str[1]) ''',self.guard208,self.act208)
        self.__actionClass['''item = get_item(self.p_str[1]) '''] = '''item := get_item(<str>) '''
        self.__orderings['''item = get_item(self.p_str[1]) '''] = 209
        self.__okExcepts['''item = get_item(self.p_str[1]) '''] = ''''''
        
        self.__actions.append(('''item = get_item(self.p_str[2]) ''',self.guard209,self.act209))
        self.__names['''item = get_item(self.p_str[2]) '''] = ('''item = get_item(self.p_str[2]) ''',self.guard209,self.act209)
        self.__actionClass['''item = get_item(self.p_str[2]) '''] = '''item := get_item(<str>) '''
        self.__orderings['''item = get_item(self.p_str[2]) '''] = 210
        self.__okExcepts['''item = get_item(self.p_str[2]) '''] = ''''''
        
        self.__actions.append(('''item = get_item(self.p_str[3]) ''',self.guard210,self.act210))
        self.__names['''item = get_item(self.p_str[3]) '''] = ('''item = get_item(self.p_str[3]) ''',self.guard210,self.act210)
        self.__actionClass['''item = get_item(self.p_str[3]) '''] = '''item := get_item(<str>) '''
        self.__orderings['''item = get_item(self.p_str[3]) '''] = 211
        self.__okExcepts['''item = get_item(self.p_str[3]) '''] = ''''''
        
        self.__actions.append(('''item = get_item(self.p_str[4]) ''',self.guard211,self.act211))
        self.__names['''item = get_item(self.p_str[4]) '''] = ('''item = get_item(self.p_str[4]) ''',self.guard211,self.act211)
        self.__actionClass['''item = get_item(self.p_str[4]) '''] = '''item := get_item(<str>) '''
        self.__orderings['''item = get_item(self.p_str[4]) '''] = 212
        self.__okExcepts['''item = get_item(self.p_str[4]) '''] = ''''''
        
        self.__actions.append(('''%action% ''',self.guard212,self.act212))
        self.__names['''%action% '''] = ('''%action% ''',self.guard212,self.act212)
        self.__actionClass['''%action% '''] = '''<action> '''
        self.__orderings['''%action% '''] = 213
        self.__okExcepts['''%action% '''] = ''''''
        
        self.__actions.append(('''items = get_items() ''',self.guard213,self.act213))
        self.__names['''items = get_items() '''] = ('''items = get_items() ''',self.guard213,self.act213)
        self.__actionClass['''items = get_items() '''] = '''items := get_items() '''
        self.__orderings['''items = get_items() '''] = 214
        self.__okExcepts['''items = get_items() '''] = ''''''
        self.__actions_backup = list(self.__actions)
        self.__actions_assume_backup = list(self.__actions)
    def slowPoolStates(self):
        nonePools = []
        notUsedPools = []
        if self.p_str[0] is None: nonePools.append('''self.p_str[0]''')
        if not self.p_str_used[0]: notUsedPools.append('''self.p_str[0]''')
        if self.p_str[1] is None: nonePools.append('''self.p_str[1]''')
        if not self.p_str_used[1]: notUsedPools.append('''self.p_str[1]''')
        if self.p_str[2] is None: nonePools.append('''self.p_str[2]''')
        if not self.p_str_used[2]: notUsedPools.append('''self.p_str[2]''')
        if self.p_str[3] is None: nonePools.append('''self.p_str[3]''')
        if not self.p_str_used[3]: notUsedPools.append('''self.p_str[3]''')
        if self.p_str[4] is None: nonePools.append('''self.p_str[4]''')
        if not self.p_str_used[4]: notUsedPools.append('''self.p_str[4]''')
        if self.p_int[0] is None: nonePools.append('''self.p_int[0]''')
        if not self.p_int_used[0]: notUsedPools.append('''self.p_int[0]''')
        if self.p_int[1] is None: nonePools.append('''self.p_int[1]''')
        if not self.p_int_used[1]: notUsedPools.append('''self.p_int[1]''')
        if self.p_int[2] is None: nonePools.append('''self.p_int[2]''')
        if not self.p_int_used[2]: notUsedPools.append('''self.p_int[2]''')
        if self.p_int[3] is None: nonePools.append('''self.p_int[3]''')
        if not self.p_int_used[3]: notUsedPools.append('''self.p_int[3]''')
        if self.p_int[4] is None: nonePools.append('''self.p_int[4]''')
        if not self.p_int_used[4]: notUsedPools.append('''self.p_int[4]''')
        if self.p_item[0] is None: nonePools.append('''self.p_item[0]''')
        if not self.p_item_used[0]: notUsedPools.append('''self.p_item[0]''')
        if self.p_item[1] is None: nonePools.append('''self.p_item[1]''')
        if not self.p_item_used[1]: notUsedPools.append('''self.p_item[1]''')
        if self.p_item[2] is None: nonePools.append('''self.p_item[2]''')
        if not self.p_item_used[2]: notUsedPools.append('''self.p_item[2]''')
        if self.p_category[0] is None: nonePools.append('''self.p_category[0]''')
        if not self.p_category_used[0]: notUsedPools.append('''self.p_category[0]''')
        if self.p_category[1] is None: nonePools.append('''self.p_category[1]''')
        if not self.p_category_used[1]: notUsedPools.append('''self.p_category[1]''')
        return (nonePools, notUsedPools)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
        if self.__collectCov: self.cleanCov()
    # BEGIN RELOAD CODE
    # END RELOAD CODE
        self.__test = []
        self.__failure = None
        self.__warning = None
        self.__raised = None
        self.__refRaised = None
        self.__poolsNone = set([])
        self.__poolsUsed = set([])
        self.__disabledByNone = set([])
        self.__disabledByUsed = set([])
        self.p_str = {}
        self.p_str_used = {}
        self.p_str[0] = None
        self.p_str_used[0] = True
        self.p_str[1] = None
        self.p_str_used[1] = True
        self.p_str[2] = None
        self.p_str_used[2] = True
        self.p_str[3] = None
        self.p_str_used[3] = True
        self.p_str[4] = None
        self.p_str_used[4] = True
        self.p_int = {}
        self.p_int_used = {}
        self.p_int[0] = None
        self.p_int_used[0] = True
        self.p_int[1] = None
        self.p_int_used[1] = True
        self.p_int[2] = None
        self.p_int_used[2] = True
        self.p_int[3] = None
        self.p_int_used[3] = True
        self.p_int[4] = None
        self.p_int_used[4] = True
        self.p_item = {}
        self.p_item_used = {}
        self.p_item[0] = None
        self.p_item_used[0] = True
        self.p_item[1] = None
        self.p_item_used[1] = True
        self.p_item[2] = None
        self.p_item_used[2] = True
        self.p_category = {}
        self.p_category_used = {}
        self.p_category[0] = None
        self.p_category_used[0] = True
        self.p_category[1] = None
        self.p_category_used[1] = True
        if self.__useCould: self.computeInitialEnabled()
        try:
            test_after_restart(self)
        except:
            pass
    def hints(self):
        return []
    def log(self, name):
        pass
    def logPost(self, name):
        pass
    def state(self):
        if self.__replayBacktrack:
            return self.captureReplay(self.__test)
        st = []
        try: st.append(copy.deepcopy(self.p_str))
        except: st.append("UNABLE TO COPY")
        st.append(copy.deepcopy(self.p_str_used))
        try: st.append(copy.deepcopy(self.p_int))
        except: st.append("UNABLE TO COPY")
        st.append(copy.deepcopy(self.p_int_used))
        try: st.append(copy.deepcopy(self.p_item))
        except: st.append("UNABLE TO COPY")
        st.append(copy.deepcopy(self.p_item_used))
        try: st.append(copy.deepcopy(self.p_category))
        except: st.append("UNABLE TO COPY")
        st.append(copy.deepcopy(self.p_category_used))
        st.append(copy.copy(self.__test))
        return st
    def shallowState(self):
        return [ ("self.p_str",self.p_str),("self.p_int",self.p_int),("self.p_item",self.p_item),("self.p_category",self.p_category)]
    def abstract(self,state):
        if self.__replayBacktrack:
            return state
        return ( state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7])
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_str = copy.deepcopy(old[0])
        self.p_str_used = copy.deepcopy(old[1])
        self.p_int = copy.deepcopy(old[2])
        self.p_int_used = copy.deepcopy(old[3])
        self.p_item = copy.deepcopy(old[4])
        self.p_item_used = copy.deepcopy(old[5])
        self.p_category = copy.deepcopy(old[6])
        self.p_category_used = copy.deepcopy(old[7])
        self.__test = copy.copy(old[-1])
    def check(self):
        try:
            if self.__collectCov:
                self.__cov.start()
            # BEGIN CHECK CODE
            # GLOBAL self.p_str[0]
            if (self.p_str[0] is not None): # CHECK POOL INIT
                assert all(item.name in [self.p_str[0]] for item in get_items())
            # GLOBAL self.p_str[1]
            if (self.p_str[1] is not None): # CHECK POOL INIT
                assert all(item.name in [self.p_str[1]] for item in get_items())
            # GLOBAL self.p_str[2]
            if (self.p_str[2] is not None): # CHECK POOL INIT
                assert all(item.name in [self.p_str[2]] for item in get_items())
            # GLOBAL self.p_str[3]
            if (self.p_str[3] is not None): # CHECK POOL INIT
                assert all(item.name in [self.p_str[3]] for item in get_items())
            # GLOBAL self.p_str[4]
            if (self.p_str[4] is not None): # CHECK POOL INIT
                assert all(item.name in [self.p_str[4]] for item in get_items())
            # assert all(category.name in ["Electronics", "Apparel"] for category in get_categories())
            # END CHECK CODE
        except KeyboardInterrupt as e:
            raise e
        except:
            self.__failure = sys.exc_info()
            return False
        finally:
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov(extendCov=True)
        return True
    """
    BOILERPLATE METHODS OF SUT
    ==========================
    These are the set of methods available on each SUT by default
    
    Examples
    --------
    
    t.enabled()
    t.actions()
    """
    
    
    def setReplayBacktrack(self, val):
        self.__replayBacktrack = val
    
    
    def test(self):
        """
        Returns the current test as a sequence of (name, guard, actions)
        """
        return self.__test
    
    
    def SUTName(self):
        return self.__SUTName
    
    
    def raised(self):
        """
        Returns exception raised by last action, or None if no exception was raised
        """
        return self.__raised
    
    
    def refRaised(self):
        """
        Returns exception raised by last reference action, or None if no exception was raised
        """
        return self.__refRaised
    
    
    def getOkExceptions(self, name):
        return self.__okExcepts[name]
    
    
    def getPreCode(self, name):
        try:
            return self.__preCode[name]
        except BaseException:
            return None
    
    
    def getRefCode(self, name):
        try:
            return self.__refCode[name]
        except BaseException:
            return None
    
    
    def getPropCode(self, name):
        try:
            return self.__propCode[name]
        except BaseException:
            return None
    
    
    def actionClass(self, action):
        return self.__actionClass[action[0]]
    
    
    def dependencies(self, actClass):
        return self.__dependencies[actClass]
    
    
    def abstraction(self, pool):
        if pool not in self.__abstraction:
            return None
        return self.__abstraction[pool]
    
    
    def prettyName(self, name):
        newName = name
        for p in self.__pools:
            pfind = newName.find(p + "[")
            while pfind != -1:
                closePos = newName.find("]", pfind)
                index = newName[newName.find("[", pfind) + 1:closePos]
                access = newName[pfind:newName.find("]", pfind) + 1]
                needUnderscore = ""
                if p[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    needUnderscore = "_"
                newAccess = p.replace(self.__poolPrefix, "") + \
                    needUnderscore + index
                newName = newName.replace(access, newAccess)
                pfind = newName.find(p + "[")
        return newName
    
    
    def actOrder(self, action):
        return self.__orderings[action[0]]
    
    
    def pools(self):
        return self.__pools
    
    
    def prettyPrintTest(self, test, columns=80):
        i = 0
        for a in test:
            s = a[0]
            steps = "# STEP " + str(i)
            if len(a) > 3:  # NOW ALLOW ANNOTATIONS!
                steps += "  ;;; " + a[3]
            print(self.prettyName(s).ljust(columns - len(steps), ' '), steps)
            i += 1
    
    
    def prettyPrintRemoved(self, test1, test2, columns=80):
        # Assumption is that test2 is test1 with parts removed!
        i = 0
        j = 0
        for a in test1:
            s = a[0]
            if i < len(test2):
                sdiff = test2[i][0]
            else:
                sdiff = None
            if s != sdiff:
                steps = ""
                if len(a) > 3:  # NOW ALLOW ANNOTATIONS!
                    steps += "  ;;; " + a[3]
                print(self.prettyName(s).ljust(columns - len(steps), ' '), steps)
                j += 1
            else:
                i += 1
                j = i
    
    
    def exploreFromHere(self, depth, checkProp=True, stopFail=True, stopCover=False,
                        gatherFail=None, gatherCover=None, verbose=False, reverse=False,
                        visited=None):
        """
        Does a DFS complete exploration.  Recursive, so limited depth, but deep runs
        unlikely to be useful, anyway.
        """
        state = self.state()
    
        if visited is not None:
            if type(visited) == list:
                if state[:-1] in visited:
                    if verbose == "BACKTRACK":
                        print("BACKTRACKING DUE TO ALREADY VISITED STATE:",
                              state[:-1])
                    return True
                else:
                    visited.append(state[:-1])
            elif type(visited) == dict:
                rs = repr(state[:-1])
                if rs in visited:
                    if verbose == "BACKTRACK":
                        print("BACKTRACKING DUE TO ALREADY VISITED STATE",
                              rs)
                    return True
                else:
                    visited[rs] = True
    
        acts = self.enabled()
        if reverse:
            # More interesting actions tend to be later in order
            acts.reverse()
    
        for a in acts:
            if verbose == "STEPS":
                print(depth, a[0])
            ok = self.safely(a)
            if not ok:
                if stopFail:
                    if verbose:
                        print("TEST FAILED!")
                    return False
                elif gatherFail is not None:
                    if verbose:
                        print("NEW FAILING TEST OF LENGTH", len(self.test()))
                        f = self.failure()
                        print("FAILURE ON ACTION:", self.prettyName(a[0]))
                        print("ERROR:", f)
                        traceback.print_tb(f[2], file=sys.stdout)
                    gatherFail.append(list(self.test()))
            if checkProp:
                if not self.check():
                    if stopFail:
                        if verbose:
                            print("PROPERTY CHECK FAILED!")
                        return False
                    elif gatherFail is not None:
                        if verbose:
                            print("NEW FAILING TEST OF LENGTH", len(self.test()))
                        f = self.failure()
                        print("FAILED PROPERTY CHECK ON ACTION:", self.prettyName(a[0]))
                        print("ERROR:", f)
                        traceback.print_tb(f[2], file=sys.stdout)
                        gatherFail.append(list(self.test()))
            if (len(self.newBranches()) > 0) or (len(self.newStatements()) > 0):
                if stopCover:
                    return False
                elif gatherCover is not None:
                    if verbose:
                        print("COLLECTED TEST WITH NEW COVERAGE FROM ACTION",
                              self.prettyName(a[0]))
                        print("ADDED", len(self.newBranches()), "BRANCHES AND",
                              len(self.newStatements()), "STATEMENTS")
                    gatherCover.append(list(self.test()))
            if depth > 1:
                r = self.exploreFromHere(depth - 1, checkProp, stopFail, stopCover,
                                         gatherFail, gatherCover, verbose, reverse,
                                         visited)
                if not r:
                    return r
            try:
                self.backtrack(state)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                print("WARNING: FAILURE IN INITIAL EXPLORATION PATH")
        return True
    
    
    def getPoolStates(self):
        if self.__useCould and not self.__actionCould:
            return (self.__poolsNone, self.__poolsUsed)
        else:
            return self.slowPoolStates()
    
    
    def setUseDependencies(self, value):
        self.__useCould = value
    
    
    def setActionApproximation(self, value):
        self.__actionCould = value
    
    
    def setFastPoolStates(self, value):
        self.__fastPoolStates = value
    
    
    def captureReplay(self, test):
        captured = ""
        for step in test:
            captured += self.serializable(step)
            captured += "#!#!"
        return captured[:-4]
    
    
    def replayable(self, stest):
        steps = stest.split("#!#!")
        if steps == ['']:
            return []
        return list(map(self.playable, steps))
    
    
    def enabled(self):
        """
        Returns all enabled action objects.
        """
        if self.__useCould:
            acts = self.couldBeEnabled()
        else:
            acts = self.__actions
        return [s_g_a1 for s_g_a1 in acts if s_g_a1[1]()]
    
    
    def couldBeEnabled(self):
        couldBe = set(map(lambda x: x[0], self.__actions))
        if self.__actionCould:
            if self.verboseActionCould:
                print("couldBe:", len(couldBe))
                print("NONE:", len(self.__disabledByNone))
                print("USED:", len(self.__disabledByUsed))
            couldBe -= self.__disabledByNone
            couldBe -= self.__disabledByUsed
            if self.verboseActionCould:
                print("couldBe:", len(couldBe))
        else:
            pNone, pNotUsed = self.getPoolStates()
            for p in pNone:
                if p in self.__poolUsers:
                    for a in self.__poolUsers[p]:
                        couldBe.discard(a)
            if self.__relaxUsedRestriction:
                return map(lambda x: self.__names[x], couldBe)
            for p in pNotUsed:
                if p in self.__poolInitializers:
                    for a in self.__poolInitializers[p]:
                        if p not in pNone:
                            couldBe.discard(a)
        return map(lambda x: self.__names[x], couldBe)
    
    
    def nowUsed(self, pool):
        if self.__actionCould:
            if pool in self.__poolInitializers:
                for a in self.__poolInitializers[pool]:
                    if self.verboseActionCould:
                        print("ENABLING", a, "DUE TO NOW USED POOL", pool)
                    self.__disabledByUsed.discard(a)
        else:
            self.__poolsUsed.add(pool)
    
    
    def noLongerNone(self, pool):
        if self.__actionCould:
            if pool in self.__poolUsers:
                for a in self.__poolUsers[pool]:
                    if self.verboseActionCould:
                        print("ENABLING", a, "DUE TO ASSIGNING TO POOL", pool)
                        print("IN DISABLED BY USED POOL?", a in self.__disabledByUsed)
                        print("OLD LENGTH", len(self.__disabledByNone))
                    self.__disabledByNone.discard(a)
                    if self.verboseActionCould:
                        print("NEW LENGTH", len(self.__disabledByNone))
        else:
            self.__poolsNone.discard(pool)
    
    
    def noLongerUsed(self, pool):
        if self.__actionCould:
            if pool in self.__poolInitializers:
                for a in self.__poolInitializers[pool]:
                    if self.verboseActionCould:
                        print("DISABLING", a, "DUE TO NO LONGER USED POOL", pool)
                    self.__disabledByUsed.add(a)
        else:
            self.__poolsUsed.discard(pool)
    
    
    def computeInitialEnabled(self):
        pNone, pNotUsed = self.slowPoolStates()
        for p in pNone:
            if self.__actionCould:
                if p in self.__poolUsers:
                    for a in self.__poolUsers[p]:
                        self.__disabledByNone.add(a)
            else:
                self.__poolsNone.add(p)
    
    
    def highLowSwarm(self, rgen, P=0.5, file=None, highProb=0.9, noDependencies=False, forceParent=True):
        high = []
    
        if file is not None:
            classProb = {}
            for l in open(file):
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
    
        for c in self.__actionClasses:
            if file is None:
                if rgen.random() < P:
                    high.append(c)
            else:
                if rgen.random() < classProb[c]:
                    high.append(c)
        if high == []:
            high.append(rgen.choice(self.__actionClasses))
    
        changed = True
        if noDependencies:
            changed = False
    
        while changed:
            changed = False
    
            if forceParent:
                forcedAdd = []
                for c in newEnabled:
                    allParents = []
                    for pp in self.__actionClasses:
                        for dl in self.dependencies(pp):
                            if c in dl:
                                allParents.append(pp)
                                break
                    if allParents == []:
                        continue
                    anyParents = [x for x in newEnabled if x in allParents]
                    anyParents.extend([x for x in forcedAdd if x in allParents])
                    if anyParents == []:
                        addC = rgen.choice(allParents)
                        forcedAdd.append(addC)
                        changed = True
                newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in high:
                for d in self.dependencies(c):
                    df = [x for x in high if x in d] + \
                        [x for x in forcedAdd if x in d]
                    if df == []:
                        forcedAdd.append(rgen.choice(d))
                        changed = True
            high.extend(forcedAdd)
    
            forcedAdd = []
            for c in high:
                if self.dependencies(c) == []:
                    anyDepend = False
                    for c2 in (high + forcedAdd):
                        for d in self.dependencies(c2):
                            if c in d:
                                anyDepend = True
                                break
                        if anyDepend:
                            break
                    if not anyDepend:
                        needsThis = []
                        for c2 in self.__actionClasses:
                            for d in self.dependencies(c2):
                                if c in d:
                                    needsThis.append(c2)
                                    break
                        if needsThis != []:
                            forcedAdd.append(rgen.choice(needsThis))
                            changed = True
            high.extend(forcedAdd)
        low = [x for x in self.__actionClasses if x not in high]
        probs = []
        if low == []:
            return [(1.0 / len(high), x) for x in high]
        if high == []:
            return [(1.0 / len(low), x) for x in low]
        highP = highProb / len(high)
        lowP = (1.0 - highProb) / len(low)
        for c in high:
            probs.append((highP, c))
        for c in low:
            probs.append((lowP, c))
        return probs
    
    
    def highLowClassProbs(self, rgen, P=0.5, file=None, highProb=0.9):
        high = []
        low = []
        if file is not None:
            classProb = {}
            for l in open(file):
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
    
        for c in self.__actionClasses:
            if file is None:
                if rgen.random() < P:
                    high.append(c)
                else:
                    low.append(c)
            else:
                if rgen.random() < classProb[c]:
                    high.append(c)
                else:
                    low.append(c)
        probs = []
        if low == []:
            return [(1.0 / len(high), x) for x in high]
        if high == []:
            return [(1.0 / len(low), x) for x in low]
        highP = highProb / len(high)
        lowP = (1.0 - highProb) / len(low)
        for c in high:
            probs.append((highP, c))
        for c in low:
            probs.append((lowP, c))
        return probs
    
    
    def randomEnabledClassProbs(self, rgen, probs):
        if self.__enumerateEnabled:
            enableds = self.enabled()
        else:
            enableds = None
        a = None
        while a is None:
            r = rgen.random()
            p = 0.0
            ac = None
            for (pac, tac) in probs:
                p += pac
                if p > r:
                    ac = tac
                    break
            a = self.randomEnabled(rgen, actFilter=lambda act: self.actionClass(
                act) == ac, enabledActs=enableds)
            if a is None:
                if len(probs) == 1:
                    return None
                padd = pac / (len(probs) - 1)
                newprobs = []
                for (pac, tac2) in probs:
                    if tac2 == tac:
                        continue
                    newprobs.append((pac + padd, tac2))
                probs = newprobs
                if probs == []:
                    break
        return a
    
    
    def setEnumerateEnabled(self, bval):
        self.__enumerateEnabled = bval
    
    
    def randomEnabled(self, rgen, actFilter=None, enabledActs=None):
        """
        Return a random enabled action, or None if no such action can be
        produced, based on a provided random generator.
        """
        if enabledActs is not None:
            acts = list(enabledActs)
        elif self.__useCould:
            acts = self.couldBeEnabled()
        else:
            acts = self.__actions
        if filter is not None:
            acts = list(filter(actFilter, acts))
        if self.__enumerateEnabled:
            try:
                return rgen.choice([s_g_a for s_g_a in acts if s_g_a[1]()])
            except IndexError:
                return None
        a = None
        while a is None:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                break
            else:
                a = None
            acts = acts[:p] + acts[p + 1:]
        return a
    
    
    def randomEnableds(self, rgen, n):
        """
        Return list of random enabled actions, up to n actions if possible
        """
    
        retActs = []
        acts = self.__actions
        if self.__enumerateEnabled:
            acts = self.enabled()
        while len(retActs) < n:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                retActs.append(a)
            acts = acts[:p] + acts[p + 1:]
        return retActs
    
    
    def randomEnabledPred(self, rgen, n, pred):
        """
        Return first enabled action satisfying pred, with up to n attempts.
        If none found, returns last enabled action checked.
        """
    
        tries = 0
        acts = self.__actions
        if self.__enumerateEnabled:
            acts = self.enabled()
        a = None
        lastSafe = None
        while tries < n:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                lastSafe = a
                if pred(a):
                    return a
                tries += 1
            acts = acts[:p] + acts[p + 1:]
        return lastSafe
    
    
    def mutate(self, test, rgen, Pinsert=0.2):
        '''
        Simple tool for mutating tests randomly.  Does not ensure validity
        of the new test, which may be functionally equivalent.  There are
        two types of mutation, replacement and insertion.  Pinsert gives
        probability of insert (default 0.2).
        '''
        newTest = list(test)
        loc = rgen.randrange(0, len(test))
        act = rgen.choice(self.__actions)
        if rgen.random() < Pinsert:
            newTest.insert(loc, act)
        else:
            newTest[loc] = act
        return newTest
    
    
    def crossover(self, test1, test2, rgen, twoPoint=False):
        '''
        Simple code for performing crossover of two tests.  Just picks an
        order, then picks a point at which to stop first test then start
        second.  twoPoint results in two point crossover.
        '''
        if rgen.randrange(2) == 0:
            t1 = test1
            t2 = test2
        else:
            t2 = test1
            t1 = test2
        if len(t1) > 1:
            p1 = rgen.randrange(1, len(t1))
        else:
            p1 = 1
        if len(t2) > 0:
            p2 = rgen.randrange(0, len(t2))
        else:
            p2 = 0
        newTest = t1[:p1]
        if twoPoint:
            if len(t1) > 1:
                p3 = rgen.randrange(p1, len(t1))
            else:
                p3 = 1
            if len(t2) > 0:
                p4 = rgen.randrange(p2, len(t2))
            else:
                p4 = 0
            newTest.extend(t2[p2:p4])
            newTest.extend(t1[p3:])
        else:
            newTest.extend(t2[p2:])
        return newTest
    
    
    def makeTest(
            self,
            size,
            rgen=None,
            generator=None,
            sgenerator=None,
            stopFail=True,
            checkProp=True,
            initial=None,
            timeout=None,
            stopWhen=None):
        '''
        Allows generation of fixed length tests using either a default
        generator (pure random testing), or using a simple generator that
        only takes the current test step as input (generator) or a complex
        stateful generator (sgenerator).  An sgenerator must take as input
        both a state and an interface to the SUT (to query for coverage,
        etc.) and return an (action, new state) tuple.  User can also
        control whether to stop on failure, whether to check properties,
        and supply a timeout in seconds.
    
        '''
    
        if timeout is not None:
            stime = time.time()
    
        noFailure = True
    
        if generator is not None:
            genF = generator
        else:
            def genF(x): return self.randomEnabled(rgen)
        if sgenerator is not None:
            state = initial
        self.restart()
        for i in range(0, size):
            if stopWhen is not None:
                if stopWhen():
                    return (list(self.test()), noFailure)
            if sgenerator is None:
                action = genF(i)
                if action is None:
                    return (list(self.test()), "DEADLOCK")
                ok = self.safely(action)
            else:
                (action, state) = sgenerator(state, self)
                if action is None:
                    return (list(self.test()), "DEADLOCK")
                ok = self.safely(action)
            if not ok:
                noFailure = False
                if stopFail:
                    return (list(self.test()), False)
            if checkProp:
                if not self.check():
                    noFailure = False
                    if stopFail:
                        return (list(self.test()), False)
            if timeout is not None:
                if (time.time() - stime) > timeout:
                    return (list(self.test()), noFailure)
        return (list(self.test()), noFailure)
    
    
    def features(self):
        return self.__features
    
    
    def actions(self):
        """
        Returns all the action objects whether enabled or disabled.
        """
        return self.__actions
    
    
    def actionClasses(self):
        return self.__actionClasses
    
    
    def essentialClasses(self):
        return self.__essentialClasses
    
    
    def disable(self, f):
        """
        Disable an action by name.
        """
        newActions = []
        for a in self.__actions:
            name = a[0]
            guard = a[1]
            act = a[2]
            if not re.match(f, name):
                newActions.append((name, guard, act))
        self.__actions = newActions
    
    
    def enableAll(self):
        """
        Enable all actions.
        """
        self.__swarmConfig = None
        self.__actions = self.__actions_backup
        self.__actions_assume_backup = list(self.__actions_backup)
    
    
    def enableAllAssume(self):
        """
        Enable all actions, but restricted by current swarm set
        """
        self.__actions = self.__actions_assume_backup
    
    
    def objCodeLOCs(self, obj, context):
        LOCs = []
        for o in inspect.getmembers(obj):
            try:
                if inspect.isfunction(o[1]) or inspect.ismethod(o[1]):
                    if o[0] == "__init__":
                        LOCs.append(
                            (context[-1], len(inspect.getsourcelines(o[1])[0]), context))
                    LOCs.append(
                        (o[0], len(inspect.getsourcelines(o[1])[0]), context))
                if inspect.isclass(o[1]):
                    if o[1] == object:
                        continue
                    if o[1] == type:
                        continue
                    LOCs.extend(self.objCodeLOCs(o[1], context + [o[0]]))
            except BaseException:
                pass
        return LOCs
    
    
    def codeLOCs(self):
        LOCs = []
        for m in self.__importModules:
            LOCs.extend(self.objCodeLOCs(m, [m.__name__]))
        return LOCs
    
    
    def codeLOCProbs(self, baseline=0.2, codeLOCs=None):
        if codeLOCs is None:
            # use static estimation if no dynamic estimates provided
            cl = self.codeLOCs()
        else:
            cl = codeLOCs
    
        totalLOCs = 0.0
        aProbs = []
        num0LOC = 0
    
        for a in self.__actionClasses:
            thisLOC = 0
            for (f, LOC, c) in cl:
                if (("." + f + "(") in a):
                    thisLOC += LOC
            totalLOCs += thisLOC
            if thisLOC == 0:
                num0LOC += 1
            aProbs.append((a, thisLOC))
        P = []
        leftOver = 1.0 - baseline
        for (a, LOC) in aProbs:
            if LOC == 0:
                P.append((baseline / num0LOC, a))
            else:
                P.append(((LOC / totalLOCs) * leftOver, a))
        return P
    
    
    def writeProbFile(self, file, classProb):
        with open(file, 'w') as f:
            for ac in classProb:
                f.write(ac + " %%%% " + str(classProb[ac]) + "\n")
    
    
    def readProbFile(self, file, returnList=False):
        classProb = {}
        with open(file) as f:
            for l in f:
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
        if not returnList:
            return classProb
        pl = []
        for k in classProb:
            pl.append((classProb[k], k))
        return pl
    
    
    def standardSwarm(
            self,
            rgen,
            P=0.5,
            file=None,
            classProb=None,
            noDependencies=False,
            forceParent=True):
        """
        Enables all actions, then sets a swarm configuration based on
        rgen, P = probability of enabling an action class, file is a file
        (format action %%%% probability) giving probabilities for
        inclusion)
        """
        self.enableAll()
        newEnabled = []
    
        if file is not None:
            classProb = self.readProbFile(file)
    
        for c in self.__actionClasses:
            if classProb is None:
                if (c in self.__essentialClasses) or (rgen.random() < P):
                    newEnabled.append(c)
            else:
                if c not in classProb:
                    classProb[c] = P
                if rgen.random() < classProb[c]:
                    newEnabled.append(c)
        if newEnabled == []:
            newEnabled.append(rgen.choice(self.__actionClasses))
    
        changed = True
        if noDependencies:
            changed = False
    
        while changed:
            changed = False
    
            if forceParent:
                forcedAdd = []
                for c in newEnabled:
                    allParents = []
                    for pp in self.__actionClasses:
                        for dl in self.dependencies(pp):
                            if c in dl:
                                allParents.append(pp)
                                break
                    if allParents == []:
                        continue
                    anyParents = [x for x in newEnabled if x in allParents]
                    anyParents.extend([x for x in forcedAdd if x in allParents])
                    if anyParents == []:
                        addC = rgen.choice(allParents)
                        forcedAdd.append(addC)
                        changed = True
                newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in newEnabled:
                for d in self.dependencies(c):
                    df = [x for x in newEnabled if x in d] + \
                        [x for x in forcedAdd if x in d]
                    if df == []:
                        forcedAdd.append(rgen.choice(d))
                        changed = True
            newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in newEnabled:
                if self.dependencies(c) == []:
                    anyDepend = False
                    for c2 in (newEnabled + forcedAdd):
                        for d in self.dependencies(c2):
                            if c in d:
                                anyDepend = True
                                break
                        if anyDepend:
                            break
                    if not anyDepend:
                        needsThis = []
                        for c2 in self.__actionClasses:
                            for d in self.dependencies(c2):
                                if c in d:
                                    needsThis.append(c2)
                                    break
                        if needsThis != []:
                            forcedAdd.append(rgen.choice(needsThis))
                            changed = True
            newEnabled.extend(forcedAdd)
    
        self.__swarmConfig = newEnabled
        enabledActions = []
        for a in self.__actions:
            if self.actionClass(a) in newEnabled:
                enabledActions.append(a)
        self.__actions = enabledActions
        self.__actions_assume_backup = list(self.__actions)
    
    
    def swarmConfig(self):
        return self.__swarmConfig
    
    
    def serializable(self, step):
        ser = step[0]
        if len(step) > 3:
            ser += ";;;" + step[3]
        return ser
    
    
    def annotate(self, text):
        self.__test[-1] = self.__test[-1] + (text,)
    
    
    def testToBytes(self, test):
        alen = len(self.actions())
        bytes = 2
        fmt = "<H"
        if alen < 256:
            bytes = 1
            fmt = "<B"
        if alen > 2**16:
            bytes = 4
            fmt = "<L"
        data = b""
        for s in test:
            index = 0
            for a in self.actions():
                if a == s:
                    break
                index += 1
            p = struct.pack(fmt, index)
            data += p
        return data
    
    
    def saveTest(self, test, filename, afl=False):
        if not afl:
            outf = open(filename, 'w')
        else:
            outf = open(filename, 'wb')
        if not afl:
            for s in test:
                outf.write(self.serializable(s) + "\n")
        else:
            outf.write(self.testToBytes(test))
        outf.close()
    
    
    def bytesToTest(self, data, swarm=False):
        alen = len(self.actions())
        bytes = 2
        fmt = "<H"
        if alen < 256:
            bytes = 1
            fmt = "<B"
        if alen > 2**16:
            bytes = 4
            fmt = "<L"
        test = []
        if swarm:
            R = random.Random()
            seed = struct.unpack("<L", data[0:4])[0]
            R.seed(seed)
            self.standardSwarm(R)
            data = data[4:]
            alen = len(self.actions())
        for i in range(0, (len(data) // bytes)):
            index = struct.unpack(
                fmt, data[i * bytes:(i * bytes) + bytes])[0] % alen
            test.append(self.actions()[index])
        return test
    
    
    def loadTest(self, filename, afl=False, swarm=False):
        if afl:
            with open(filename, 'rb') as f:
                return self.bytesToTest(f.read(), swarm=swarm)
    
        test = []
        with open(filename) as f:
            for l in f:
                test.append(self.playable(l[:-1]))
        return test
    
    
    def playable(self, name):
        if ";;;" in name:
            annotateSplit = name.split(";;;")
            rname = annotateSplit[0]
            return self.__names[rname] + (annotateSplit[1],)
        else:
            return self.__names[name]
    
    
    def setDebugSafelyMode(self, mode):
        self.__safeSafelyMode = mode
    
    
    def safely(self, act):
        if self.__safeSafelyMode:
            if not act[1]():
                print("WARNING:  ATTEMPED TO EXECUTE NON-ENABLED ACTION")
                return False
        try:
            act[2]()
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            self.__failure = sys.exc_info()
            return False
        finally:
            if len(act) > 3:
                self.annotate(act[3])
        return True
    
    
    def failure(self):
        return self.__failure
    
    
    def warning(self):
        return self.__warning
    
    
    def allEnabled(self, test):
        for a in test:
            name = a[0]
            guard = a[1]
            act = a[2]
            if not guard():
                return False
            self.safely((name, guard, act))
        return True
    
    
    def replay(
            self,
            test,
            catchUncaught=False,
            extend=False,
            checkProp=False,
            verbose=False,
            stopFail=True,
            returnCov=False,
            delay=None):
        '''
        Replays a test, either resetting first or extending current test
        (default is to restart).  Can either stop or keep going on
        failure, catch and notify about uncaught exceptions or throw them,
        and check or not check properties.  The returnCov setting adds a
        sequential record of coverage by step as another element of a
        return tuple.
        '''
        if not extend:
            self.restart()
        if returnCov:
            allS = set([])
            allB = set([])
            cov = []
        for a in test:
            name = a[0]
            if name == "<<RESTART>>":
                self.restart()
            guard = a[1]
            act = a[2]
            if verbose:
                print(name)
            if guard():
                if verbose:
                    print("EXECUTING")
                try:
                    act()
                except KeyboardInterrupt as e:
                    raise e
                except Exception as e:
                    self.__failure = sys.exc_info()
                    if catchUncaught:
                        if stopFail:
                            return False
                    else:
                        raise e
                if checkProp:
                    if (not self.check()) and stopFail:
                        return False
                if delay is not None:
                    time.sleep(delay)
            if returnCov:
                s = set(self.currStatements())
                b = set(self.currBranches())
                newS = s - allS
                newB = b - allB
                if (len(newS) > 0) or (len(newB) > 0):
                    cov.append((newS, newB))
                allS.update(s)
                allB.update(b)
        if returnCov:
            return (self.__failure is None, cov)
        return (self.__failure is None)
    
    
    def replayUntil(
            self,
            test,
            pred,
            catchUncaught=False,
            checkProp=False,
            stopFail=True):
        self.restart()
        newt = []
        if pred():
            return newt
    
        for a in test:
            name = a[0]
            guard = a[1]
            act = a[2]
    
            newt.append((name, guard, act))
            if guard():
                if catchUncaught:
                    try:
                        act()
                    except KeyboardInterrupt as e:
                        raise e
                    except BaseException:
                        self.__failure = sys.exc_info()
                        if stopFail:
                            return False
                        pass
                else:
                    act()
            if pred():
                return newt
            if checkProp:
                if not self.check():
                    return False
        return None
    
    
    def eqFail(self, f1, f2):
        if (f1[0] != f2[0]) or (repr(f1[1]) != repr(f2[1])):
            return False
        if f1[0] != AssertionError:
            return True
        # For assertions, require equal line nos.
        return ((f1[2].tb_lineno == f2[2].tb_lineno) and
                ((f1[2].tb_frame.f_code.co_filename) == (f2[2].tb_frame.f_code.co_filename)))
    
    
    def failsCheck(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, catchUncaught=True,
                            checkProp=True, verbose=verbose)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            if (failure is None) or self.eqFail(self.__failure, failure):
                return True
            else:
                return False
        if r is True:
            return False
        if (failure is None) or self.eqFail(self.__failure, failure):
            return True
        else:
            return False
    
    
    def fails(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, verbose=verbose, catchUncaught=True)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            if verbose:
                print("Got exception during replay!")
            if failure is None:
                return True
            if (self.__failure is not None) and self.eqFail(self.__failure, failure):
                return True
            else:
                return False
        if r is True:
            return False
        if (failure is None) or self.eqFail(self.__failure, failure):
            return True
        else:
            return False
    
    
    def failsAny(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, checkProp=True,
                            verbose=verbose, catchUncaught=True)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            self.__failure = sys.exc_info()
            if (failure is None) or ((self.__failure[0] == failure[0]) and (
                    repr(self.__failure[1]) == repr(failure[1]))):
                return True
            return False
        if r is False:
            # self.__failure = sys.exc_info()
            if (failure is None) or ((self.__failure[0] == failure[0]) and (
                    repr(self.__failure[1]) == repr(failure[1]))):
                return True
            return False
        return False
    
    
    def P(self, t, pred, samples=10):
        success = 0.0
        for i in range(0, samples):
            if pred(t):
                success += 1.0
        return (success / samples)
    
    
    def forceP(self, t, pred, P=0.5, samples=10, replications=1):
        while (replications > 0):
            success = 0.0
            for i in range(0, samples):
                if pred(t):
                    success += 1.0
            replications -= 1
            if replications == 0:
                return (success / samples) >= P
            elif (success / samples) < P:
                return False
    
    
    def findProcessNondeterminism(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            delay=None,
            tries=1):
        for j in range(0, tries):
            try:
                self.saveTest(t, ".tmp.test")
                cmd = ["tstl_replay", ".tmp.test", "--hideOpaque", "--verbose"]
                if delay is not None:
                    cmd.extend(["--delay", str(delay)])
                out1 = subprocess.check_output(cmd, universal_newlines=True)
                out2 = subprocess.check_output(cmd, universal_newlines=True)
            finally:
                os.remove(".tmp.test")
            out1l = out1.split("\n")
            out2l = out2.split("\n")
            if ignoreExceptions:
                removeExceptions = (lambda l: "RAISED".find(l) != 0)
                out1l = list(filter(removeExceptions, out1l))
                out2l = list(filter(removeExceptions, out2l))
            if (out1l != out2l):
                action = -1
                for i in range(0, min(len(out1l), len(out2l))):
                    if out1l[i].find("STEP") == 0:
                        action = int(out1l[i].split(":")[0].split("#")[1]) + 1
                    if out1l[i] != out2l[i]:
                        if verbose:
                            print("=" * 50)
                            print("DIFFERENCE FOUND AT STEP", action)
                            print(out1l[i])
                            print("  VS.")
                            print(out2l[i])
                            print("=" * 50)
                        break
                return action
            else:
                if verbose:
                    print("NO DIFFERENCES IN OUTPUT FILES")
        return -1
    
    
    def iterateFindProcessNondeterminism(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            double=False,
            delay=None,
            tries=1):
        i = 1
        if verbose:
            print("TRYING WITH LENGTH:", i)
        p = self.findProcessNondeterminism(
            t[:i], ignoreExceptions, verbose, delay, tries)
        while (p == -1) and (i < len(t)):
            if not double:
                i += 1
            else:
                i *= 2
                if (i > len(t)):
                    i = len(t)
            if verbose:
                print("TRYING WITH LENGTH:", i)
            p = self.findProcessNondeterminism(
                t[:i], ignoreExceptions, verbose, delay, tries)
        return p
    
    
    def processNondeterministic(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            iterate=False,
            double=True,
            delay=None,
            tries=1):
        for i in range(0, tries):
            if not iterate:
                nd = (self.findProcessNondeterminism(
                    t, ignoreExceptions, verbose, delay) != -1)
            else:
                nd = (self.iterateFindProcessNondeterminism(
                    t, ignoreExceptions, verbose, double, delay) != -1)
            if nd:
                return True
        return False
    
    
    def trajectoryItem(self, pools=None):
        ss = self.shallowState()
        o = set(self.opaque())
        if pools is not None:
            for p in self.pools():
                if p not in pools:
                    o.add(p)
        ti = {}
        for (name, vals) in ss:
            if name in o:
                continue
            if name.replace(
                "_REF",
                    "") in o:  # Assume if pool is opaque, so is reference
                continue
            ti[name] = {}
            for v in vals:
                try:
                    ti[name][v] = copy.deepcopy(vals[v])
                except BaseException:
                    ti[name][v] = "UNABLE TO COPY"
        return ti
    
    
    def stepNondeterministic(
            self,
            t,
            delay=1.0,
            delay0=None,
            tries=1,
            verbose=False,
            reportEqualFail=False,
            pools=None):
        """
        Checks if a test behaves nondeterministically (in terms of all
        non-opaque pool values produced) under an optional timing change.
        Default is to run with no delay for an initial capture of state,
        then run with a 1 second delay, and only run once.
        """
        trajectory = []
        self.restart()
        for s in t:
            self.safely(s)
            trajectory.append(self.trajectoryItem(pools))
            if delay0 is not None:
                time.sleep(delay0)
        for i in range(0, tries):
            pos = 0
            self.restart()
            for s in t:
                self.safely(s)
                try:
                    if (self.trajectoryItem(pools)) != (trajectory[pos]):
                        return True
                except BaseException:
                    if reportEqualFail:
                        raise
                if delay is not None:
                    time.sleep(delay)
                pos += 1
        return False
    
    
    def nondeterministic(
            self,
            t,
            delay=1.0,
            delay0=None,
            tries=1,
            reportEqualFail=False,
            pools=None):
        """
        Checks if a test behaves nondeterministically (in terms of final non-opaque pool values)
        under an optional timing change.  Default is to run with no delay for an initial capture
        of state, then run with a 1 second delay, and only run once.
        """
        self.replay(t, delay=delay0)
        ss = self.shallowState()
        o = set(self.opaque())
        if pools is not None:
            for p in self.pools():
                if p not in pools:
                    o.add(p)
        s0 = {}
        for (name, vals) in ss:
            if name in o:
                continue
            if name.replace(
                "_REF",
                    "") in o:  # Assume if pool is opaque, so is reference
                continue
            s0[name] = {}
            for v in vals:
                try:
                    s0[name][v] = copy.deepcopy(vals[v])
                except BaseException:
                    s0[name][v] = "UNABLE TO COPY"
        for i in range(0, tries):
            self.replay(t, delay=delay)
            ss = self.shallowState()
            s1 = {}
            for (name, vals) in ss:
                if name in o:
                    continue
                if name.replace(
                        "_REF", "") in o:  # Assume if pool is opaque, so is reference
                    continue
                s1[name] = {}
                for v in vals:
                    try:
                        s1[name][v] = copy.deepcopy(vals[v])
                    except BaseException:
                        s1[name][v] = "UNABLE TO COPY"
            try:
                if s0 != s1:
                    return True
            except BaseException:
                if reportEqualFail:
                    raise
        return False
    
    
    def verbose(self, bool):
        self.__verboseActions = bool
    
    
    def verboseOpaque(self, bool):
        self.__verbosePrintOpaque = bool
    
    
    def logOff(self):
        self.__log = None
    
    
    def logAll(self):
        self.__log = 'All'
    
    
    def setLog(self, level):
        self.__log = level
    
    
    def setLogAction(self, f):
        self.__logAction = f
    
    
    def logPrint(self, name, code, text, after):
        print("[", end=' ')
        if after:
            print("POST", end=' ')
        print("LOG " + name + "  :  " + str(code) + "] " + str(text))
    
    
    def testCandidates(self, t, n):
        # Fix so that if n means removal is single items, you just return all the
        # relevant removals
        candidates = []
        if t == []:
            return [[]]
        s = int(len(t) / n)
        if (s == 1):
            n = len(t)
        for i in range(0, n):
            tc = t[0:i * s]
            tc.extend(t[(i + 1) * s:])
            candidates.append(tc)
        return candidates
    
    
    def reduce(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=True,
            rgen=None,
            amplify=False,
            amplifyReplications=1,
            stopFound=False,
            tryFast=True,
            testHandler=None,
            findLocations=False,
            noResetSplit=False,
            safeReduce=False,
            saveIntermediate=None):
        """
        This function takes a test that has failed, and attempts to reduce
        it using a simplified version of Zeller's Delta-Debugging
        algorithm.  pruneGuards determines if disabled guards are
        automatically removed from reduced tests, keepLast determines if
        the last action must remain unchanged (this is useful for keeping
        the fault detected from changing).
    
        amplify changes behavior from "preserve (or find) pred(test) =
        True" to "increase the value of pred(test)"
    
        tryFast means that instead of the binary search, reduce assumes
        the test is already close to 1-minimal (e.g., from normalization)
        and skips right to the smallest granularity, searching for a
        close-by 1-minimal test.
    
        testHandler is an optional function to pass in.  It can do things
        like check for new coverage from a candidate run, and collect such
        tests for quick testing or GA-based exploration.
        """
        try:
            test_before_reduce(self)
        except BaseException:
            pass
    
        intermediate = 0
    
        if len(test) < 2:
            return test
    
        if amplify:
            currBest = pred(test)
            if verbose:
                print("Starting best value:", currBest)
    
        if findLocations:
            ntest = []
            i = 0
            for a in test:
                name = a[0]
                guard = a[1]
                act = a[2]
                ntest.append((name, guard, act, i))
                i += 1
            test = ntest
    
        if keepLast:
            tb = test[:-1]
            addLast = [test[-1]]
        else:
            tb = test
            addLast = []
    
        n = 2
    
        if tryFast:
            n = len(tb)
    
        lastRemove = 0
    
        count = 0
        stests = {}
        while True:
            # If there is nothing left in the test, either the null test fails,
            # of you just need to return the keepLast item
            if len(tb) == 0:
                return tb + addLast
            if verbose or safeReduce:
                # We only perform a sanity check to avoid infinite loops if verbose
                # or if safeReduce is True
                stest = self.captureReplay(tb)
                assert ((stest, n, lastRemove) not in stests)
                stests[(stest, n, lastRemove)] = True
            count += 1
            c = self.testCandidates(tb, n)
            if lastRemove > 0:
                c = c[lastRemove:] + c[:lastRemove]
            if rgen:
                rgen.shuffle(c)
            reduced = False
            removePos = -1
            truePos = -1
            for tc in c:
                removePos += 1
                if verbose == "VERY":
                    print("Trying candidate of length", len(tc + addLast))
                if not findLocations:
                    v = pred(tc + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in tc + addLast])
                if testHandler is not None:
                    testHandler()
                if amplify:
                    if v > currBest:
                        for rep in range(0, amplifyReplications - 1):
                            if not findLocations:
                                v = pred(tc + addLast)
                            else:
                                v = pred([(x[0], x[1], x[2])
                                          for x in tc + addLast])
                            if v <= currBest:
                                break
                        if v > currBest:
                            currBest = v
                            v = True
                            if verbose:
                                print("New best value:", currBest)
                        else:
                            v = False
                    else:
                        v = False
                if v:
                    if stopFound:
                        return (tc + addLast)
                    if verbose == "SHOW":
                        print("REMOVED:")
                        self.prettyPrintRemoved(tb, tc)
                    tb = tc
                    if not noResetSplit:
                        n = 2
                    else:
                        if n > len(tb):
                            n = len(tb)
                    if verbose:
                        print("Reduced test length to", len(tb + addLast))
                    if pruneGuards:
                        self.restart()
                        newtb = []
                        for a in tb:
                            if a[0] == "<<RESTART>>":
                                newtb.append(a)
                                self.restart()
                            elif a[1]():
                                newtb.append(a)
                                try:
                                    a[2]()
                                except KeyboardInterrupt as e:
                                    raise e
                                except BaseException:
                                    pass
                        if verbose:
                            if len(newtb) < len(tb):
                                print("Guard pruning reduced test length to",
                                      len(newtb + addLast))
                                if verbose == "SHOW":
                                    print("REMOVED:")
                                    self.prettyPrintRemoved(tb, newtb)
                        tb = newtb
                    if tryFast:
                        n = len(tb)
                        truePos = (lastRemove + removePos) % max(len(tb), 1)
                        lastRemove = truePos
                        if verbose == "VERY":
                            print("check #", truePos, removePos, lastRemove)
                    if saveIntermediate is not None:
                        self.saveTest(
                            tb +
                            addLast,
                            saveIntermediate +
                            "." +
                            str(intermediate) +
                            ".test")
                        intermediate += 1
                    reduced = True
                    break
            if not reduced:
                if (n == len(tb)):
                    try:
                        test_after_reduce(self)
                    except BaseException:
                        pass
                    return tb + addLast
                n = min(n * 2, len(tb))
                if verbose:
                    print("Failed to reduce, increasing granularity to", n)
            elif False and (not reduced) and tryFast and (lastRemove != 0):
                if verbose:
                    print(
                        "Trying a pass from the beginning, was at position",
                        lastRemove)
                lastRemove = 0
                n = len(tb)
            elif len(tb) == 1:
                try:
                    test_after_reduce(self)
                except BaseException:
                    pass
    
                if not findLocations:
                    v = pred([] + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in [] + addLast])
                if amplify:
                    if v > currBest:
                        v = True
                    else:
                        v = False
                if v:
                    return ([] + addLast)
    
                if not findLocations:
                    v = pred(tc + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in tc + addLast])
                if amplify:
                    if v > currBest:
                        v = True
                    else:
                        v = False
                if v:
                    return (tc + addLast)
                else:
                    return (tb + addLast)
    
    
    def tryCompose(
            tests,
            pred,
            pruneGuards=False,
            keepLast=False,
            verbose=True,
            rgen=None,
            amplify=False,
            combs=1):
        newt = []
        for t in tests:
            newt.extend(t)
        newt = newt * combs
        return reduce(newt, pred, pruneGuards, keepLast, verbose, rgen, amplify)
    
    
    def reductions(
            self,
            test,
            pred,
            pruneGuards=True,
            tryFast=True,
            keepLast=False,
            verbose=True,
            recursive=1,
            useClasses=True,
            limit=None):
        # use recursive = -1 for infinite recursion (all tests)
        r = self.reduce(test, pred, pruneGuards=pruneGuards,
                        keepLast=keepLast, verbose=verbose, tryFast=tryFast)
        reductions = [r]
        anyNew = True
        filterActs = set()
        impossibleSets = []
        analyzedCount = 0
        analyzed = []
        while anyNew:
            recursive = recursive - 1
            filterActs = set([])
            for r in reductions:
                for s in r:
                    if not set([s]) in impossibleSets:
                        filterActs.add(s)
    
            anyNew = False
            sys.stdout.flush()
            for i in range(1, len(filterActs)):
                ncombos = 0
                if verbose:
                    print("ANALYZING SIZE", i, "COMBINATIONS")
                combs = combinations(filterActs, i)
                for c in combs:
                    analyzedCount += 1
                    # if (analyzedCount % 10) == 0:
                    #    print "ANALYZED:",analyzedCount
                    if (limit is not None) and (analyzedCount > limit):
                        print("REDUCTION LIMIT EXCEEDED")
                        return reductions
                    cs = set(c)
                    if cs in analyzed:
                        continue
                    analyzed.append(cs)
                    skipCombo = False
                    for iset in impossibleSets:
                        if [x for x in iset if x not in cs] == []:
                            skipCombo = True
                            break
                    if skipCombo:
                        continue
                    skipCombo = False
                    for r in reductions:
                        if [x for x in r if x in cs] == []:
                            skipCombo = True
                            break
                    if skipCombo:
                        continue
                    ncombos += 1
                    ac = list(map(self.actionClass, cs))
                    if useClasses:
                        tfilter1 = [
                            x for x in test if self.actionClass(x) not in ac]
                        pfilter1 = pred(tfilter1)
                    else:
                        pfilter1 = False
                    tfilter2 = [x for x in test if x not in cs]
                    pfilter2 = pred(tfilter2)
                    if pfilter1:
                        rfilter1 = self.reduce(
                            tfilter1,
                            pred,
                            pruneGuards=pruneGuards,
                            keepLast=keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if rfilter1 not in reductions:
                            if recursive != 0:
                                anyNew = True
                            if verbose:
                                print("ADDING NEW TEST OF LENGTH", len(rfilter1))
                            reductions.append(rfilter1)
                    if pfilter2:
                        rfilter2 = self.reduce(
                            tfilter2,
                            pred,
                            pruneGuards=pruneGuards,
                            keepLast=keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if rfilter2 not in reductions:
                            if recursive != 0:
                                anyNew = True
                            if verbose:
                                print("ADDING NEW TEST OF LENGTH", len(rfilter2))
                            reductions.append(rfilter2)
                    if (not pfilter1) and (not pfilter2):
                        if cs not in impossibleSets:
                            if verbose:
                                print("FOUND IMPOSSIBLE RESTRICTION:", [
                                      self.prettyName(x[0]) for x in cs])
                            impossibleSets.append(cs)
                if verbose:
                    print("ANALYZED", ncombos, "COMBINATIONS")
    
        return reductions
    
    
    def poolUses(self, str):
        uses = []
        for p in self.__pools:
            pos = str.find(p, 0)
            while pos != -1:
                access = str[pos:str.find("]", pos) + 1]
                if access not in uses:
                    uses.append(
                        (access, access[access.find("[") + 1:access.find("]")]))
                pos = str.find(p, pos + 1)
        return uses
    
    
    def powerset(self, iterable):
        xs = list(iterable)
        return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))
    
    
    def reduceEssentials(
            self,
            test,
            original,
            pred,
            pruneGuards=True,
            keepLast=False,
            tryFast=True):
        possibleRemove = test
        if keepLast:
            possibleRemove = test[:-1]
        removals = list(self.powerset(possibleRemove))
        removals = sorted(removals, key=lambda x: len(x), reverse=True)
        workingRemovals = []
        failedRemovals = []
        for rset in removals:
            if rset == []:
                continue
            foundSuperset = False
            for (w, _) in workingRemovals:
                allPresent = True
                for r in rset:
                    if r not in w:
                        allPresent = False
                        break
                if allPresent:
                    foundSuperset = True
                    break
            if foundSuperset:
                continue
            newOrig = [x for x in original if x not in rset]
            if pred(newOrig):
                reduced = self.reduce(
                    newOrig, pred, pruneGuards, keepLast, tryFast=tryFast)
                workingRemovals.append((rset, reduced))
            else:
                failedRemovals.append(rset)
        return (workingRemovals, failedRemovals)
    
    
    def actionReplace(self, action, old, new):
        if action[0] == old:
            return self.__names[new]
        else:
            return action
    
    
    def actionModify(self, action, old, new):
        name = action[0]
        newName = name.replace(old, new)
        return self.__names[newName]
    
    
    def levDist(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        distances = list(range(len(s1) + 1))
        for index2, char2 in enumerate(s2):
            newDistances = [index2 + 1]
            for index1, char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1 + 1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]
    
    
    def getEnabled(self, test, checkEnabled):
        self.restart()
        enableChange = {}
        for i in range(0, len(test)):
            if checkEnabled:
                enableChange[i] = [x[0] for x in self.enabled()]
                self.safely(test[i])
            else:
                enableChange[i] = [x[0] for x in self.actions()]
        for i in range(0, len(test)):
            enableChange[i] = sorted(
                enableChange[i], key=lambda x: self.__orderings[x])
        return enableChange
    
    
    def numReassigns(self, test):
    
        if not self.__noReassigns:
            return 0
    
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i, p))
                        else:
                            lhsPools.append(p)
            i += 1
        return len(reuses)
    
    
    def reduceLengthStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None,
            tryFast=True):
        if verbose == "VERY":
            print("STARTING REDUCE LENGTH STEP")
        # Replace any action with another action, if that allows test to be
        # further reduced
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        stop = len(test)
        if keepLast:
            stop -= 1
    
        for i in range(0, stop):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if name1 != name2:
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i + 1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        rtestC = self.reduce(
                            testC,
                            pred,
                            pruneGuards,
                            keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if len(rtestC) < len(test):
                            if verbose:
                                print(
                                    "NORMALIZER: RULE ReduceAction: STEP",
                                    i,
                                    name1,
                                    "-->",
                                    name2,
                                    "REDUCING LENGTH FROM",
                                    len(test),
                                    "TO",
                                    len(rtestC))
                            return (True, rtestC)
        return (False, test)
    
    
    def replaceAllStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE ALL STEP")
        # Replace all occurrences of an action with a simpler action
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        donePairs = []
        for i in range(0, len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if (self.__orderings[name1] > self.__orderings[name2]) and (
                        (name1, name2) not in donePairs):
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    donePairs.append((name1, name2))
                    testC = [self.actionReplace(x, name1, name2) for x in test]
                    if keepLast:
                        testC = testC[:-1] + [test[-1]]
                        if testC == test:
                            continue
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SimplifyAll:",
                                  name1, "-->", name2)
                        return (True, testC)
        return (False, test)
    
    
    def replacePoolStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE POOL STEP")
        # Replace pools with lower-numbered pools
    
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)
    
        # First try the simple version:
    
        if self.__noReassigns:
    
            for (p, i) in pools:
                for n in range(0, int(i)):
                    new = p.replace("[" + i + "]", "[" + str(n) + "]")
                    testC = [self.actionModify(x, p, new) for x in test]
                    if (testC != test) and (self.numReassigns(
                            testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE ReplacePool:", p, "WITH", new)
                        return (True, testC)
    
            # Remained of this code is now not needed, probably, due to
            # noReassignRule
            return (False, test)
    
        # Reduce number of pools but may need to move assignment to a later
        # position, or only change after the position
        for pos in range(0, len(test)):
            for (p, i) in pools:
                for n in range(0, int(i)):
                    new = p.replace("[" + i + "]", "[" + str(n) + "]")
                    prefix = []
                    moved = []
                    for j in range(0, pos):
                        if new in test[j][0]:
                            moved.append(test[j])
                        else:
                            prefix.append(test[j])
                    suffix = [self.actionModify(x, p, new)
                              for x in moved + test[pos:]]
                    newPrefix = [self.actionModify(x, p, new) for x in prefix]
                    newSuffix = [self.actionModify(x, p, new) for x in suffix]
                    testC = newPrefix + newSuffix
                    if (testC != test) and (self.numReassigns(
                            testC) <= reassignCount) and pred(testC):
                        if verbose:
                            if pos == 0:
                                print(
                                    "NORMALIZER: RULE ReplacePool:", p, "WITH", new)
                            else:
                                print("NORMALIZER: RULE ReplaceMovePool:",
                                      p, "WITH", new, " -- MOVED TO", pos)
                        return (True, testC)
                    # Not possible, try with only replacing between pos and pos2
                    for pos2 in range(len(test), pos, -1):
                        prefix = test[:pos]
                        suffix = [self.actionModify(x, p, new)
                                  for x in test[pos:pos2]]
                        testC = prefix + suffix + test[pos2:]
                        if (testC != test) and (self.numReassigns(
                                testC) <= reassignCount) and pred(testC):
                            if verbose:
                                print("NORMALIZER: RULE ReplacePool:", p,
                                      "WITH", new, "FROM", pos, "TO", pos2)
                            return (True, testC)
        return (False, test)
    
    
    def replaceSingleStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE SINGLE STEP")
        # Replace any single action with a lower-numbered action
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        stop = len(test)
        if keepLast:
            stop -= 1
    
        for i in range(0, stop):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if self.__orderings[name1] > self.__orderings[name2]:
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i + 1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SimplifySingle: STEP",
                                  i, name1, "-->", name2)
                        return (True, testC)
        return (False, test)
    
    
    def swapPoolStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING SWAP POOL STEP")
        # Swap two pool uses in between two positions, if this lowers the minimal
        # action ordering between them
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)
    
        swaps = []
        for (p1, i1) in pools:
            for (p2, i2) in pools:
                for pos1 in range(0, len(test)):
                    for pos2 in range(len(test), pos1, -1):
                        if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                            p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                            p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                            p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                            tempTest = [(x[0].replace(p2, p2newTemp), x[1], x[2])
                                        for x in test[pos1:pos2]]
                            tempTest2 = [(x[0].replace(p1, p1new), x[1], x[2])
                                         for x in tempTest]
                            testC = test[:pos1] + [self.actionModify(
                                x, p2newTemp, p2new) for x in tempTest2] + test[pos2:]
                            leastTestC = -1
                            leastTest = -1
                            for s in range(0, len(test)):
                                if test[s] != testC[s]:
                                    ordTest = self.__orderings[test[s][0]]
                                    if (leastTest == -1) or (ordTest < leastTest):
                                        leastTest = ordTest
                                    ordTestC = self.__orderings[testC[s][0]]
                                    if (leastTestC == -1) or (ordTestC < leastTestC):
                                        leastTestC = ordTestC
                            if leastTestC < leastTest:
                                if (self.numReassigns(testC) <=
                                        reassignCount) and pred(testC):
                                    if verbose:
                                        print(
                                            "NORMALIZER: RULE SwapPool:",
                                            p1,
                                            "AND",
                                            p2,
                                            "BETWEEN STEP",
                                            pos1,
                                            "AND",
                                            pos2)
                                    return (True, testC)
        return (False, test)
    
    
    def opaque(self):
        return self.__opaque
    
    
    def uniqueVals(self):
        ss = self.shallowState()
        uvals = []
        for (pool, vals) in ss:
            if pool not in self.__opaque:
                for v in list(vals.values()):
                    if v is not None:
                        if (pool, str(v)) not in uvals:
                            uvals.append((pool, str(v)))
        return uvals
    
    
    def coversUnique(self, val, catchUncaught=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            uv = self.uniqueVals()
            return val in uv
        return coverPred
    
    
    def noReassignStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if not self.__noReassigns:
            return (False, test)
    
        if verbose == "VERY":
            print("STARTING NOREASSIGNS STEP")
        # Replace reassignments with fresh variables
        pools = []
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i, p))
                        else:
                            lhsPools.append(p)
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p[0])
            i += 1
    
        for (i, pu) in reuses:
            prefix = test[0:i]
            (p, pnum) = pu
            newp = None
            for ni in range(0, self.__psize[p.split(
                    "[")[0].replace(self.__poolPrefix, "")]):
                if int(ni) == int(pnum):
                    continue
                tnewp = p.replace("[" + str(pnum) + "]", "[" + str(ni) + "]")
                print("REPLACING", tnewp, ni, p, pnum)
                if tnewp not in pools:
                    newp = tnewp
                    break
            if newp is None:
                continue
            if verbose:
                print("NORMALIZER: RULE NoReassigns:",
                      i, test[i][0], p, "TO", newp)
            suffix = []
            for s in test[i:]:
                suffix.append(self.actionModify(s, p, newp))
            return (True, prefix + suffix)
    
        return (False, test)
    
    
    def swapActionOrderStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING SWAP ACTION ORDER STEP")
        # Try to swap any out-of-order actions
        lastMover = len(test)
        if keepLast:
            lastMover -= 1
    
        for i in range(0, lastMover):
            for j in range(i + 1, lastMover):
                step1 = test[i][0]
                step2 = test[j][0]
                if self.__orderings[step2] < self.__orderings[step1]:
                    frag1 = test[:i]
                    frag2 = [test[j]]
                    frag3 = test[i + 1:j]
                    frag4 = [test[i]]
                    frag5 = test[j + 1:]
                    testC = frag1 + frag2 + frag3 + frag4 + frag5
                    if pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SwapAction:", i,
                                  test[i][0], "WITH STEP", j, test[j][0])
                        return (True, testC)
        return (False, test)
    
    
    def clearNormalizationCache(self):
        self.__simplifyCache = {}
    
    
    def swapPools(self, test, p1, p2, after=0):
        poolsByLength = sorted(self.__pools, key=len, reverse=True)
        tPrefix = test[:after]
        test = test[after:]
        p1new = self.__poolPrefix + p1
        p2new = self.__poolPrefix + p2
        for p in poolsByLength:
            if p in p1new:
                p1new = p + "[" + p1new.split(p)[1] + "]"
        for p in poolsByLength:
            if p in p2new:
                p2new = p + "[" + p2new.split(p)[1] + "]"
        newTest = [x[0].replace(p1new, "!!P1NEW!!") for x in test]
        newTest = [x.replace(p2new, p1new) for x in newTest]
        newTest = [x.replace("!!P1NEW!!", p2new) for x in newTest]
        newTest = [self.__names[x] for x in newTest]
        return tPrefix + newTest
    
    
    def alphaConvert(self, test, verbose=False):
        """
        This ONLY performs renaming of pools to lowest values possible; it
        CAN in theory cause worse normalization.
        """
        count = {}
        changed = True
        while changed:
            if verbose:
                print("RESTARTING")
            changed = False
            for p in self.__pools:
                count[p] = 0
            i = -1
            for s in test:
                i += 1
                if "=" not in s[0]:
                    continue
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if verbose:
                    print("EXAMINING:", s[0], lhsp, count)
                for (p, n) in lhsp:
                    basep = p.split("[")[0]
                    if verbose:
                        print((p, n), "BASE", basep, count[basep])
                    if count[basep] < int(n):
                        p1new = p
                        p2new = p.replace(n, str(count[basep]))
                        if verbose:
                            print("REPLACING", p1new, "WITH", p2new)
                        newTest = [x[0].replace(p1new, "!!P1NEW!!") for x in test[i:]]
                        newTest = [x.replace(p2new, p1new) for x in newTest]
                        newTest = [x.replace("!!P1NEW!!", p2new) for x in newTest]
                        newTest = [self.__names[x] for x in newTest]
                        test = test[:i] + newTest
                        # self.prettyPrintTest(test)
                        count[basep] += 1
                        changed = True
                        break
                    elif int(n) >= count[basep]:
                        count[basep] += 1
                if changed:
                    break
        return test
    
    
    def normalize(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            speed="FAST",
            checkEnabled=False,
            distLimit=None,
            reorder=True,
            noReassigns=False,
            useCache=True,
            tryFast=True):
        """
        Attempts to produce a normalized test case
        """
        try:
            test_before_normalize(self)
        except BaseException:
            pass
    
        if noReassigns:
            self.__noReassigns = True
        else:
            self.__noReassigns = False
    
        # Check the cache
        stest = self.captureReplay(test)
        if useCache and (stest in self.__simplifyCache):
            if verbose:
                print("NORMALIZER: FOUND TEST IN CACHED RESULTS")
            return self.__simplifyCache[stest]
        history = [stest]
    
        # Turns off requirement that you can't initialize an unused variable,
        # allowing reducer to take care of redundant assignments
        # self.relax()
    
        # Default speed is fast, if speed not recognized
        simplifiers = [
            self.noReassignStep,
            self.replaceAllStep,
            self.replacePoolStep,
            self.replaceSingleStep,
            self.swapPoolStep,
            self.swapActionOrderStep,
            self.reduceLengthStep]
        # simplifiers = [self.noReassignStep, self.replaceAllStep, self.replaceSingleStep,
        #                self.swapActionOrderStep, self.reduceLengthStep]
        # Default approach tries a reduce after any change
        reduceOnChange = True
        if speed == "SLOW":
            simplifiers = [
                self.reduceLengthStep,
                self.replaceAllStep,
                self.replacePoolStep,
                self.replaceSingleStep,
                self.swapPoolStep,
                self.swapActionOrderStep]
        elif speed == "ONEREDUCE":
            # Runs one attempt at length reduction before normal simplification,
            # without reduction step
            (changed, test) = self.reduceLengthStep(test, pred, pruneGuards,
                                                    keepLast, verbose, checkEnabled,
                                                    distLimit, tryFast=tryFast)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
            simplifiers = [
                self.replaceAllStep,
                self.replacePoolStep,
                self.replaceSingleStep,
                self.swapPoolStep,
                self.swapActionOrderStep]
        elif speed == "MEDIUM":
            # Runs one attempt at length reduction before normal simplification
            (changed, test) = self.reduceLengthStep(test, pred,
                                                    pruneGuards, keepLast, verbose, tryFast=tryFast)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
        elif speed == "VERYFAST":
            reduceOnChange = False
            if distLimit is None:
                distLimit = 3  # maximum of 3 char change when replacing actions!
                # allows numeric switches, simple pool modifications, but very few method changes
        elif speed == "VERYFASTREDUCE":
            reduceOnChange = True
            if distLimit is None:
                distLimit = 3  # maximum of 3 char change when replacing actions!
                # allows numeric switches, simple pool modifications, but very few method changes
    
        numChanges = 0
        changed = True
        stests = {}
        while changed:
            stest = self.captureReplay(test)
            assert (stest not in stests)
            stests[stest] = True
            changed = False
            if reorder:
                newSimplifiers = list(simplifiers)
            for s in simplifiers:
                oldTest = test
                (changed, test) = s(test, pred, pruneGuards,
                                    keepLast, verbose, checkEnabled, distLimit)
                if changed:
                    if reduceOnChange:
                        test = self.reduce(test, pred, pruneGuards,
                                           keepLast, verbose=verbose, tryFast=True)
                    if verbose:
                        self.prettyPrintTest(test)
                    stest = self.captureReplay(test)
                    if useCache and (stest in self.__simplifyCache):
                        if verbose:
                            print("NORMALIZER: FOUND TEST IN CACHED RESULTS")
                        result = self.__simplifyCache[stest]
                        for t in history:
                            self.__simplifyCache[t] = result
                        # self.stopRelax()
                        return result
                    history.append(stest)
                    if reorder:
                        simplifiers = newSimplifiers
                    break
                elif reorder:
                    newSimplifiers.remove(s)
                    newSimplifiers.append(s)
    
        # No changes, this is 1-simple (fix-point)
        try:
            test_after_normalize(self)
        except BaseException:
            pass
    
        # self.stopRelax()
        # restore normal TSTL semantics!
    
        # Update the simplification cache and return
        if useCache:
            for t in history:
                self.__simplifyCache[t] = test
        return test
    
    
    def freshSimpleVariants(self, name, previous, replacements):
        prevNames = [x[0] for x in previous]
        prevNames.reverse()
        lastAppear = []
        eqFind = name.find("=")
        if eqFind != -1:
            poolAssign = name[0:eqFind - 1]
        else:
            poolAssign = None
        pools = self.poolUses(name)
        lastAppearMap = {}
        for (p, i) in pools:
            for n in prevNames:
                if p[0:p.find("[")] in self.__consts:
                    if n.find(p + " = ") == -1:
                        continue
                lastAppearMap[p] = [n]
                break
            skeys = list(replacements.keys())
            skeys = [x for x in skeys if x < len(previous)]
            skeys = sorted(skeys, reverse=True)
            for i in skeys:
                foundAny = False
                for r in replacements[i]:
                    if p[0:p.find("[")] in self.__consts:
                        if r.find(p + " = ") == -1:
                            continue
                    foundAny = True
                    if p in lastAppearMap:
                        lastAppearMap[p].append(r)
                    else:
                        lastAppearMap[p] = [r]
                if foundAny:
                    break
        for n in lastAppearMap:
            lastAppear.extend(lastAppearMap[n])
    #    print "LAST APPEAR = ",lastAppear
        freshSimples = []
        for (p, i) in pools:
            if p == poolAssign:
                continue
            for n in self.__names:
                if n in lastAppear:
                    continue
                if (p + " = ") in n:
                    uses = self.poolUses(n[n.find("=") + 1:])
                    if uses == []:
                        freshSimples.append([self.__names[n], self.__names[name]])
        freshSimples = sorted(
            freshSimples, key=lambda x: self.__orderings[x[0][0]])
        return freshSimples
    
    
    def generalize(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None,
            returnCollect=False,
            collected=None,
            depth=0,
            silent=False,
            targets=None,
            fresh=True):
    
        if collected is None:
            collected = {}
    
        newCollected = {}
    
        # Change so double assignments are allowed
        # self.relax()
    
        enableChange = self.getEnabled(test, checkEnabled)
    
        canReplace = {}
        canSwap = {}
        canMakeSimple = {}
        for i in range(0, len(test)):
            canSwap[i] = []
        for i in range(0, len(test)):
            canReplace[i] = []
            canMakeSimple[i] = []
            if i not in enableChange:
                continue
            for a in enableChange[i]:
                if (distLimit is not None) and (
                        self.levDist(a, test[i][0]) > distLimit):
                    continue
                if a != test[i][0]:
                    testC = test[:i] + [self.__names[a]] + test[i + 1:]
                    if pred(testC):  # and self.allEnabled(testC):
                        if returnCollect:
                            stestC = self.captureReplay(testC)
                            if stestC not in collected:
                                collected[stestC] = True
                                newCollected[stestC] = True
                            if stestC in targets:
                                # self.stopRelax()
                                return (True, stestC, dict(collected))
                        canReplace[i].append(a)
            for j in range(i + 1, len(test)):
                if i == j or test[i][0] == test[j][0]:
                    continue
                testC = test[:i] + [test[j]] + \
                    test[i + 1:j] + [test[i]] + test[j + 1:]
                if pred(testC):  # and self.allEnabled(testC):
                    if returnCollect:
                        stestC = self.captureReplay(testC)
                        if stestC not in collected:
                            collected[stestC] = True
                            newCollected[stestC] = True
                            if stestC in targets:
                                # self.stopRelax()
                                return (True, stestC, dict(collected))
                    canSwap[i].append(j)
                    canSwap[j].append(i)
            if fresh:
                for v in self.freshSimpleVariants(
                        test[i][0], test[:i], canReplace):
                    testC = test[:i] + v + test[i + 1:]
                    # self.prettyPrintTest(testC)
                    if pred(testC) and self.allEnabled(testC):
                        canMakeSimple[i].append(v)
        if not silent:
            noOrder = []
            endSwappable = -1
            for i in range(0, len(test)):
                if endSwappable >= i:
                    continue
                foundSwap = False
                for j in range(len(test) - 1, i, -1):
                    allSwappable = True
                    for k1 in range(i, j + 1):
                        for k2 in range(k1 + 1, j + 1):
                            if k2 not in canSwap[k1]:
                                allSwappable = False
                                break
                        if not allSwappable:
                            break
                    if allSwappable:
                        noOrder.append((i, j))
                        for k1 in range(i, j + 1):
                            for k2 in range(i, j + 1):
                                if k2 in canSwap[k1]:
                                    canSwap[k1].remove(k2)
                        endSwappable = j
                        break
            for i in range(0, len(test)):
                for (begin, end) in noOrder:
                    if i == begin:
                        print("#[")
                pn = self.prettyName(test[i][0])
                spaces = " " * (90 - len(pn) - len(" # STEP"))
                print(self.prettyName(test[i][0]), spaces, "# STEP", i)
                if canReplace[i] != []:
                    firstRep = None
                    lastRep = None
                    for rep in canReplace[i]:
                        if firstRep is None:
                            firstRep = rep
                            lastRep = rep
                        elif self.__orderings[rep] != (self.__orderings[lastRep] + 1):
                            if firstRep == lastRep:
                                print("#  or", self.prettyName(firstRep))
                            else:
                                print("#  or", self.prettyName(firstRep))
                                print("#   -", self.prettyName(lastRep))
                            firstRep = rep
                            lastRep = rep
                        else:
                            lastRep = rep
                    if firstRep == lastRep:
                        print("#  or", self.prettyName(firstRep))
                    else:
                        print("#  or", self.prettyName(firstRep))
                        print("#   -", self.prettyName(lastRep))
                if canMakeSimple[i] != []:
                    for v in canMakeSimple[i]:
                        print("#  or (")
                        for s in v[:-1]:
                            print("#     ", self.prettyName(s[0]), ";")
                        print("#     ", self.prettyName(v[-1][0]))
                        print("#     )")
                if canSwap[i] != []:
                    if len(canSwap[i]) == 1:
                        print("#  swaps with step", end=' ')
                    else:
                        print("#  swaps with steps", end=' ')
                    for j in canSwap[i]:
                        print(j, end=' ')
                    print()
                for (begin, end) in noOrder:
                    if i == end:
                        print("#] (steps in [] can be in any order)")
        # Restore semantics
        # self.stopRelax()
        if returnCollect:
            if depth == 0:
                return (False, None, dict(collected))
            else:
                allCollected = dict(collected)
                for c in newCollected:
                    (found,
                     stest,
                     cGen) = self.generalize(self.replayable(c),
                                             pred,
                                             pruneGuards,
                                             keepLast,
                                             verbose,
                                             checkEnabled,
                                             distLimit,
                                             returnCollect=True,
                                             collected=allCollected,
                                             depth=depth - 1,
                                             silent=True,
                                             targets=targets)
                    for c2 in cGen:
                        if c2 not in allCollected:
                            allCollected[c2] = True
                    if found is True:
                        return (True, stest, dict(allCollected))
                return (False, None, dict(allCollected))
    
    
    def relax(self):
        self.__relaxUsedRestriction = True
    
    
    def setReload(self, val):
        self.__doReload = val
    
    
    def stopRelax(self):
        self.__relaxUsedRestriction = False
    
    
    def moduleLocations(self):
        # This code may not be completely robust, but it seems to work, unless
        # previous approaches
        locs = []
        for m in self.__importModules:
            try:
                p = m.__path__
                if p != []:
                    locs.extend(m.__path__)
                else:
                    raise AttributeError
            except AttributeError:
                try:
                    f = m.__file__
                    if ("lib-dynload" in f) or ("site-packages" not in f):
                        continue  # skip system code
                    locs.append(m.__name__)
                except AttributeError:
                    pass
        return locs
    def __updateCov(self, extendCov=False):
        if not extendCov:
            self.__newBranches = set()
            self.__newStatements = set()
        newCov = self.__cov.get_data()
        if self.__oldCovData is None:
            self.__oldCovData = coverage.CoverageData()
        self.__oldCovData.update(newCov)
        if newCov.measured_files() is None:
            return
        for src_file in newCov.measured_files():
            thisArcs = newCov.arcs(src_file)
            if thisArcs is None:
                continue  # assume if we have arcs we have lines
            for arc in thisArcs:
                branch = (src_file, arc)
                if branch not in self.__allBranches:
                    self.__allBranches.add(branch)
                    self.__newBranches.add(branch)
                    self.__newCurrBranches.add(branch)
                if branch not in self.__currBranches:
                    self.__currBranches.add(branch)
            for line in newCov.lines(src_file):
                statement = (src_file, line)
                if statement not in self.__allStatements:
                    self.__allStatements.add(statement)
                    self.__newStatements.add(statement)
                    self.__newCurrStatements.add(statement)
                if statement not in self.__currStatements:
                    self.__currStatements.add(statement)
    
    
    def silenceCoverage(self):
        self.__cov._warn_no_data = False
    
    
    def internalReport(self):
        print("TSTL INTERNAL COVERAGE REPORT:")
        if self.__oldCovData is None:
            return
        for src_file in self.__oldCovData.measured_files():
            adata = self.__oldCovData.arcs(src_file)
            print(src_file, "ARCS:", len(adata), sorted(adata))
            for (f, a) in self.__allBranches:
                if f == src_file:
                    if a not in adata:
                        print("WARNING:", a, "VISITED BUT MISSING FROM COVERAGEDATA")
            for a in adata:
                if (src_file, a) not in self.__allBranches:
                    print(
                        "WARNING:",
                        a,
                        "IN COVERAGEDATA BUT NOT IN TSTL COVERAGE")
            ldata = list(set(self.__oldCovData.lines(src_file)))
            print(src_file, "LINES:", len(ldata), sorted(ldata))
            for (f, l) in self.__allStatements:
                if f == src_file:
                    if l not in ldata:
                        print("WARNING:", l, "VISITED BUT MISSING FROM COVERAGEDATA")
            for l in ldata:
                if (src_file, l) not in self.__allStatements:
                    print("WARNING", l, "IN COVERAGEDATA BUT NOT IN TSTL COVERAGE")
        for (f, l) in self.__allStatements:
            if f not in self.__oldCovData.measured_files():
                print("WARNING:", (f, l), "IS NOT IN COVERAGEDATA")
        print("TSTL BRANCH COUNT:", len(self.__allBranches))
        print("TSTL STATEMENT COUNT:", len(self.__allStatements))
    
    
    def cleanCov(self):
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
        if self.__oldCovData is None:
            self.__oldCovData = coverage.CoverageData()
        if self.__cov.get_data() is None:
            return
        self.__oldCovData.update(self.__cov.get_data())
        self.__cov.erase()
    
    
    def resetCov(self):
        self.__cov.erase()
        self.__oldCovData = None
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
    
    
    def report(self, filename):
        if self.__oldCovData is not None:
            self.__oldCovData.write_file(filename)
            self.__cov.combine([filename])
        outf = open(filename, 'w')
        r = -1
        try:
            r = self.__cov.report(morfs=self.__modules,
                                  file=outf, show_missing=True)
        finally:
            outf.close()
            return r
    
    
    def htmlReport(self, dir):
        if self.__oldCovData is not None:
            self.__oldCovData.write_file(dir + "/.tmpcov")
            self.__cov.combine([dir + "/.tmpcov"])
        r = -1
        try:
            r = self.__cov.html_report(
                morfs=self.__modules,
                directory=dir,
                title="TSTL Coverage Report",
                show_missing=True)
        finally:
            return r
    
    
    def allBranches(self):
        return self.__allBranches
    
    
    def allStatements(self):
        return self.__allStatements
    
    
    def currBranches(self):
        return self.__currBranches
    
    
    def currStatements(self):
        return self.__currStatements
    
    
    def newBranches(self):
        return self.__newBranches
    
    
    def newStatements(self):
        return self.__newStatements
    
    
    def newCurrBranches(self):
        return self.__newCurrBranches
    
    
    def newCurrStatements(self):
        return self.__newCurrStatements
    
    
    def startCoverage(self):
        self.__collectCov = True
    
    
    def stopCoverage(self):
        self.__collectCov = False
    
    
    def coversBranches(self, branches, catchUncaught=False, checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
    
    
    def coversStatements(self, statements, catchUncaught=False, checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            return True
        return coverPred
    
    
    def coversAll(
            self,
            statements,
            branches,
            catchUncaught=False,
            checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
    
    
    def coversMore(
            self,
            statements,
            branches,
            catchUncaught=False,
            checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            for b in cb:
                if b not in branches:
                    return True
            for s in cs:
                if s not in statements:
                    return True
            return False
        return coverPred
    
    
    def coversSame(self, test, catchUncaught=False, checkProp=False):
        self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        return self.coversAll(
            self.currStatements(),
            self.currBranches(),
            catchUncaught=catchUncaught,
            checkProp=checkProp)
    
    
    def coversMoreThan(self, test, catchUncaught=False, checkProp=False):
        self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        return self.coversMore(
            self.currStatements(),
            self.currBranches(),
            catchUncaught=catchUncaught,
            checkProp=checkProp)
    
    
    def coverDecompose(
            self,
            test,
            verbose=False,
            catchUncaught=False,
            checkProp=False):
        (result, coverages) = self.replay(test, returnCov=True,
                                          catchUncaught=catchUncaught, checkProp=checkProp)
        tests = []
        coverages.reverse()
    
        allSCoverages = set([])
        allBCoverages = set([])
        for (s, b) in coverages:
            allSCoverages.update(set(s))
            allBCoverages.update(set(b))
    
        if verbose:
            print("ORIGINAL TEST OF LENGTH", len(test), "COVERS", len(
                allSCoverages), "STATEMENTS AND", len(allBCoverages), "BRANCHES")
    
        i = 1
        while (len(allSCoverages) != 0) or (len(allBCoverages) != 0):
            (sgoal, bgoal) = coverages[0]
            if verbose:
                print("CONSTRUCTING TEST #" + str(i), "WITH GOAL",
                      len(sgoal), "STATEMENTS AND", len(bgoal), "BRANCHES")
            t = self.reduce(
                test,
                self.coversAll(
                    sgoal,
                    bgoal,
                    catchUncaught=catchUncaught,
                    checkProp=checkProp),
                verbose=verbose)
            tests.append(t)
            self.replay(t, catchUncaught=catchUncaught, checkProp=checkProp)
            currS = set(self.currStatements())
            currB = set(self.currBranches())
            allSCoverages.difference_update(currS)
            allBCoverages.difference_update(currB)
            if verbose:
                print("NEW TEST OF LENGTH", len(t), "COVERS", len(
                    currS), "STATEMENTS AND", len(currB), "BRANCHES")
                print("REMAINING COVERAGE GOALS:", len(allSCoverages),
                      "STATEMENTS,", len(allBCoverages), "BRANCHES")
            newCoverages = []
            for (s, b) in coverages:
                newS = s.copy()
                newB = b.copy()
                newS.difference_update(currS)
                newB.difference_update(currB)
                if verbose and ((len(newS) != len(s)) or (len(newB) != len(b))):
                    print("GOAL WAS:", len(s), len(b))
                    print("NOW:", len(newS), len(newB))
                if (len(newS) != 0) or (len(newB) != 0):
                    newCoverages.append((newS, newB))
            coverages = newCoverages
            i += 1
        return tests
