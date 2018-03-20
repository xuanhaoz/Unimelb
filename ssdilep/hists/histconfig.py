from hists import *


"""
This contains the histogram
configuration. Do not create
other config files !!!
"""


# -------
# event
# -------
h_averageIntPerXing = Hist1D( hname  = "h_averageIntPerXing",
                              xtitle = "averageInteractionsPerCrossing",
                              ytitle = "Events", 
                              nbins  = 50,
                              xmin   = -0.5,
                              xmax   = 49.5,
                              dir    = "event",
                              vexpr  = "self.chain.averageInteractionsPerCrossing",
                            )

h_actualIntPerXing = Hist1D( hname  = "h_actualIntPerXing",
                              xtitle = "actualInteractionsPerCrossing",
                              ytitle = "Events", 
                              nbins  = 50,
                              xmin   = -0.5,
                              xmax   = 49.5,
                              dir    = "event",
                              vexpr  = "self.chain.actualInteractionsPerCrossing",
                            )

h_correct_mu = Hist1D( hname  = "h_correct_mu",
                              xtitle = "<#mu_{corr}>",
                              ytitle = "Events", 
                              nbins  = 50,
                              xmin   = -0.5,
                              xmax   = 49.5,
                              dir    = "event",
                              vexpr  = "self.chain.correct_mu",
                            )

h_NPV = Hist1D( hname  = "h_NPV",
                              xtitle = "NPV",
                              ytitle = "Events", 
                              nbins  = 35,
                              xmin   = 0.,
                              xmax   = 35.0,
                              dir    = "event",
                              vexpr  = "self.chain.NPV",
                            )

h_nmuons = Hist1D( hname  = "h_nmuons",
                              xtitle = "N_{#mu}",
                              ytitle = "Events", 
                              nbins  = 8,
                              xmin   = 0,
                              xmax   = 8,
                              dir    = "event",
                              vexpr  = "self.chain.nmuon",
                            )

h_nelectrons = Hist1D( hname  = "h_nelectrons",
                              xtitle = "N_{e}",
                              ytitle = "Events", 
                              nbins  = 8,
                              xmin   = 0,
                              xmax   = 8,
                              dir    = "event",
                              vexpr  = "self.chain.nel",
                            )

h_njets = Hist1D( hname  = "h_njets",
                              xtitle = "N_{jet}",
                              ytitle = "Events", 
                              nbins  = 8,
                              xmin   = 0,
                              xmax   = 8,
                              dir    = "event",
                              vexpr  = "self.chain.njet",
                            )

h_muons_chargeprod  = Hist1D( hname  = "h_muons_chargeprod",
                              xtitle = "q(#mu_{lead}) #timesq (#mu_{sublead})",
                              ytitle = "Events", 
                              nbins  = 4,
                              xmin   = -2,
                              xmax   = 2,
                              dir    = "event",
                              vexpr  = "self.store['charge_product']",
                            )

h_muons_dphi  = Hist1D( hname  = "h_muons_dphi",
                              xtitle = "#Delta#phi(#mu_{lead},#mu_{sublead})",
                              ytitle = "Events", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "event",
                              vexpr  = "self.store['muons_dphi']",
                            )

h_muons_deta  = Hist1D( hname  = "h_muons_deta",
                              xtitle = "#Delta#eta(#mu_{lead},#mu_{sublead})",
                              ytitle = "Events", 
                              nbins  = 50,
                              xmin   = -2.5,
                              xmax   = 2.5,
                              dir    = "event",
                              vexpr  = "self.store['muons_deta']",
                            )

h_muons_mVis  = Hist1D( hname  = "h_muons_mVis",
                              xtitle = "m_{vis}(#mu_{lead},#mu_{sublead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.,
                              dir    = "event",
                              vexpr  = "self.store['mVis']/GeV",
                            )

h_muons_pTH  = Hist1D( hname  = "h_muons_pTH",
                              xtitle = "p_T(SS_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.,
                              dir    = "event",
                              vexpr  = "self.store['muons_pTH']/GeV",
                              )

h_muons_dR  = Hist1D( hname  = "h_muons_dR",
                              xtitle = "#DeltaR(SS_{lead})",
                              ytitle = "Events", 
                              nbins  = 60,
                              xmin   = 0.,
                              xmax   = 6.,
                              dir    = "event",
                              vexpr  = "self.store['muons_dR']",
                              )

h_muons_mTtot  = Hist1D( hname  = "h_muons_mTtot",
                              xtitle = "m^{tot}_{T}(#mu_{lead},#mu_{sublead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.,
                              dir    = "event",
                              vexpr  = "self.store['mTtot']/GeV",
                            )

