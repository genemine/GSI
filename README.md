# GSI
This repository provides source codes to build the model for predicting AD-associated genes and to make predictions. The model is built using Ridge regression. The feature vectors of training and test genes are extracted from the ADBrainNexus network, which is available at https://zenodo.org/record/5594149.

## 1. Usage
(1) After this repository is downloaded and unzipped, go into the folder. 

(2) We have created a python script, named 'AD_gene_pred.py', which includes all source codes (i) to build the model for predicting AD-associated genes and (ii) to make predictions.
Assuming that you are currently in the downloaded folder, just run the following command and you will be able to built a model and make predictions:

```bash
 
 python AD_gene_pred.py output data/integrated_feature.txt  10
 
 ```
In the above commands, the third input, i.e. 10, represents the times of random sampling to build sub-models: in each random sampling,  negative genes shuffle for modeling. 5-fold CV is performed on the combined set of the positives and the sampled negatives. The sub-models built during CV are used to rank all human genes.

Note: The three modules, which are pandas, numpy and sklearn, need to be installed before running the script. 

(3) After running the script, the prediction results will be saved to the file named 'prediction.txt', in which each row contains a gene and the predicted regression value that measures the level for the gene to be associated with AD.

## 2. Contact
If you have any questions, please contact us:<br>
ChaoDeng, deng_chao@csu.edu.cn <br>
Jianxin Wang, jxwang@mail.csu.edu.cn<br>
