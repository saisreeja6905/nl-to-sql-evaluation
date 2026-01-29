Title: An Evaluation Framework for Natural Language to SQL Systems

This academic mini project focuses on evaluating the correctness of SQL queries
generated from natural language questions.

The project compares expected SQL queries with simulated LLM-generated queries
using execution-based validation.

# NL-to-SQL Evaluation Framework

## Overview
This academic mini project implements an execution-based evaluation framework for Natural Language to SQL systems. The objective is to assess the correctness of SQL queries generated from natural language inputs by comparing them against expected (ground-truth) SQL queries.

Instead of generating SQL using a live LLM, the project simulates LLM-generated queries and evaluates them through actual execution on a database.

---

## Objectives
- Evaluate the correctness of SQL queries derived from natural language questions  
- Identify logical and aggregation-related errors in generated queries  
- Analyze common failure patterns in NL-to-SQL systems  

---

## Methodology
1. Define natural language questions  
2. Write expected (correct) SQL queries for each question  
3. Simulate LLM-generated SQL queries  
4. Execute both expected and generated queries on a SQLite database  
5. Compare results to classify queries as Correct, Logical Error, or Syntax Error  

---

## Tools and Technologies
- Python  
- SQLite  
- Pandas  

---

## Project Structure

Future Scope:
- Integration with Gemini Pro for real-time SQL generation

