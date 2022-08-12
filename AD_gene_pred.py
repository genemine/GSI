"""
@author: Deng chao
"""

from sklearn.model_selection import StratifiedKFold,train_test_split
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn.metrics import roc_curve, auc, roc_auc_score,precision_recall_curve
import scipy.sparse as sp
import random,sys,os

def get_data(positiveGenePath, t, geneList):
    positive_gene=pd.read_csv(positiveGenePath,header=None)
    positive_gene=list(positive_gene[0].values)
    positive_gene=list(set(positive_gene)&set(geneList))

    res_gene=list(set(geneList)-set(positive_gene))
    random.seed(t)
    negative_gene=random.sample(res_gene,len(positive_gene))
    negative_gene.sort()
    return  positive_gene,negative_gene

def fiveFoldCV(positiveGenePath, totaltimes, geneList, signalMatrix):
    AUROC = list()
    AUPRC = list()
    evaluationRes = pd.DataFrame(index = geneList)
    for i in range(totaltimes):
        positive_gene, negative_gene = get_data(positiveGenePath, i, geneList)
        train_positive_matrix = signalMatrix.loc[positive_gene]
        train_negative_matrix = signalMatrix.loc[negative_gene]
        X = pd.concat([train_positive_matrix,train_negative_matrix],axis=0)
        X = X.values
        y = pd.DataFrame(data=len(positive_gene)*[1]+len(negative_gene)*[0])
        y = y.values.ravel()
        skfolds = StratifiedKFold(n_splits=5,shuffle=True,random_state=i)
        for train_index, test_index in skfolds.split(X, y):
            train_matrix,train_y = X[train_index],y[train_index]
            test_matrix,test_y = X[test_index],y[test_index]
            label_train = train_y
            label_test = test_y

            clf = RandomForestClassifier(n_estimators=200, n_jobs=-1,class_weight = "balanced_subsample",random_state=0)
            clf.fit(train_matrix,train_y)
            y_pred = clf.predict_proba(test_matrix)[:,1]
            AUROC_i = roc_auc_score(test_y, y_pred)
            precision, recall, _thresholds = precision_recall_curve(test_y, y_pred)
            AUPRC_i = auc(recall, precision)
            AUROC.append(AUROC_i)
            AUPRC.append(AUPRC_i)
    return AUROC,AUPRC



_, signalMatrixPath, geneListPath, positiveGenePath, totaltimes = sys.argv

# read data
geneList = pd.read_csv(geneListPath, header=None)
geneList = geneList[0].values
geneList = list(geneList)
signalMatrix = sp.load_npz(signalMatrixPath)
signalMatrix = pd.DataFrame(data = signalMatrix.A, index= geneList)
totaltimes = int(totaltimes)

AUROC,AUPRC = fiveFoldCV(positiveGenePath, totaltimes, geneList, signalMatrix)
print(np.mean(AUROC),np.mean(AUPRC))