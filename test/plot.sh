#!bin/bash

# ------------
# FAKE FACTORS
# ------------

#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_NUM_F1" --lab="NUM" --tag="s1" --icut="4" --input="/coepp/cephfs/mel/xuanhaoz/SSDiLep/test" --output="./plots" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_DEN_F1" --lab="DEN" --tag="s1" --icut="4" --input="/coepp/cephfs/mel/xuanhaoz/SSDiLep/test" --output="./plots" --makeplot=True --fakest="Subtraction"

python ../ssdilep/scripts/merge.py --var="tausublead_pt" --reg="FAKES_NUM_F1" --lab="NUM" --tag="s1" --icut="4" --input="/coepp/cephfs/mel/xuanhaoz/SSDiLep/jobs/SUSY11Data.v3.r1/Data/TwoSS" --output="./" --makeplot=True --fakest="Subtraction"
python ../ssdilep/scripts/merge.py --var="tausublead_pt" --reg="FAKES_DEN_F1" --lab="DEN" --tag="s1" --icut="4" --input="/coepp/cephfs/mel/xuanhaoz/SSDiLep/jobs/SUSY11Data.v3.r1/Data/TwoSS" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F1" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F1" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F2" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F2" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F3" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F3" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F4" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F4" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F5" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F5" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F6" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F6" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F7" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F7" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F8" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F8" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"



# -------------
# TAG AND PROBE
# -------------
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeTight_R1" --lab="FakeFilter_SS" --tag="fakefilter_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeTight_R2" --lab="AntiTruth_SS" --tag="antitruth_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeTight_R3" --lab="FakeFilter_OS" --tag="fakefilter_os" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeTight_R4" --lab="AntiTruth_OS" --tag="antitruth_os" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeLoose_R1" --lab="FakeFilter_SS" --tag="fakefilter_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeLoose_R2" --lab="AntiTruth_SS" --tag="antitruth_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeLoose_R3" --lab="FakeFilter_OS" --tag="fakefilter_os" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_pt" --reg="ProbeLoose_R4" --lab="AntiTruth_OS" --tag="antitruth_os" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="probe_ujet_pt" --reg="ProbeLoose_F1" --lab="TruthFilter_SS" --tag="truthfilter_ss" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist30JanV2TP" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_ujet_pt" --reg="ProbeLoose_F2" --lab="TruthFilter_OS" --tag="truthfilter_os" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=True --fakest="Subtraction"

# ----------
# VALIDATION
# ----------
#python ../ssdilep/scripts/merge.py --var="muons_mVis" --reg="FAKESVR1_MAINREG" --lab="VR" --tag="lowM" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVRNewFF" --output="./" --makeplot=True --fakest="ReducedRegions"
#python ../ssdilep/scripts/merge.py --var="muons_mVis" --reg="FAKESVR1_MAINREG" --lab="VR" --tag="v2" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2VR" --output="./" --makeplot=True --fakest="ReducedRegions"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR1_MAINREG" --lab="VR" --tag="set3_lowM" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVRSliceSet3" --output="./" --makeplot=True --fakest="ReducedRegions"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR2_MAINREG" --lab="VR" --tag="set3_highMET" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVRSliceSet3" --output="./" --makeplot=True --fakest="ReducedRegions"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR3_MAINREG" --lab="VR" --tag="set3_bveto" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVRSliceSet3" --output="./" --makeplot=True --fakest="ReducedRegions"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR1_MAINREG" --lab="VR" --tag="full" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistNoteVR1" --output="./" --makeplot=True --fakest="FullRegions"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR3_MAINREG" --lab="VR" --tag="full" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistNewFFVR3" --output="./" --makeplot=True --fakest="FullRegions"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKESVR3_MAINREG" --lab="VR" --tag="full" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistAllVR3" --output="./" --makeplot=True --fakest="FullRegions"

#python ../ssdilep/scripts/merge.py --var="NPV" --reg="FAKESVR1_LTT" --lab="VR" --tag="test" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistNoteVR1" --output="./" --makeplot=True --fakest="Subtraction"



# ----
# MISC
# ----

#python ../ssdilep/scripts/merge.py --var="mulead_ptvarcone30" --reg="FAKES_DEN_F1" --lab="denominator" --tag="comp" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFull21JanFF" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_ptvarcone30" --reg="FAKES_DEN_F1" --lab="denominator" --tag="compWeighted" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist23JanFF" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="probe_ptvarcone30" --reg="ProbeLoose_F1" --lab="TruthFilter_SS" --tag="compV2_truthfilter_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV2TP" --output="./" --makeplot=False --fakest="Subtraction" 
#python ../ssdilep/scripts/merge.py --var="probe_ptvarcone30" --reg="ProbeLoose_F1" --lab="TruthFilter_SS" --tag="compV1_truthfilter_ss" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist21JanV1TP" --output="./" --makeplot=False --fakest="Subtraction" 



