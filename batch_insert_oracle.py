import cx_Oracle
from datetime import datetime


def sequential_insert():
    dsn_tns = cx_Oracle.makedsn('<HOSTNAME>', '<PORT NO>', '<ORACLE_SID>')
    dbconn = cx_Oracle.connect('<SCHEMA>', '<PASSWORD>', dsn_tns)
    dbconn.autocommit = True
    c = dbconn.cursor()
    t1 = datetime.now()
    c.execute("insert into ashianan_dummy values('A',1)")
    c.execute("insert into ashianan_dummy values('B',2)")
    c.execute("insert into ashianan_dummy values('C',3)")
    c.execute("insert into ashianan_dummy values('D',4)")
    c.close()
    t2 = datetime.now()
    print(t1)
    print(t2)


# sequential_insert()


def bulk_insert():
    dsn_tns = cx_Oracle.makedsn('<HOSTNAME>', '<PORT NO>', '<ORACLE_SID>')
    dbconn = cx_Oracle.connect('<SCHEMA>', '<PASSWORD>', dsn_tns)
    dbconn.autocommit = True
    c = dbconn.cursor()
    t1 = datetime.now()
    data =[15, 16, 17, 18]
    c.executemany("insert into ashianan_dummy values('A',57)", batcherrors=True)
    t2 = datetime.now()
    print(str(c.rowcount))
    print(t1)
    print(t2)
    for err in c.getbatcherrors():
        print(f"Row {err.offset} has error {err.message}")
    dbconn.commit()
    c.close()



bulk_insert()
