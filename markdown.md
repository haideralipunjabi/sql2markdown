## 1. `select * from emp;`
|EMPNO|ENAME|INIT|JOB|MGR|BDATE|MSAL|COMM|DEPTNO|
|-|-|-|-|-|-|-|-|-|
|7001|SMITH|N|TRAINER|7902|17-DEC-75|1800| |20|
|7002|ALLEN|JAM|SALESREP|7006|20-MAY-71|1600|300|30|
|7003|WARD|TF|SALESREP|7006|02-MAR-72|1250|500|10|
|7004|JACK|JM|MANAGER|7009|02-APR-77|2975| |20|
|7005|BROWN|P|SALESREP|7006|28-SEP-76|1250|1400|30|
|7006|BLAKE|R|MANAGER|7009|01-NOV-73|2850| |10|
|7007|CLARK|AB|MANAGER|7009|09-JUN-75|2450| |10|
|7008|SCOTT|DEF|TRAINER|7004|26-NOV-79|3000| |20|
|7009|KING|CC|DIRECTOR| |17-OCT-72|5000| |10|
|7010|BREAD|JJ|SALESREP|7006|28-SEP-78|1500| 0|30|
|7011|ADAMS|AA|TRAINER|7008|30-DEC-76|1100| |20|
|7012|JONES|R|ADMIN|7006|03-OCT-79|8000| |30|
|7902|FORD|MG|TRAINER|7004|13-FEB-79|3000| |20|
|7934|MARY|ABC|ADMIN|7007|23-JAN-72|1300| |10|
## 2. `select ename, msal from emp where msal > 2000;`
|ENAME|MSAL|
|-|-|
|JACK|2975|
|BLAKE|2850|
|CLARK|2450|
|SCOTT|3000|
|KING|5000|
|JONES|8000|
|FORD|3000|
## 3. `select * from emp where ename like 'S%';`
|EMPNO|ENAME|INIT|JOB|MGR|BDATE|MSAL|COMM|DEPTNO|
|-|-|-|-|-|-|-|-|-|
|7001|SMITH|N|TRAINER|7902|17-DEC-75|1800| |20|
|7008|SCOTT|DEF|TRAINER|7004|26-NOV-79|3000| |20|
## 4. `select * from emp where ename like '%S';`
|EMPNO|ENAME|INIT|JOB|MGR|BDATE|MSAL|COMM|DEPTNO|
|-|-|-|-|-|-|-|-|-|
|7011|ADAMS|AA|TRAINER|7008|30-DEC-76|1100| |20|
|7012|JONES|R|ADMIN|7006|03-OCT-79|8000| |30|
## 5. `select * from emp where ename like '_L%';`
|EMPNO|ENAME|INIT|JOB|MGR|BDATE|MSAL|COMM|DEPTNO|
|-|-|-|-|-|-|-|-|-|
|7002|ALLEN|JAM|SALESREP|7006|20-MAY-71|1600|300|30|
|7006|BLAKE|R|MANAGER|7009|01-NOV-73|2850| |10|
|7007|CLARK|AB|MANAGER|7009|09-JUN-75|2450| |10|
## 6. `select * from emp where comm != 0;`
|EMPNO|ENAME|INIT|JOB|MGR|BDATE|MSAL|COMM|DEPTNO|
|-|-|-|-|-|-|-|-|-|
|7002|ALLEN|JAM|SALESREP|7006|20-MAY-71|1600|300|30|
|7003|WARD|TF|SALESREP|7006|02-MAR-72|1250|500|10|
|7005|BROWN|P|SALESREP|7006|28-SEP-76|1250|1400|30|
## 7. `select ename "Name", msal "Salary"  from emp;`
|Name|Salary|
|-|-|
|SMITH|1800|
|ALLEN|1600|
|WARD|1250|
|JACK|2975|
|BROWN|1250|
|BLAKE|2850|
|CLARK|2450|
|SCOTT|3000|
|KING|5000|
|BREAD|1500|
|ADAMS|1100|
|JONES|8000|
|FORD|3000|
|MARY|1300|
