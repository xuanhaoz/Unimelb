# encoding: utf-8
'''
vars_mumu.py
description:
variables for the mumu channel
'''

## modules
from var import Var

## Cutflows
## ---------------------------------------
cutflow_weighted          = Var(name = 'cutflow_weighted_mumu',log=False)
cutflow                   = Var(name = 'cutflow_mumu',log=False)
cutflow_weighted_mu_pairs = Var(name = 'cutflow_weighted_mumu_mu_pairs',log=False)
cutflow_mu_pairs          = Var(name = 'cutflow_mumu_mu_pairs',log=False)
cutflow_presel            = Var(name = 'cutflow_presel',log=False)
cutflow_weighted_presel   = Var(name = 'cutflow_weighted_presel',log=False)
cutflow_ZCR               = Var(name = 'cutflow_ZCR',log=False)
cutflow_weighted_ZCR      = Var(name = 'cutflow_weighted_ZCR',log=False)



## Event variables
## ---------------------------------------
averageIntPerXing = Var(name = 'averageIntPerXing',
              path  = 'event',
              xmin  = 0,
              xmax  = 45,
              log   = False,
              )

actualIntPerXing = Var(name = 'actualIntPerXing',
              path  = 'event',
              xmin  = 0,
              xmax  = 45,
              log   = False,
              )

NPV = Var(name = 'NPV',
              path  = 'event',
              xmin  = 0,
              xmax  = 35.,
              log   = False,
              )

