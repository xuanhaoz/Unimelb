import os
import sys
import subprocess

from pyutils.utils import recreplace, mcstrings

from SamplesID import SampleID

## list jobs output
## it wildcards around jtagsamp!

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--samp', dest='sample',
                  help='sample name',metavar='SAMP',default="")
(options, args) = parser.parse_args()

# prototype of sample name
#user.tadej.SeeSaw.EXOT12MC.v1a.nominal.363355.e5525_e5984_s3126_r9781_r9778_p3371.rF1
#user.tadej.SeeSaw.EXOT22Data.v1a.fakes.data15_13TeV.periodD.physics_Main.r1

#user.fscutti.SSDiLep.SUSY11Data.v0.fakes.data17_13TeV.periodI.physics_Main.r3/

# --------------
user  = "fscutti"
#user  = "tadej"

samp  = options.sample

##jtag = "EX12MC.v3.sys.003"
#jtag = "HIGG3D3MC.v2.fakes"
#jtag = "EXOT22MC.v1a"
#jtag = "EXOT12Data.v1a"
jtag = "SUSY11Data.v2"

# append here any last tag 
# before the file type identifyier
append_id = "r3"

jtagsamp  = "%s.*%s*" % (jtag,samp)


jtype = "SSDiLep"
#jtype = "SeeSaw"

sys   = None
if not sys: sys = "nominal"

use_sample_id = True
# --------------


# --------------
if append_id: jtagsamp+=".%s"%append_id

SCRIPT     = os.path.join("/coepp/cephfs/mel/fscutti/Analysis/batch","Get.sh")
OUTDIR     = "/coepp/cephfs/mel/fscutti/ssdilep/%s" % (jtag)

if append_id: OUTDIR += ".%s"%append_id

OUTMERGED  = os.path.join(OUTDIR,"merged",sys)
OUTTREE    = os.path.join(OUTDIR,"tree",sys)
OUTMETA    = os.path.join(OUTDIR,"metadata",sys)
OUTCUTFLOW = os.path.join(OUTDIR,"cutflow",sys)
OUTLOGS    = os.path.join(OUTDIR,"log",sys)
JOB_TAG    = jtagsamp
QUEUE      = "long"
NCORES     = 1
# --------------

JOBDIR    = "/coepp/cephfs/mel/fscutti/jobdir" 
JOBTMP    = "/coepp/cephfs/mel/fscutti/jobtmp" 

dir_list = []
dir_list.append(JOBDIR)
dir_list.append(JOBTMP)
dir_list.append(os.path.join(OUTDIR,"tree"))
dir_list.append(os.path.join(OUTDIR,"tree",sys))
dir_list.append(os.path.join(OUTDIR,"metadata"))
dir_list.append(os.path.join(OUTDIR,"metadata",sys))
dir_list.append(os.path.join(OUTDIR,"cutflow"))
dir_list.append(os.path.join(OUTDIR,"cutflow",sys))
dir_list.append(os.path.join(OUTDIR,"merged"))
dir_list.append(os.path.join(OUTDIR,"merged",sys))
dir_list.append(os.path.join(OUTDIR,"log"))
dir_list.append(os.path.join(OUTDIR,"log",sys))

for d in dir_list:
 if not os.path.exists(d):
   os.makedirs(d)

outjobs_tree = "%s_%s_%s_tree.txt" % (user, jtype, jtagsamp)
outjobs_meta = "%s_%s_%s_metadata.txt" % (user, jtype, jtagsamp)
outjobs_cutflow = "%s_%s_%s_cutflow.txt" % (user, jtype, jtagsamp)

outjobs_tree = recreplace(outjobs_tree,[["*","X"]])
outjobs_meta = recreplace(outjobs_meta,[["*","X"]])
outjobs_cutflow = recreplace(outjobs_cutflow,[["*","X"]])


infile_tree = os.path.join(JOBDIR,outjobs_tree)
infile_meta = os.path.join(JOBDIR,outjobs_meta)
infile_cutflow = os.path.join(JOBDIR,outjobs_cutflow)