h_mujet_dphi  = Hist1D( hname  = "h_mujet_dphi",
                              xtitle = "#Delta#phi(#mu_{lead},jet_{lead})",
                              ytitle = "Events", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "event",
                              vexpr  = "self.store['mujet_dphi']",
                            )

h_mujet_scdphi  = Hist1D( hname  = "h_mujet_scdphi",
                              xtitle = "#Sigma cos#Delta#phi(#mu,jet)",
                              ytitle = "Events", 
                              nbins  = 400,
                              xmin   = -2.,
                              xmax   = 2.,
                              dir    = "event",
                              vexpr  = "self.store['mujet_scdphi']",
                            )

h_taujet_dphi  = Hist1D( hname  = "h_taujet_dphi",
                              xtitle = "#Delta#phi(#tau_{lead},jet_{lead})",
                              ytitle = "Events", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "event",
                              vexpr  = "self.store['taujet_dphi']",
                              )

h_taujet_scdphi  = Hist1D( hname  = "h_taujet_scdphi",
                           xtitle = "#Sigma cos#Delta#phi(#tau,jet)",
                           ytitle = "Events", 
                           nbins  = 400,
                           xmin   = -2.,
                           xmax   = 2.,
                           dir    = "event",
                           vexpr  = "self.store['taujet_scdphi']",
                           )

h_taujet_ptratio  = Hist1D( hname  = "h_taujet_ptratio",
                            xtitle = "p_{T}(#tau_{lead})/p_{T}(jet_{lead})",
                            ytitle = "Events", 
                            nbins  = 64,
                            xmin   = 0.,
                            xmax   = 2.,
                            dir    = "event",
                            vexpr  = "self.store['taujet_ptratio']",
                            )
h_tau_JetBDTScoreSigTrans  = Hist1D( hname  = "h_tau_JetBDTScoreSigTrans",
				     xtitle = "#tau_{JetBDTScore}",
				     ytitle = "Events",
				     nbins  = 64,
				     xmin   = 0.,
				     xmax   = 1.,
				     dir    = "taus",
				     vexpr  = "self.store['taus'][0].JetBDTScoreSigTrans"
				     )

h_ntaus = Hist1D( hname  = "h_ntaus",
                              xtitle = "N_{#tau}",
                              ytitle = "Events",
                              nbins  = 8,
                              xmin   = 0,
                              xmax   = 8,
                              dir    = "event",
                              vexpr  = "self.chain.ntau",
                            )

# -------
# jets
# -------
h_jetlead_pt = Hist1D( hname  = "h_jetlead_pt",
                              xtitle = "p_{T}(jet_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "jets",
                              vexpr  = "self.store['jets'][0].tlv.Pt()/GeV",
                            )

h_jetlead_eta = Hist1D( hname  = "h_jetlead_eta",
                              xtitle = "#eta(jet_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 50,
                              xmin   = -2.5,
                              xmax   = 2.5,
                              dir    = "jets",
                              vexpr  = "self.store['jets'][0].tlv.Eta()",
                            )

h_jetlead_phi = Hist1D( hname  = "h_jetlead_phi",
                              xtitle = "#phi(jet_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "jets",
                              vexpr  = "self.store['jets'][0].tlv.Phi()",
                            )

# -------
# taus
# -------

# taulead
# ------
h_taulead_pt = Hist1D( hname  = "h_taulead_pt",
                              xtitle = "p_{T}(#tau_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "taus",
                              vexpr  = "self.store['taus'][0].tlv.Pt() / GeV",
                            )

h_taulead_eta = Hist1D( hname  = "h_taulead_eta",
                              xtitle = "#eta(#tau_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 50,
                              xmin   = -2.5,
                              xmax   = 2.5,
                              dir    = "taus",
                              vexpr  = "self.store['taus'][0].tlv.Eta()",
                            )

h_taulead_phi = Hist1D( hname  = "h_taulead_phi",
                              xtitle = "#phi(#tau_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "taus",
                              vexpr  = "self.store['taus'][0].tlv.Phi()",
                            )

h_taulead_ntrk = Hist1D( hname  = "h_taulead_ntrk",
                              xtitle = "ntrak(#tau_{lead})",
                              ytitle = "Events / (0.1)",
                              nbins  = 4,
                              xmin   = 0,
                              xmax   = 4,
                              dir    = "taus",
                              vexpr  = "self.store['taus'][0].ntrk",
                            )

h_tausublead_pt = Hist1D( hname  = "h_tausublead_pt",
                              xtitle = "p_{T}(#tau_{sublead}) [GeV]",
                              ytitle = "Events / (1 GeV)",
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "taus",
                              vexpr  = "self.store['taus'][1].tlv.Pt() / GeV",
                            )

# -------
# muons
# -------

# mulead
# ------
h_mulead_pt = Hist1D( hname  = "h_mulead_pt",
                              xtitle = "p_{T}(#mu_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].tlv.Pt() / GeV",
                            )