nmuons = Var(name = 'nmuons',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

nelectrons = Var(name = 'nelectrons',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

njets = Var(name = 'njets',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

ntaus = Var(name = 'ntaus',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

nmuonpairs = Var(name = 'nmuonpairs',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

mujet_dphi = Var(name = 'mujet_dphi',
              path    = 'event',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = True,
              )

scdphi = Var(name     = 'scdphi',
              path    = 'event',
              xmin    = -2.,
              xmax    = 2.,
              rebin   = 4,
              log     = False,
              )

muons_mVis = Var(name     = 'muons_mVis',
              path    = 'event',
              #xmin    = 0.,
              xmin    = 0.,
              #xmax    = 800.,
              xmax    = 500.,
              rebin   = 20,
              #rebin   = 1,
              log     = False,
              )

muons_mTtot = Var(name     = 'muons_mTtot',
              path    = 'event',
              #xmin    = 0.,
              xmin    = 0.,
              #xmax    = 800.,
              xmax    = 500.,
              rebin   = 40,
              #rebin   = 1,
              log     = False,
              )

muons_dphi = Var(name = 'muons_dphi',
              path    = 'event',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

muons_deta = Var(name = 'muons_deta',
              path    = 'event',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin  = 4,
              log     = False,
              )

muons_chargeprod = Var(name = 'muons_chargeprod',
              path    = 'event',
              xmin    = -2,
              xmax    = 2,
              #rebin  = 10,
              log     = False,
              )

muons_dR = Var(name = 'muons_dR',
              path    = 'event',
              xmin    = 0,
              xmax    = 6,
              rebin   = 2,
              log     = False,
              )

muons_pTH = Var(name = 'muons_pTH',
              path    = 'event',
              xmin    = 0,
              xmax    = 600,
              rebin   = 20,
              log     = False,
              )

## Single muon variables
## ---------------------------------------
mulead_pt = Var(name = 'mulead_pt',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 600.,
              #xmax   = 400.,
              #rebin  = 20,
              rebin  = 5,
              log    = True,
              )

musublead_pt = Var(name = 'musublead_pt',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 400.,
              #xmax   = 120.,
              rebin  = 20,
              #rebin  = 5,
              log    = False,
              )

mulead_eta = Var(name = 'mulead_eta',
              path    = 'muons',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )

musublead_eta = Var(name = 'musublead_eta',
              path    = 'muons',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )

mulead_phi = Var(name = 'mulead_phi',
              path    = 'muons',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

musublead_phi = Var(name = 'musublead_phi',
              path    = 'muons',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

mulead_trkd0 = Var(name = 'mulead_trkd0',
              path    = 'muons',
              xmin    = -0.2,
              xmax    = 0.2,
              rebin  = 1,
              log     = False,
              )

musublead_trkd0 = Var(name = 'musublead_trkd0',
              path    = 'muons',
              xmin    = -0.2,
              xmax    = 0.2,
              rebin   = 1,
              log     = False,
              )

mulead_trkd0sig = Var(name = 'mulead_trkd0sig',
              path    = 'muons',
              xmin    = 0.,
              xmax    = 10.,
              rebin   = 3,
              log     = False,
              )

musublead_trkd0sig = Var(name = 'musublead_trkd0sig',
              path    = 'muons',
              xmin    = 0.,
              xmax    = 10.,
              rebin   = 3,
              log     = False,
              )

mulead_trkz0 = Var(name = 'mulead_trkz0',
              path    = 'muons',
              xmin    = -1.0,
              xmax    = 1.0,
              rebin   = 1,
              log     = False,
              )

musublead_trkz0 = Var(name = 'musublead_trkz0',
              path    = 'muons',
              xmin    = -1.0,
              xmax    = 1.0,
              rebin   = 1,
              log     = False,
              )

mulead_trkz0sintheta = Var(name = 'mulead_trkz0sintheta',
              path    = 'muons',
              xmin    = -0.7,
              xmax    = 0.7,
              rebin   = 2,
              log     = False,
              )

musublead_trkz0sintheta = Var(name = 'musublead_trkz0sintheta',
              path    = 'muons',
              xmin    = -0.7,
              xmax    = 0.7,
              rebin   = 2,
              log     = False,
              )

musublead_ptvarcone30 = Var(name = 'musublead_ptvarcone30',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )

# isolation
mulead_topoetcone20 = Var(name = 'mulead_topoetcone20',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )

mulead_topoetcone30 = Var(name = 'mulead_topoetcone30',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_topoetcone40 = Var(name = 'mulead_topoetcone40',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_ptvarcone20 = Var(name = 'mulead_ptvarcone20',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = True,
              )
mulead_ptvarcone30 = Var(name = 'mulead_ptvarcone30',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_ptvarcone40 = Var(name = 'mulead_ptvarcone40',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_ptcone20 = Var(name = 'mulead_ptcone20',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_ptcone30 = Var(name = 'mulead_ptcone30',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )
mulead_ptcone40 = Var(name = 'mulead_ptcone40',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )


## tag and probe
## -------------------------------------
tag_pt = Var(name = 'tag_pt',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 400.,
              rebin  = 20,
              log    = False,
              )
probe_pt = Var(name = 'probe_pt',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 400.,
              rebin  = 20,
              log    = False,
              )
probe_ptiso = Var(name = 'probe_ptiso',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 500.,
              rebin  = 10,
              log    = False,
              )
probe_ujet_pt = Var(name = 'probe_ujet_pt',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 500.,
              rebin  = 10,
              log    = False,
              )
probe_ptvarcone30 = Var(name = 'probe_ptvarcone30',
              path   = 'muons',
              xmin   = 0.,
              xmax   = 1.2,
              rebin  = 20,
              log    = False,
              )

# -----------------------------------------------------
# jets
jetlead_pt = Var(name = 'jetlead_pt',
              path    = 'jets',
              xmin    = 0.,
              xmax    = 600.,
              rebin   = 5,
              log     = False,
              )

jetlead_phi = Var(name = 'jetlead_phi',
              path    = 'jets',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 2,
              log     = False,
              )

jetlead_eta = Var(name = 'jetlead_eta',
              path    = 'jets',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 2,
              log     = False,
              )


# taus
taulead_pt = Var(name = 'taulead_pt',
              path    = 'taus',
              xmin    = 0.,
              xmax    = 600.,
              rebin   = 5,
              log     = False,
              )

tausublead_pt = Var(name = 'tausublead_pt',
              path    = 'taus',
              xmin    = 0.,
              xmax    = 600.,
              rebin   = 5,
              log     = False,
              )

taulead_phi = Var(name = 'taulead_phi',
              path    = 'taus',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 2,
              log     = False,
              )

taulead_eta = Var(name = 'taulead_eta',
              path    = 'taus',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 2,
              log     = False,
              )

taulead_ntrk = Var(name = 'taulead_ntrk',
              path    = 'taus',
              xmin    = 0.,
              xmax    = 4,
              rebin   = 1 ,
              log     = False,
              )

tau_JetBDTScoreSigTrans = Var(name = 'tau_JetBDTScoreSigTrans',
			  path	= 'taus',
			  xmin	= 0.,
			  xmax	= 1.,
			  rebin	= 5,
			  log	= False,
			 )

# taujet
taujet_ptratio = Var(name = 'taujet_ptratio',
		path	= 'event',
		xmin	= 0.,
		xmax	= 2.,
		rebin	= 2,
		log	= False,
		)

taujet_dphi = Var(name = 'taujet_dphi',
                path    = 'event',
                xmin    = -3.2,
                xmax    = 3.2,
                rebin   = 5,
                log     = False,
                )


## MET variables
## ---------------------------------------
met_clus_et = Var(name = 'met_clus_et',
              path    = 'met',
              xmin    = 0.,
              xmax    = 300.,
              rebin   = 10,
              log     = True,
              )

met_clus_phi = Var(name = 'met_clus_phi',
              path    = 'met',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

met_trk_et = Var(name = 'met_trk_et',
              path    = 'met',
              xmin    = 0.,
              xmax    = 300.,
              rebin   = 10,
              log     = True,
              )

met_trk_phi = Var(name = 'met_trk_phi',
              path    = 'met',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 2,
              log     = False,
              )

met_clus_sumet = Var(name = 'met_clus_sumet',
              path    = 'met',
              xmin    = 0.,
              xmax    = 1000.,
              rebin   = 50,
              log     = False,
              )

met_trk_sumet = Var(name = 'met_trk_sumet',
              path    = 'met',
              xmin    = 0.,
              xmax    = 1000.,
              rebin   = 50,
              log     = False,
              )



vars_list = []


# ---------------
# for all studies
# ---------------
#"""
#vars_list.append(averageIntPerXing)
#vars_list.append(actualIntPerXing)
#vars_list.append(NPV)
#vars_list.append(nmuons)
#vars_list.append(nelectrons)
#vars_list.append(njets)
#vars_list.append(nmuonpairs)

#vars_list.append(mulead_pt)
#vars_list.append(mulead_eta)
#vars_list.append(mulead_phi)
#vars_list.append(mulead_trkd0)
#vars_list.append(mulead_trkd0sig)
#vars_list.append(mulead_trkz0)
#vars_list.append(mulead_trkz0sintheta)
#vars_list.append(mulead_ptvarcone30)

#vars_list.append(met_clus_et)
#vars_list.append(met_clus_phi)
#vars_list.append(met_clus_sumet)
#"""
#vars_list.append(met_trk_et)


#'''
# -------------
# taus
# -------------
#vars_list.append(taulead_pt)
#vars_list.append(taulead_phi)
#vars_list.append(taulead_eta)

#vars_list.append(taulead_ntrk)
#vars_list.append(tau_JetBDTScoreSigTrans)
vars_list.append(tausublead_pt)

#vars_list.append(jetlead_phi)
#vars_list.append(jetlead_pt)
#vars_list.append(jetlead_eta)

#vars_list.append(ntaus)
#vars_list.append(njets)
#vars_list.append(taujet_ptratio)
#vars_list.append(taujet_dphi)

#'''

# -------------
# FF
# -------------
#vars_list.append(tau_JetBDTScoreSigTrans)
#vars_list.append(taulead_pt)
#vars_list.append(taulead_eta)
#vars_list.append(jetlead_phi)
#vars_list.append(jetlead_eta)
#vars_list.append(taulead_ntrk)

# -------------
# tag-and-probe
# -------------
"""
vars_list.append(tag_pt)
vars_list.append(probe_pt)
vars_list.append(probe_ptiso)
vars_list.append(probe_ptiso)
vars_list.append(probe_ujet_pt)
vars_list.append(probe_ptvarcone30)
"""


# ---------------------
# just for fake-factors
# ---------------------
#"""
#vars_list.append(mujet_dphi)
#vars_list.append(scdphi)
#vars_list.append(jetlead_pt)
#"""

# ---------------------
# for validation
# ---------------------
"""
vars_list.append(musublead_pt)
vars_list.append(musublead_eta)
vars_list.append(musublead_phi)
vars_list.append(musublead_trkd0)
vars_list.append(musublead_trkd0sig)
vars_list.append(musublead_trkz0)
vars_list.append(musublead_trkz0sintheta)
vars_list.append(musublead_ptvarcone30)

vars_list.append(muons_mTtot)
vars_list.append(muons_mVis)
vars_list.append(muons_dphi)
vars_list.append(muons_deta)
vars_list.append(muons_dR)
vars_list.append(muons_pTH)
vars_list.append(muons_chargeprod)
"""


# ---------------------
# cutflows
# ---------------------
"""
vars_list.append(cutflow_presel)
vars_list.append(cutflow_weighted_presel)
vars_list.append(cutflow_ZCR)
vars_list.append(cutflow_weighted_ZCR)
"""

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


