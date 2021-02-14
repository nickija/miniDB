from database import Database
from table import Table
import pickle

#table wide exclusive locking:
def lockX_table(self, table_name):
        '''
        Locks the specified table using the exclusive lock (X)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta': #AN TO TABLE EINAI META TABLE, DE THELOUME NA KLEIDWTHEI
            return

        self.tables['meta_locks']._update_row(True, 'xlocked', f'table_name=={table_name}') #EKEI POU TO TABLE NAME EINAI IDIO ME TO TABLE NAME MESA STO META LOCKS, KANE TO EXCLUSIVE LOCK TOU NA EINAI TRUE
        self._save_locks()

def unlockX_table(self, table_name):
        '''
        Unlocks the specified table that is exclusivelly locked (X)

        table_name -> table's name (needs to exist in database)
        '''
        self.tables['meta_locks']._update_row(False, 'xlocked', f'table_name=={table_name}') #EKEI POU TO TABLE NAME EINAI IDIO ME TO TABLE NAME MESA STO META LOCKS, KANE TO EXCLUSIVE LOCK TOU NA EINAI FALSE WSTE NA GINEI UNLOCK
        self._save_locks()

def isX_locked(self, table_name):
        '''
        Check whether the specified table is exclusivelly locked (X)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':  # meta tables will never be locked (they are internal)
            return False

        with open(f'{self.savedir}/meta_locks.pkl', 'rb') as f:
            self.tables.update({'meta_locks': pickle.load(f)})
            self.meta_locks = self.tables['meta_locks']

        try:
            res = self.select('meta_locks', ['xlocked'], f'table_name=={table_name}', return_object=True).xlocked[0] #TOU LEW NA PAREI TO EXCLUSIVE LOCK(XLOCKED) TO MHDENIKO TOU STOIXEIO KAI NA TO XWSEI STO RES ANALOGA AN EINAI TRUE H FALSE
            if res:
                print(f'Table "{table_name}" is currently exclusicely locked.')
            return res

        except IndexError:
            return

#table wide shared locking:
def lockS_table(self, table_name):
        '''
        Locks the specified table using the share lock (S)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':
            return

        self.tables['meta_locks']._update_row(True, 'slocked', f'table_name=={table_name}') #EKEI POU TO TABLE NAME EINAI IDIO ME TO TABLE NAME MESA STO META LOCKS, KANE TO SHARE LOCK TOU NA EINAI TRUE
        self._save_locks()

def unlockS_table(self, table_name):
        '''
        Unlocks the specified table that is share locked (S)

        table_name -> table's name (needs to exist in database)
        '''
        self.tables['meta_locks']._update_row(False, 'slocked', f'table_name=={table_name}') #EKEI POU TO TABLE NAME EINAI IDIO ME TO TABLE NAME MESA STO META LOCKS, KANE TO SHARE LOCK TOU NA EINAI FALSE
        self._save_locks()

def isS_locked(self, table_name):
        '''
        Check whether the specified table is exclusivelly locked (X)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':  # meta tables will never be locked (they are internal)
            return False

        with open(f'{self.savedir}/meta_locks.pkl', 'rb') as f:
            self.tables.update({'meta_locks': pickle.load(f)})
            self.meta_locks = self.tables['meta_locks']

        try:
            res = self.select('meta_locks', ['slocked'], f'table_name=={table_name}', return_object=True).slocked[0] #TOU LEW PARE TO SLOCKED(SHARE LOCKED) EKEI POU TO TABLE NAME STO META LOCKS EINAI IDIO ME AUTO POU TOU DINW, KAI EITE EINAI FALSE H TRUE, XWSTO STO RES
            if res:
                print(f'Table "{table_name}" is currently share locked.')
            return res

        except IndexError:
            return

# def lockX_row(self, table_name, row):
#         '''
#         Locks the specified row using the exclusive lock (X)
#
#         table_name -> table's name (needs to exist in database)
#         '''
#         if table_name[:4]=='meta':
#             return
#
#         self.select('meta_locks','*', f'table_name=={table_name}', None, False, None)._update_row(True, 'xlocked', f'row=={row}') #
#         self._save_locks()


