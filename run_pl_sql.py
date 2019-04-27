import cx_Oracle

dns_tns = cx_Oracle.makedsn("lnxdb-dev-vm-288", "1551", "DRVDEV")
conn = cx_Oracle.connect("dbsnmp", "dboem10g", dns_tns)

c = conn.cursor()

statement = """
            declare
  
            -- declare variable x, y  
            -- and z of datatype number 
            x number(5);              
            y number(5);             
            z number(7);         
              
            begin
              
            -- Here we Assigning 10 into x 
            x:=10;                  
              
            -- Assigning 20 into x 
            y:=20;                  
              
            -- Assigning sum of x and y into z 
            z:=x+y;                  
              
            dbms_output.put_line('Sum is '||z);  
            end;                          
                
            """
c.execute(statement)
#result = c.fetchall()

#print(result)
