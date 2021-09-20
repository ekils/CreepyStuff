# Only need to set this path: 
export DATAPATH='./'

# Copy source data to step1: 
cp -a $DATAPATH'src_data/.' './step1_data'
# rm -R $DATAPATH'src_data/'*
# step1:
python3 step1_change_name.py --path $DATAPATH

# # Copy source data to step2: 
cp -a $DATAPATH'step1_data/.' './step2_data'
rm -R $DATAPATH'step1_data'
# step2:
mkdir ./step2_data/img
mkdir ./step2_data/gt
mkdir ./step3_data
python3 step2_totxt.py --txt_folder ./step3_data/gt/ --img_folder ./step3_data/img/

# Copy source data to step3:
rm -R $DATAPATH'step2_data'
# step3:  Split data into train, test dataset
python3 step3_split_data.py --path $DATAPATH  # Modify the path according to your situation
# rm -R $DATAPATH'step3_data'