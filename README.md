# Blizzard Employee Voluntary Salary Exploratory Data Analysis

## Project Overview
The **Blizzard Employee Voluntary Salary Analysis** project aims to explore and analyze the voluntary salary data of employees at Blizzard Entertainment. By examining this data, we seek to uncover insights into salary distributions, trends across different job titles, and the impact of various factors such as experience and location on employee compensation. The ultimate goal is to provide a comprehensive understanding of how salaries are structured within the company.

## Installation Instructions
To set up this project on your local machine, please follow these steps:

1. **Clone the repository**:
```bash
   git clone https://github.com/luisdzanetta/blizzard-employee-voluntary-salary.git
```
   
2. **Navigate to the project directory:**
```bash
    cd blizzard-employee-voluntary-salary
```

3. **Install required dependencies:**
```bash
    pip install -r requirements.txt
```

## Data Source
The data used in this project was sourced from:

https://www.kaggle.com/datasets/mexwell/blizzard-employee-voluntary-salary-info

## Project Structure
.
├── data                                # Directory containing raw dataset
├── README.md                           # Project documentation
├── exploratory-data-analysis.ipynb     # Main script .ipynb
├── exploratory-data-analysis.py        # Main script .py
├── requirements.txt                    # Project dependencies
└── LICENSE                             # Project license

## Conclusions and Limitations

### Results
**Competitive Starting Salaries:** Blizzard offers higher entry-level salaries than the general market, with a 31.67% premium at the lower end. This could reflect a strategy to attract fresh talent and ensure new engineers see Blizzard as a competitive employer from the start.

**Sustained Mid-Level Competitiveness:** For mid-level engineers, Blizzard maintains a salary advantage, particularly on the lower end (+25%). This might indicate an emphasis on retaining mid-career professionals, as this experience level often brings critical technical expertise and operational knowledge without the full cost of seniority.

**Senior Level Premiums Reflect Increased Value:** At the senior level, Blizzard’s salary range continues to outpace the market, especially at the upper limit (+28.57%). This suggests that Blizzard is willing to invest in experienced engineers who bring strategic value, likely due to the higher impact of their work on core products and teams.

**Substantial Principal Level Premiums at Lower Range:** The principal engineer role shows the largest salary difference on the lower end (+43.08%), suggesting Blizzard is competitive in attracting high-level engineering talent. The smaller discrepancy at the upper range (+8%) may indicate Blizzard aligns top-end principal salaries with the broader market, possibly reflecting an industry standard at this level.

### Limitations
Despite the conclusions drawn from the analyses, it is important to exercise caution when interpreting
and extrapolating the results, as there are some limitations:

**Sample Bias:** The data might not represent the entire Blizzard employee population.
Participation in the anonymous survey may have been skewed towards specific demographics or job roles.

**External Market Data:** Salary ranges from the tech industry were used for comparison with Blizzard's salaries. However, the accuracy of the salary data from this source is uncertain, which may affect the reliability of the analysis.

## References
1. [Wikipedia, 2024](https://en.wikipedia.org/wiki/Blizzard_Entertainment)
2. [Time, 2020](https://time.com/5875371/blizzard-wage-disaparities/)
3. [Bloomberg, 2020](https://www.bloomberg.com/news/articles/2020-08-03/blizzard-workers-share-salaries-in-revolt-over-wage-disparities)
4. [OpenInto, 2020](https://www.openintro.org/data/index.php?data=blizzard_salary)
5. [Kaggle, 2024](https://www.kaggle.com/datasets/mexwell/blizzard-employee-voluntary-salary-info)
6. [Ellow, 2024](https://ellow.io/contract-work-vs-full-time-employment/)
7. [IT Career Finder, 2023](https://www.itcareerfinder.com/brain-food/it-salaries/computer-software-engineer-salary-range.html)

## License
This project is licensed under the MIT License. Please refer to the LICENSE file for details.
The dataset is subject to its own licensing agreements; please review those before use.