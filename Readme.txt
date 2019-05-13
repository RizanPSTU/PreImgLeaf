https://github.com/wkentaro/labelme


D:
cd D:\RizGit\PreImgLeaf
conda activate labelme
# It generates:
#   - data_dataset_voc/JPEGImages
#   - data_dataset_voc/SegmentationClass
#   - data_dataset_voc/SegmentationClassVisualization

Evn agey active korte hoibo
conda activate labelme
python labelme2voc.py data_annotated data_dataset_voc --labels labels.txt