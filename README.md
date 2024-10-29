# Real-time Financial Data Processing System

- Developed a real-time financial data processing system in Python, interfacing with a market data server to retrieve and analyze stock quotes for multiple securities.
- Implemented and optimized algorithms for calculating stock price ratios and handling edge cases, enhancing the reliability and accuracy of trading data analysis.

## Technical Stack & Specifications:
**Primary Language:** Python  
**Architecture:** Client-Server model  
**APIs & Protocols:** HTTP-based REST API  
**Local server running on port 8080**  
**URL endpoint:** /query  

## Key Components:

### Server (`server3.py`):
- Multithreaded HTTP Server
- Simulated market data generation
- Real-time order book management
- CSV data persistence

### Client (`client3.py`):
- REST API consumption
- Data processing for stock quotes
- Price calculation algorithms
- 500 server requests per session

### Testing (`client_test.py`):
- Unit testing framework
- Test cases for price calculations
- Error handling validation

## Features:
- Real-time market data simulation
- Price aggregation and ratio calculations
- Thread-safe operations
- Error handling for edge cases (e.g., division by zero)
- Data persistence using CSV format
