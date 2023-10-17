PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2023/05-deployment/homework
wget $PREFIX/model1.bin -P data
wget $PREFIX/dv.bin -P data
cp data/model1.bin data/model.bin