#row wide exclusive locking:
def lockX_row(self, table_name, row):
        '''
        Locks the specified row using the exclusive lock (X)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':
            return

        self.tables['meta_locks']._update_row(True, 'χlocked', f'row=={row}') #TOU LEW NA PAEI EKEI POU TO ROWSTO META LOCKS EINAI IDIO ME TO ROW POU TOU DINW, ANEKSARTHTA APO TO TABLE NAME, KAI NA XWSEI EKEI TRUE STO XLOCKED
        self._save_locks()

def unlockX_row(self, table_name, row):
        '''
        Unlocks the specified row that is exclusivelly locked (X)

        table_name -> table's name (needs to exist in database)
        '''
        self.tables['meta_locks']._update_row(False, 'xlocked', f'row=={row}') #TOU LEW NA PAEI EKEI POU TO ROWSTO META LOCKS EINAI IDIO ME TO ROW POU TOU DINW, ANEKSARTHTA APO TO TABLE NAME, KAI NA XWSEI EKEI FALSE STO XLOCKED
        self._save_locks()

def is_rowX_locked(self, table_name, row):
        '''
        Check whether the specified row is exclusivelly locked (X)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':  # meta tables will never be locked (they are internal)
            return False

        with open(f'{self.savedir}/meta_locks.pkl', 'rb') as f:
            self.tables.update({'meta_locks': pickle.load(f)})
            self.meta_locks = self.tables['meta_locks']

        try:
            res = self.select('meta_locks', ['xlocked'], f'row=={row}', return_object=True).xlocked[0] #LEW: EKEI POU TO ROW POU SOU DINW EINAI IDIO ME TO ROW STO META LOCKS, FERE MOU AUTO POU EXEI STH STHLH XLOCKED(TRUE H FALSE) KAI XWSTO STO RES
            if res:
                print(f'Row is currently exclusicely locked.')
            return res

        except IndexError:
            return

#row wide shared locking:
def lockS_row(self, table_name, row):
        '''
        Locks the specified row using the share lock (S)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':
            return

        self.tables['meta_locks']._update_row(True, 'slocked', f'row=={row}') #PHGAINE EKEI POU TO ROW POU SOU DINW NA SYGKRINEIS AN EINAI IDIO ME KAPOIO ROW POU EXEIS MESA SOU, KAI XWSE STO SLOCKED(SHARE LOCKED) TRUE
        self._save_locks()

def unlockS_row(self, table_name, row):
        '''
        Unlocks the specified row that is share locked (S)

        table_name -> table's name (needs to exist in database)
        '''
        self.tables['meta_locks']._update_row(False, 'slocked', f'row=={row}') #PHGAINE EKEI POU TO ROW POU SOU DINW NA SYGKRINEIS AN EINAI IDIO ME KAPOIO ROW POU EXEIS MESA SOU, KAI XWSE STO SLOCKED(SHARE LOCKED) FALSE
        self._save_locks()

def is_rowS_locked(self, table_name, row):
        '''
        Check whether the specified row is share locked (S)

        table_name -> table's name (needs to exist in database)
        '''
        if table_name[:4]=='meta':  # meta tables will never be locked (they are internal)
            return False

        with open(f'{self.savedir}/meta_locks.pkl', 'rb') as f:
            self.tables.update({'meta_locks': pickle.load(f)})
            self.meta_locks = self.tables['meta_locks']

        try:
            res = self.select('meta_locks', ['slocked'], f'row=={row}', return_object=True).slocked[0] #PAIRNW TO VALUE(TRUE H FALSE) TOU SLOCKED EKEI POU TO ROW EINAI IDIO ME TO ROW MEA STO META LOCKS KAI TO VAZW STO RES GIA NA TO EPISTREPSW
            if res:
                print(f'Row is currently share locked.')
            return res

        except IndexError:
            return