h_mulead_eta = Hist1D( hname  = "h_mulead_eta",
                              xtitle = "#eta(#mu_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 50,
                              xmin   = -2.5,
                              xmax   = 2.5,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].tlv.Eta()",
                            )

h_mulead_phi = Hist1D( hname  = "h_mulead_phi",
                              xtitle = "#phi(#mu_{lead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].tlv.Phi()",
                            )

h_mulead_trkd0 = Hist1D( hname  = "h_mulead_trkd0",
                              xtitle = "d^{trk}_{0}(#mu_{lead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 80,
                              xmin   = -0.4,
                              xmax   = 0.4,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].trkd0",
                            )

h_mulead_trkd0sig = Hist1D( hname  = "h_mulead_trkd0sig",
                              xtitle = "d^{trk}_{0} / #sigma(d^{trk}_{0}) (#mu_{lead})",
                              ytitle = "Events / (0.01)", 
                              nbins  = 100,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].trkd0sig",
                            )

h_mulead_trkz0 = Hist1D( hname  = "h_mulead_trkz0",
                              xtitle = "z^{trk}_{0}(#mu_{lead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 40,
                              xmin   = -2,
                              xmax   = 2,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].trkz0",
                            )

h_mulead_trkz0sintheta  = Hist1D( hname  = "h_mulead_trkz0sintheta",
                              xtitle = "z^{trk}_{0}sin#theta(#mu_{lead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 200,
                              xmin   = -1,
                              xmax   = 1,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].trkz0sintheta",
                            )

h_mulead_ptvarcone30  = Hist1D( hname  = "h_mulead_ptvarcone30",
                              xtitle = "ptvarcone30/p_{T}(#mu_{lead})",
                              ytitle = "Events / (0.001)", 
                              nbins  = 10000,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].ptvarcone30 / self.store['muons'][0].tlv.Pt()",
                            )

# musublead
# ---------
h_musublead_pt = Hist1D( hname  = "h_musublead_pt",
                              xtitle = "p_{T}(#mu_{sublead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].tlv.Pt() / GeV",
                            )

h_musublead_eta = Hist1D( hname  = "h_musublead_eta",
                              xtitle = "#eta(#mu_{sublead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 50,
                              xmin   = -2.5,
                              xmax   = 2.5,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].tlv.Eta()",
                            )

h_musublead_phi = Hist1D( hname  = "h_musublead_phi",
                              xtitle = "#phi(#mu_{sublead})",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].tlv.Phi()",
                            )

h_musublead_trkd0 = Hist1D( hname  = "h_musublead_trkd0",
                              xtitle = "d^{trk}_{0}(#mu_{sublead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 80,
                              xmin   = -0.4,
                              xmax   = 0.4,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].trkd0",
                            )

h_musublead_trkd0sig = Hist1D( hname  = "h_musublead_trkd0sig",
                              xtitle = "d^{trk}_{0} / #sigma(d^{trk}_{0}) (#mu_{sublead})",
                              ytitle = "Events / (0.01)", 
                              nbins  = 100,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].trkd0sig",
                            )

h_musublead_trkz0 = Hist1D( hname  = "h_musublead_trkz0",
                              xtitle = "z^{trk}_{0}(#mu_{sublead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 40,
                              xmin   = -2,
                              xmax   = 2,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].trkz0",
                            )

h_musublead_trkz0sintheta  = Hist1D( hname  = "h_musublead_trkz0sintheta",
                              xtitle = "z^{trk}_{0}sin#theta(#mu_{sublead}) [mm]",
                              ytitle = "Events / (0.01)", 
                              nbins  = 200,
                              xmin   = -1,
                              xmax   = 1,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].trkz0sintheta",
                            )

h_musublead_ptvarcone30  = Hist1D( hname  = "h_musublead_ptvarcone30",
                              xtitle = "ptvarcone30/p_{T}(#mu_{sublead})",
                              ytitle = "Events / (0.001)", 
                              nbins  = 10000,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][1].ptvarcone30 / self.store['muons'][1].tlv.Pt()",
                            )

# -------------
# tag and probe
# -------------
h_tag_pt = Hist1D( hname  = "h_tag_pt",
                              xtitle = "p_{T}(#mu_{tag}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['tag'].tlv.Pt() / GeV",
                            )

h_probe_pt = Hist1D( hname  = "h_probe_pt",
                              xtitle = "p_{T}(#mu_{probe}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['probe'].tlv.Pt() / GeV",
                            )

h_probe_ptiso = Hist1D( hname  = "h_probe_ptiso",
                              xtitle = "p_{T}(#mu_{probe}) + ptvarcone30 [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 1000,
                              xmin   = 0.0,
                              xmax   = 1000.0,
                              dir    = "muons",
                              vexpr  = "( self.store['probe'].tlv.Pt() + self.store['probe'].ptvarcone30 ) / GeV",
                            )

