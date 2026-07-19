create database project;
use project;
select * from Customers;

select count(*) from customers;
select count(*) from customers where Churn = "Yes";
select count(*) from customers where churn = "No";
select round(count(case when churn = "Yes" then 1 end)/count(*)*100,2) as churn_Rate from customers;
select contract, count(*) as Customers from customers where churn = "Yes" group by contract;
select paymentmethod, count(*) as Customers from customers where churn = "Yes" group by paymentmethod order by Customers desc;
select CustomerID,MonthlyCharges,Churn from customers where monthlycharges > 80 order by monthlycharges desc;
select avg(tenure) from customers where churn = "Yes";