with open(infile_tree,"w") as f:
  cmd = "rucio list-dids"
  cmd += " %s.%s:" % ("user",user)
  cmd += "%s.%s.%s.*%s*tree*" % ("user",user,jtype,jtagsamp)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

with open(infile_meta,"w") as f:
  cmd = "rucio list-dids"
  cmd += " %s.%s:" % ("user",user)
  cmd += "%s.%s.%s.*%s*metadata*" % ("user",user,jtype,jtagsamp)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

with open(infile_cutflow,"w") as f:
  cmd = "rucio list-dids"
  cmd += " %s.%s:" % ("user",user)
  cmd += "%s.%s.%s.*%s*cutflow*" % ("user",user,jtype,jtagsamp)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

outputs = {}

rep = []
rep.append([" ",""])
rep.append(["\n",""])
rep.append(["|",""])
rep.append(["CONTAINER",""])
rep.append(["user.%s:"%user,""])

with open(infile_tree) as f: lines = f.readlines()
for l in lines:
  if not "CONTAINER" in l: continue
  if "duplicates" in l: continue
  key = recreplace(l.replace("_tree",""),rep)
  outputs[key] = {}
  print key
  outputs[key]["tree"] = recreplace(l,rep)
f.close()

with open(infile_cutflow) as f: lines = f.readlines()
for l in lines:
  if not "CONTAINER" in l: continue
  if "duplicates" in l: continue
  key = recreplace(l.replace("_cutflow",""),rep)
  outputs[key]["cutflow"] = recreplace(l,rep)
f.close()

with open(infile_meta) as f: lines = f.readlines()
for l in lines:
  if not "CONTAINER" in l: continue
  if "duplicates" in l: continue
  key = recreplace(l.replace("_metadata",""),rep)
  outputs[key]["metadata"] = recreplace(l,rep)
f.close()

jrep = []
jrep.append(["user",""])
jrep.append([user,""])
jrep.append([":",""])
jrep.append(["..",""])
jrep.append([".root",""])

for k,v in outputs.iteritems():
  print 'downloading %s ...' % k
  job_name = recreplace(k,jrep)
  if job_name.startswith("."): job_name = job_name[1:]
  
  # my config
  #if "physics_Main" in job_name: id = k.split(".")[7]+"_"+k.split(".")[6]
  #else: id = k.split(".")[5]
  
  # tadej config
  if "physics_Main" in job_name: id = k.split(".")[6]+"_"+k.split(".")[7]
  else: id = k.split(".")[6]
  
  # replace number with name of sample
  if use_sample_id  and not "physics_Main" in job_name:
    id = SampleID[int(id)]
  
  merged = recreplace(id, mcstrings)
  
  vars=[]
  vars+=["JOBTMP=%s"        % JOBTMP                 ]
  vars+=["NCORES=%d"        % NCORES                 ]
  vars+=["TREEFILE=%s"      % v["tree"]              ]
  vars+=["METAFILE=%s"      % v["metadata"]          ]
  vars+=["CUTFLOWFILE=%s"   % v["cutflow"]           ]
  vars+=["MERGEDTREE=%s"    % merged+"_tree.root"    ] 
  vars+=["MERGEDMETA=%s"    % merged+"_metadata.root"] 
  vars+=["MERGEDCUTFLOW=%s" % merged+"_cutflow.root" ] 
  vars+=["OUTTREE=%s"       % OUTTREE                ]
  vars+=["OUTMETA=%s"       % OUTMETA                ]
  vars+=["OUTCUTFLOW=%s"    % OUTCUTFLOW             ]
  vars+=["MERGED=%s"        % merged+".root"         ]
  vars+=["OUTMERGED=%s"     % OUTMERGED              ]

  VARS = ','.join(vars)

  cmd = 'qsub'
  cmd += ' -l nodes=1:ppn=%d' % NCORES
  cmd += ' -q %s'             % QUEUE
  cmd += ' -v "%s"'           % VARS
  cmd += ' -N j.get.%s'       % job_name
  cmd += ' -j n -o %s'        % OUTLOGS
  cmd += ' -e %s'             % OUTLOGS
  cmd += ' %s'                % SCRIPT
  
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  print m.communicate()[0]