h_probe_ujet_pt = Hist1D( hname  = "h_probe_ujet_pt",
                              xtitle = "p_{T}(#mu_{probe} underlying jet) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2100,
                              xmin   = -100.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['probe_ujet_pt']",
                            )

h_tag_ptvarcone30  = Hist1D( hname  = "h_tag_ptvarcone30",
                              xtitle = "ptvarcone30/p_{T}(#mu_{tag})",
                              ytitle = "Events / (0.001)", 
                              nbins  = 10000,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['tag'].ptvarcone30 / self.store['tag'].tlv.Pt()",
                            )
h_probe_ptvarcone30  = Hist1D( hname  = "h_probe_ptvarcone30",
                              xtitle = "ptvarcone30/p_{T}(#mu_{probe})",
                              ytitle = "Events / (0.001)", 
                              nbins  = 10000,
                              xmin   = 0.,
                              xmax   = 10.,
                              dir    = "muons",
                              vexpr  = "self.store['probe'].ptvarcone30 / self.store['probe'].tlv.Pt()",
                            )

# -------
# MET
# -------
"""
h_met_clus_et  = Hist1D( hname  = "h_met_clus_et",
                              xtitle = "E^{miss}_{T}(clus) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.store['met_clus'].tlv.Pt()/GeV",
                            )

h_met_clus_phi  = Hist1D( hname  = "h_met_clus_phi",
                              xtitle = "#phi(E^{miss}_{T}(clus))",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "met",
                              vexpr  = "self.store['met_clus'].tlv.Phi()",
                            )
"""
h_met_trk_et  = Hist1D( hname  = "h_met_trk_et",
                              xtitle = "E^{miss}_{T}(trk) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.store['met_trk'].tlv.Pt()/GeV",
                            )

h_met_trk_phi  = Hist1D( hname  = "h_met_trk_phi",
                              xtitle = "#phi(E^{miss}_{T}(trk))",
                              ytitle = "Events / (0.1)", 
                              nbins  = 64,
                              xmin   = -3.2,
                              xmax   = 3.2,
                              dir    = "met",
                              vexpr  = "self.store['met_trk'].tlv.Phi()",
                            )
"""
h_met_clus_sumet  = Hist1D( hname  = "h_met_clus_sumet",
                              xtitle = "#Sigma E_{T}(clus) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.store['met_clus'].sumet/GeV",
                          )
"""
h_met_trk_sumet  = Hist1D( hname  = "h_met_trk_sumet",
                              xtitle = "#Sigma E_{T}(trk) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.store['met_trk'].sumet/GeV",
                          )


# --------
# 2D hists
# --------
h_mulead_ptiso_jetlead_pt  = Hist2D( hname      = "h_mulead_ptiso_jetlead_pt",
                              xtitle  = "p_{T}(#mu_{lead}) + ptvarcone30 [GeV]",
                              ytitle  = "p_{T}(jet_{lead}) [GeV]", 
                              nbinsx  = 1000,
                              xmin    = 0.,
                              xmax    = 1000.,
                              nbinsy  = 1000,
                              ymin    = 0.,
                              ymax    = 1000.,
                              dir     = "event",
                              vexpr   = "( self.store['muons'][0].tlv.Pt() + self.store['muons'][0].ptvarcone30 ) / GeV , self.store['jets'][0].tlv.Pt() / GeV",
                          )


h_mulead_pt_mulead_iso  = Hist2D( hname      = "h_mulead_pt_mulead_iso",
                              xtitle  = "p_{T}(#mu_{lead}) [GeV]",
                              ytitle  = "ptvarcone30(#mu_{lead}) [GeV]", 
                              nbinsx  = 1000,
                              xmin    = 0.,
                              xmax    = 1000.,
                              nbinsy  = 1000,
                              ymin    = 0.,
                              ymax    = 1000.,
                              dir     = "event",
                              vexpr   = "self.store['muons'][0].tlv.Pt() / GeV , self.store['muons'][0].ptvarcone30 / GeV",
                          )

h_mulead_pt_jetlead_pt  = Hist2D( hname      = "h_mulead_pt_jetlead_pt",
                              xtitle  = "p_{T}(#mu_{lead}) [GeV]",
                              ytitle  = "p_{T}(jet_{lead}) [GeV]", 
                              nbinsx  = 1000,
                              xmin    = 0.,
                              xmax    = 1000.,
                              nbinsy  = 1000,
                              ymin    = 0.,
                              ymax    = 1000.,
                              dir     = "event",
                              vexpr   = " self.store['muons'][0].tlv.Pt() / GeV , self.store['jets'][0].tlv.Pt() / GeV",
                          )

# EOF
