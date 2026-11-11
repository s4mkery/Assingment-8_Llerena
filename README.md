# Assingment-8_Llerena
## Technical Implementation and Data Architecture

### Computational Framework and Library Integration

Data ingestion, structural manipulation, and exploratory pre-processing were conducted through the Python scientific stack, primarily orchestrated via **Pandas**, **NumPy**, and **Matplotlib**. Initial table structures were imported and parsed using Pandas DataFrames, wherein missing records were systematically diagnosed and pruned via subset evaluation. String sanitization operations were vectorially deployed to eliminate currency symbols (`£`) and comma delimiters from character-based monetary records, after which explicit data types were enforced through coercive numeric casting. Continuous variables were subsequently partitioned into categorical cohorts using boundary binning functions (`pd.cut`), enabling demographic segmentation across discrete cohorts.

Underlying mathematical thresholds and interval geometries were generated using NumPy. Homogeneous class boundaries across disjoint distributions were determined using linear space discretizations (`np.linspace`), while boundary bounds for open-ended categories were stabilized through infinite floating-point scalars (`np.inf`).

Visual representations were assembled through Matplotlib's object-oriented interface, relying on explicit `Figure` and `Axes` coordinate systems. Multiple independent visual layers were compiled onto unified horizontal multi-panel matrices ($1 \times 3$ grid arrays), where canvas overplotting was mitigated through alpha-transparency calibration and marker-scale adjustment. Element collision across adjacent figure boundaries was resolved through manual layout padding and inter-subplot spacing parameters (`wspace`), while axes values were mapped directly into condensed units to preserve typographic readability.

---

### Dataset Architecture and Exploratory Intent

1. 'Iris.Csv
Morphological variation and class separability were investigated using the classic Fisher Iris dataset. The primary objective assigned to this corpus was the empirical observation of multivariate trait boundaries across distinct biological taxa (*Iris setosa*, *Iris versicolor*, and *Iris virginica*). Bivariate scatter representations were constructed to contrast sepal and petal dimensions, whereby linear separability and clustering behaviors were highlighted across species.

2. Financial Credit Records (`LoanDataset - LoansDatasest.csv`)
Real-world behavioral patterns and operational anomaly management were explored using the credit applicant dataset. While classical benchmark data provides sanitized environments, this repository was approached as an exercise in confronting unpredictable and malformed information. 

### Figures Analysis

Iris.csv
1. Sepal Length vs. Petal Length (Scatter Plot)
A clear morphological segmentation across species is displayed, with Iris setosa clustered in isolation within lower boundaries, whereas versicolor and virginica occupy moderate-to-high coordinate spaces. A strong positive linear relationship between sepal length and petal length is exhibited across all three classes. Petal length can be interpreted as a decisive morphometric predictor for taxonomic classification, enabling the linear isolation of setosa alongside a distinct decision boundary between the remaining taxa.

2.Petal Width Distribution (Histogram)
A pronounced bimodal distribution is observed in petal width, characterized by a sharp density peak between 0 and 0.5 cm followed by a broader secondary cluster spanning 1.2 to 2.5 cm. An evident discontinuity is revealed around 0.7 cm, reflecting an almost complete absence of transitional measurements within the genus. This structure can be interpreted as evidence that petal width does not conform to a unified normal distribution, but rather captures an intrinsic macro-morphological divergence among distinct botanical groups.

3.Measurements Across Samples (Plot)
Biometric fluctuations across all four dimensions are recorded across the sequential sample index. Discrete upward shifts in petal dimensions (PetalLength and PetalWidth) are prominently exhibited near index thresholds 50 and 100, whereas sepal features remain bounded within a relatively stable variance envelope. These stepwise transitions can be interpreted as evidence that the underlying records are ordered by species, demonstrating that petal dimensions undergo far more decisive taxonomic leaps than sepal structures.

LoanDataset - LoansDatasest.csv
1.Loan Intent (H. Bar Chart)
The distribution of borrowing motives is dominated by non-collateralized personal necessities, led primarily by EDUCATION and MEDICAL purposes, with each exceeding 5,000 applicants. Conversely, capital investment and asset-building categories—specifically debt consolidation and home improvement—record the lowest overall demand.  This can be interpreted as an indication that the institution’s core customer base seeks unsecured credit primarily to finance urgent life events and career advancement rather than property equity enhancement.

2.Income vs. Loan Amount (Scatter Plot)
A massive concentration of borrowing activity is clustered below annual incomes of £50k and loan commitments under £10k. While borrowing capacity is nominally bounded by personal earnings, striking horizontal striations are prominently displayed at round nominal tiers (£5k, £10k, £15k, £20k, and £25k). A weak-to-moderate positive boundary relationship is exhibited, indicating that higher income acts as an eligibility ceiling rather than a direct driver of requested size. This behavior can be interpreted as evidence that applicant demand is heavily governed by psychological round-number benchmarks and lender policy product caps rather than exact continuous debt calculations.

3.Loan Amount Distribution among Age Groups (Histogram)
The overall volume of credit applications is heavily skewed toward young and early-career adults, with the 25–35 and 18–25 cohorts forming the highest frequency peaks. As loan amounts increase beyond £15k, total applicant frequency decays sharply across all demographics, though the 25–35 cohort consistently retains the highest absolute volume across nearly every interval. A pronounced right-skewed decay pattern is displayed alongside secondary spikes at round monetary increments (£10k, £15k, £20k, and £25k). This can be interpreted as reflecting standard life-cycle borrowing dynamics, where early-to-mid career individuals carry the greatest appetite for credit financing before household balance sheets mature in older brackets.
