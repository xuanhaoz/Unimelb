from histconfig import *


hist_list = []


# -------
# event
# -------
hist_list.append(h_averageIntPerXing)
#hist_list.append(h_NPV)
#hist_list.append(h_nmuons)
#hist_list.append(h_nelectrons)
hist_list.append(h_njets)

hist_list.append(h_taujet_dphi)
hist_list.append(h_taujet_ptratio)


# -------
# jets
# -------

# jetlead
hist_list.append(h_jetlead_pt)
hist_list.append(h_jetlead_eta)
hist_list.append(h_jetlead_phi)

# -------
# taus
# -------

# taulead
hist_list.append(h_taulead_pt)
hist_list.append(h_taulead_eta)
hist_list.append(h_taulead_phi)

# -------
# muons
# -------

# mulead
#hist_list.append(h_mulead_pt)
#hist_list.append(h_mulead_eta)
#hist_list.append(h_mulead_phi)
#hist_list.append(h_mulead_trkd0)
#hist_list.append(h_mulead_trkd0sig)
#hist_list.append(h_mulead_trkz0)
#hist_list.append(h_mulead_trkz0sintheta)
#hist_list.append(h_mulead_ptvarcone30)


# -------
# MET
# -------
#hist_list.append(h_met_clus_et)
#hist_list.append(h_met_clus_phi)
hist_list.append(h_met_trk_et)
#hist_list.append(h_met_trk_phi)
#hist_list.append(h_met_clus_sumet)
#hist_list.append(h_met_trk_sumet)

# -------
# jets
# -------
#hist_list.append(h_jetlead_pt)
#hist_list.append(h_mujet_dphi)


# EOF






