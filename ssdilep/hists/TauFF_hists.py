from histconfig import *


hist_list = []


# -------
# event
# -------
#hist_list.append(h_averageIntPerXing)
#hist_list.append(h_njets)
#hist_list.append(h_ntaus)

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
#hist_list.append(h_taulead_ntrk)
hist_list.append(h_tau_JetBDTScoreSigTrans)

# tausublead
#hist_list.append(h_tausublead_pt)

# -------
# MET
# -------
#hist_list.append(h_met_trk_et)



# ------
# FF
# ______
#hist_list.append(h_taulead_pt)

# EOF






