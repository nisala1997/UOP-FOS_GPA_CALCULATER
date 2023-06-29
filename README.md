
# calculate-gpa

A simple notebook to calculate the GPA using a csv file with the results. This implementation is based on the GPA calculation guidelines of the `Faculty of Science, University of Peradeniya (FoS, UoP).`

# Prerequisites

To run this notebook you need pandas installed. It can be installed using `pip` as follows:

```bash
pip install pandas
```

# Usage

The results are read from the `grades.csv` file. It is the comma separated file. Sample structure of the file is as follows:

```
code,course,year,sem,credits,grade
CH101,Principles of Chemistry I,2017/2018,I,3,A,
CH102,Principles of Chemistry II,2017/2018,II,3,A,
```

Run all cells to see the outputs. This notebook provides the following outputs:

- Overall GPA
- Credits per level
- Credits per year
- credits per subject
- Percentage of `A` and `A+` in `300` Level and `400` Level

# Limitations

Current implementation only covers calculating the GPA for a 4 year degree based on FoS, UoP's guidelines. Cannot be used in the casual calculation of GPA.
