# GSI
This repository provides source codes to build the model for predicting ASD-associated genes and AD-associated genes. The model is built using Random Forest.

## 1. Usage
(1) After this repository is downloaded and unzipped, go into the folder. 

(2) We have created a python script, named 'ASD_gene_pred.py', which includes all source codes to build the model for predicting ASD-associated genes and AD-associated genes.
Assuming that you are currently in the downloaded folder, just run the following command and you will be able to built a model and make predictions:

predicting ASD-associated genes
```bash
 
 python ASD_gene_pred.py ./data/signalMatrix.npz ./data/geneList.csv ./data/datasets/ASD/asd_truth_set.csv ./data/datasets/ASD/control_gene_set.csv 10
 
 ```
 
predicting AD-associated genes
```bash
 
python AD_gene_pred.py ./data/signalMatrix.npz ./data/geneList.csv ./data/datasets/AD/ADgene.txt 10
 
 ```
In the above commands, the fifth input, i.e. 10, represents the times of random sampling to build sub-models: in each random sampling,  negative genes shuffle for modeling. 5-fold CV is performed on the combined set of the positives and the sampled negatives. The sub-models built during CV are used to rank all human genes.

Note: The four modules, which are pandas, numpy, scipy and sklearn, need to be installed before running the script. 

## 2. Contact
If you have any questions, please contact us:<br>
Hong-Dong Li, hongdong@csu.edu.cn<br>
Chao Deng, deng_chao@csu.edu.cn <br>

